# langchain_utils.py
from langchain_openai import ChatOpenAI
import os


def extract_incident_details(description, past_incidents):
    """
    Extract the incident type, location, severity, and corrective action
    from the description using LangChain and OpenAI GPT model.
    If the new incident is similar to any past incidents, return the same corrective action.
    Otherwise, return none for the corrective action.
    """

    # Set your OpenAI API key
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Initialize the model
    llm = ChatOpenAI(model="gpt-4o-mini")

    # Define the prompt for extraction
    prompt = f"""
    Với mô tả sự cố sau, hãy trích xuất loại sự cố, vị trí và mức độ nghiêm trọng.
    Mức độ nghiêm trọng phải là một trong các mức 'low', 'medium' hoặc 'high':
    Mô tả: {description}
    
    Trả lời theo định dạng sau:
    Loại sự cố: <incident_type>
    Vị trí: <location>
    Mức độ nghiêm trọng: <severity>
    """

    # Run the LLM to get the extracted information
    response = llm(prompt)
    print(response)
    response_content = response.content

    # Parse the content manually using string manipulation (since it's already structured text)
    lines = response_content.split('\n')
    incident_type = ''
    location = ''
    severity = ''

    for line in lines:
        if line.startswith("Loại sự cố:"):
            incident_type = line.replace("Loại sự cố:", "").strip()
        elif line.startswith("Vị trí:"):
            location = line.replace("Vị trí:", "").strip()
        elif line.startswith("Mức độ nghiêm trọng:"):
            severity = line.replace("Mức độ nghiêm trọng:", "").strip()

    # If no past incidents, return the extracted details and no corrective action
    if not past_incidents:
        return incident_type, location, severity, None


    # Combine all past incidents into a single prompt for comparison and action generation
    past_incidents_text = "\n\n".join([f"Sự cố {i + 1}:\nMô tả: {incident['description']}\nHành động khắc phục: {incident['corrective_action']}" for i, incident in enumerate(past_incidents)])

    comparison_prompt = f"""
    So sánh mô tả sự cố mới sau đây với các sự cố trước đó và xác định xem có sự cố nào tương tự không.
    Nếu phát hiện sự cố tương tự, hãy tạo hành động khắc phục mới. Nếu không phát hiện sự cố tương tự nào, hãy đề xuất hành động khắc phục mới.

    Sự cố mới:
    Mô tả: {description}

    Sự cố trong quá khứ:
    {past_incidents_text}

    Trả lời bằng:
    Có bất kỳ sự cố nào trong quá khứ tương tự không? Nếu tương tự, hãy tạo hành động khắc phục bắt đầu bằng Hành động khắc phục:.
    """
    # Make a single API call to check similarity and generate a corrective action
    comparison_response = llm(comparison_prompt).content.strip()
    print(comparison_response)

    # Parse the response to extract similarity check and corrective action
    lines = comparison_response.split('\n')
    corrective_action = ''

    for line in lines:
        if line.startswith("Hành động khắc phục:"):
            corrective_action = line.replace("Hành động khắc phục:", "").strip()

    # Return the extracted details along with the generated corrective action
    return incident_type, location, severity, corrective_action