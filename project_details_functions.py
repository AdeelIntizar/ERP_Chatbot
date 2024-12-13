def extract_project_details(query,qa_pipeline):
    questions = [
        "What is the project name mentioned in this query?",
        "What is the project number mentioned in this query?"
    ]
    
    answers = {}
    for question in questions:
        result = qa_pipeline({
            'context': query,
            'question': question
        })
        answers[question] = result['answer']
    
    project_name = answers["What is the project name mentioned in this query?"]
    project_number = answers["What is the project number mentioned in this query?"]
    project_name = project_name if project_name and not project_name.isdigit() else None
    project_number = project_number if project_number and project_number.isdigit() else None
    
    return project_name, project_number