import difflib
import random
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
import os

def get_rag():
    os.environ["OPENAI_API_KEY"] = "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"

    llm = ChatOpenAI(model="gpt-4o-mini")

    # LangChain initialization logic here
    module_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(module_path, 'data.txt')

    loader = TextLoader(file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()
    prompt = hub.pull("rlm/rag-prompt")

    return (
        {"context": retriever | (lambda docs: "\n\n".join(doc.page_content for doc in docs)), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

# Functions to generate and parse questions
def create_structured_prompt():
    topics = [
        "KHÁI QUÁT CHUNG VỀ AN TOÀN VÀ BẢO HỘ LAO ĐỘNG",
        "SỨC KHOẺ VÀ AN TOÀN TẠI NƠI LÀM VIỆC",
        "KHOA HỌC VỀ LAO ĐỘNG",
        "AN TOÀN XƯỞNG CƠ KHÍ",
        "AN TOÀN PHÒNG CHÁY CHỮA CHÁY",
        "QUẢN LÝ NỘI VI 5S"
    ]
    topic = random.choice(topics)
    is_multiple_choice = random.choice([True, False])  # Randomly choose the question type

    if is_multiple_choice:
        return {
            'prompt': f"""
                Hãy tạo một câu hỏi trắc nghiệm về bài {topic} theo định dạng sau:
                Question: <question_content>
                A: <answer_choice_a>
                B: <answer_choice_b>
                C: <answer_choice_c>
                D: <answer_choice_d>
                Correct Answer: <correct_answer>
            """,
            'is_multiple_choice': True
        }
    else:
        return {
            'prompt': f"""
                Hãy tạo một câu hỏi điền vào chỗ trống về bài {topic}:
                Question: <question_content>
                Correct Answer: <correct_answer_text>
            """,
            'is_multiple_choice': False
        }

def parse_question_response(response, is_multiple_choice):
    print(response)
    lines = response.strip().split("\n")
    if is_multiple_choice:
        return {
            'content': lines[0].replace("Question: ", "").strip(),
            'answer_a': lines[1].replace("A: ", "").strip(),
            'answer_b': lines[2].replace("B: ", "").strip(),
            'answer_c': lines[3].replace("C: ", "").strip(),
            'answer_d': lines[4].replace("D: ", "").strip(),
            'true_answer': lines[5].replace("Correct Answer: ", "").strip(),
            'is_multiple_choice': True
        }
    else:
        return {
            'content': lines[0].replace("Question: ", "").strip(),
            'true_answer_text': lines[1].replace("Correct Answer: ", "").strip(),
            'is_multiple_choice': False
        }

def generate_questions(question_num):
    rag_chain = get_rag()
    questions = []
    for i in range(question_num):
        prompt_data = create_structured_prompt()
        question_response = rag_chain.invoke(prompt_data['prompt'])
        question = parse_question_response(question_response, prompt_data['is_multiple_choice'])
        questions.append(question)
    return questions

import numpy as np

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)


def are_sentences_similar_llm(sentence1, sentence2, threshold=0.85):

    os.environ["OPENAI_API_KEY"] = "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"
    embedding_model = OpenAIEmbeddings()

    # Get embeddings for both sentences
    sentence1_embedding = embedding_model.embed_query(sentence1)
    sentence2_embedding = embedding_model.embed_query(sentence2)

    # Compute cosine similarity between the two sentence embeddings
    similarity = cosine_similarity(sentence1_embedding, sentence2_embedding)

    # If the similarity exceeds the threshold, consider them similar
    return similarity >= threshold
