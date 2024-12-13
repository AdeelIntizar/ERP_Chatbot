def extract_interview_details(query,qa_pipeline):
    questions = [
        "What is the candidate's name in this query?",
        "What is the field, stack, or position mentioned in this query?",
        "What is the day mentioned in this query?",
        "What is the time mentioned in this query?"
    ]

    answers = {}
    for question in questions:
        result = qa_pipeline({
            'context': query,
            'question': question
        })
        answers[question] = result['answer']

    candidate_name = answers["What is the candidate's name in this query?"]
    field_stack_position = answers["What is the field, stack, or position mentioned in this query?"]
    day = answers["What is the day mentioned in this query?"]
    time = answers["What is the time mentioned in this query?"]
    common_positions = ["software engineer", "developer", "manager", "analyst", "designer", "engineer"]
    candidate_name = candidate_name if candidate_name and candidate_name.lower() not in common_positions else None
    valid_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = day if day and day.lower() in valid_days else None
    time_keywords = ["am", "pm", ":"]
    time = time if time and any(keyword in time.lower() for keyword in time_keywords) else None

    return candidate_name, field_stack_position, day, time