import re
def extract_info_with_bert(query,qa_pipeline):
    questions = [
        "What is the project name or number in this query?",
        "What is the amount mentioned in this query?",
        "What is the reason for the request in this query?"
    ]
    
    answers = {}
    for question in questions:
        result = qa_pipeline({
            'context': query,
            'question': question
        })
        answers[question] = result['answer']
    
    project = answers["What is the project name or number in this query?"]
    amount = answers["What is the amount mentioned in this query?"]
    reason = answers["What is the reason for the request in this query?"]
    project = project if project and not any(word in project.lower() for word in ["money", "usd", "riyals", "amount"]) else None
    amount = amount if amount and any(word in amount.lower() for word in ["usd", "riyals", "inr", "eur", "sar"]) else None
    reason_keywords = ["to", "because", "want", "need", "request"]
    reason = reason if any(keyword in reason.lower() for keyword in reason_keywords) else None
    return project, amount, reason
def print_msg(missing_features):
    ret_str=f"Some of the details are missing. Can you please enter  {missing_features}"
    return ret_str
def extract_amount(amount_str):

    match = re.match(r'(\d+)', amount_str)
    if match:
        # Return the integer value of the extracted digits
        return int(match.group(1))
    return None