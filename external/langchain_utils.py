import random
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

import getpass
import os

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

rag_chain = (
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
    return f"""
    hãy tạo một câu hỏi trắc nghiệm về bài {topic} theo định dạng sau:
    Question: <question_content>
    A: <answer_choice_a>
    B: <answer_choice_b>
    C: <answer_choice_c>
    D: <answer_choice_d>
    Correct Answer: <correct_answer>
    """

def parse_question_response(response):
    print(response)
    lines = response.strip().split("\n")
    return {
        "content": lines[0].replace("Question: ", "").strip(),
        "answer_a": lines[1].replace("A: ", "").strip(),
        "answer_b": lines[2].replace("B: ", "").strip(),
        "answer_c": lines[3].replace("C: ", "").strip(),
        "answer_d": lines[4].replace("D: ", "").strip(),
        "true_answer": lines[5].replace("Correct Answer: ", "").strip()
    }

def generate_questions():
    questions = []
    for i in range(3):
        structured_prompt = create_structured_prompt()
        question_response = rag_chain.invoke(structured_prompt)
        question = parse_question_response(question_response)
        questions.append(question)
        print(question)
    return questions
