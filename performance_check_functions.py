import random
def extract_employee_id(query, qa_pipeline):
    question = "What is the employee ID mentioned in this query?"
    result = qa_pipeline(question=question, context=query)  # Updated syntax
    employee_id = result['answer']
    if employee_id and employee_id.isdigit():
        return employee_id
    return None
def get_random_employee_id_prompt():
    employee_id_prompts = [
        "Bot : Can you please provide your employee ID?",
        "Bot : May I have your employee ID to proceed?",
        "Bot : I’ll need your employee ID to assist you. Please enter it.",
        "Bot : Could you share your employee ID?",
        "Bot : Kindly provide your employee ID.",
    ]
    return random.choice(employee_id_prompts)