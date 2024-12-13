
import gradio as gr
from transformers import BertTokenizerFast, BertForSequenceClassification, pipeline
import torch
import pyttsx3
from getting_info_from_database_tables import details_for_money_request, fetch_and_print_inventory, update_money_table, get_employee_performance, get_project_details, insert_interview_details, get_client_query_details
from money_request_functions import extract_info_with_bert,print_msg,extract_amount
from performance_check_functions import extract_employee_id,get_random_employee_id_prompt
from project_details_functions import extract_project_details
from inter_scheduling_functions import extract_interview_details
from speech_functions import convert_text_to_speech,convert_to_text
def infer(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1).item()
    return prediction
def chatbot(engine,input_text, qa_pipeline):
    money_request_dict={"project":None,"amount":None,"reason":None}
    prediction = infer(input_text)
    print("prediction: ",prediction)
    if prediction == 0:
        bot_response = "Bot : For now I am assisting \n1-Scheduling Interview\n2-Checking Performance\n in Human Resource. Which specific service do you need my assistance with?"
    elif prediction == 1:
        bot_response = "Bot : I’m here to help with \n1-Requesting money for a project \nin Financial Management. What service do you want me to assist?"
    elif prediction == 2:
        bot_response = "Bot : I’m here to help with \n1-Track the inventory \nin Supply Chain Management. What service do you want me to assist?"
    elif prediction == 3:
        bot_response = "Bot : At the moment, I can assist with: \n1-Checking details of a project\n2-Asking for resource allocation for a project. Which of these would you like support for?"
    elif prediction == 4:
        bot_response = "Bot : Here’s how I can help: \n1-Customer queries regarding orders or services. What can I assist you with?"
    elif prediction==5:
        project, amount, reason = extract_info_with_bert(input_text,qa_pipeline)
        money_request_dict["project"] = money_request_dict["project"] or project
        money_request_dict["amount"] = money_request_dict["amount"] or amount
        money_request_dict["reason"] = reason
        if project.lower=="None" or project.lower() =="project":
            money_request_dict["project"]=None
        elif str(amount).lower() == "none" or str(amount).lower() == "amount" or str(amount).lower() == "money":
            money_request_dict["amount"]=None
        while None in [money_request_dict["project"], money_request_dict["amount"]]:
            missing_features = []
            if money_request_dict["project"] is None:
                missing_features.append("Project Name")
            if money_request_dict["amount"] is None:
                missing_features.append("Amount")
            ret_str = print_msg(", ".join(missing_features))
            convert_text_to_speech(engine,ret_str)
            new_query = convert_to_text(engine)
            project_update, amount_update, _ = extract_info_with_bert(new_query,qa_pipeline)
            if money_request_dict["project"] is None and project_update and not any(word in project_update.lower() for word in ["money", "usd", "riyals", "amount"]):
                money_request_dict["project"] = project_update
            if money_request_dict["amount"] is None and amount_update and any(word in amount_update.lower() for word in ["usd", "riyals", "inr", "eur", "sar"]):
                money_request_dict["amount"] = amount_update
        project_details=details_for_money_request(money_request_dict["project"])
        if project_details:
                new_str=f'''Are you sure you want to get {money_request_dict["amount"]} for {project_details[2]} project'''
                convert_text_to_speech(engine,new_str)
                new_query = convert_to_text(engine)
                if "yes" in new_query.lower():
                    bot_response=f'''Request for {money_request_dict["amount"]} for {project_details[2]} is accepted and {money_request_dict["amount"]} is granted to this project.'''

                    print("Project Details:")
                    print(f"Project ID: {project_details[1]}")
                    print(f"Project Name: {project_details[2]}")
                    print(f"Amount: {project_details[3]}")
                    amount_requested=extract_amount(money_request_dict["amount"])
                    current_amount = project_details[3] if project_details[3] else 0
                    current_reason = project_details[4] if project_details[4] else ""
                    updated_amount = current_amount + amount_requested
                    updated_reason = current_reason + " " + money_request_dict["reason"]
                    update_money_table(money_request_dict["project"],updated_amount,updated_reason)
                else:
                    bot_response=f'''No money is granted to {project_details[2]} project'''


        else:
            bot_response="Bot : No such projext exists"
            print(bot_response)
            convert_text_to_speech(engine,bot_response)
        

    elif prediction == 6:
        emp_id = extract_employee_id(input_text, qa_pipeline)
        while emp_id is None:
            bot_str = get_random_employee_id_prompt()
            engine = pyttsx3.init()
            convert_text_to_speech(engine,bot_str)
            
            print(bot_str)
            user_input = convert_to_text(engine)
            emp_id = extract_employee_id(user_input, qa_pipeline)

        employee_performance = get_employee_performance(emp_id)
        if employee_performance:
            bot_response = (f"The performance of {employee_performance[1]} who is working as {employee_performance[2]} is {employee_performance[4]}.")
            
        else:
            bot_response = "No performance details found for the given Employee ID."
    elif prediction==7:
        project_name, project_number=extract_project_details(input_text,qa_pipeline)
        while not project_number:
            bot_str="Bot : The project number seems to be missing. Can you please provide it?"
            print(bot_str)
            convert_text_to_speech(engine,bot_str)
            print("User : ")
            user_input = convert_to_text(engine)

            _, project_number = extract_project_details(user_input,qa_pipeline)
        project_details = get_project_details(project_number) 
        if project_details:
            print("Bot : Project Details\n")
            print(f"Project Name: {project_details[0]}")
            print(f"Project Details: {project_details[1]}")
            print(f"Start Date: {project_details[2]}")
            print(f"End Date: {project_details[3]}")
            print(f"Milestones: {project_details[4]}")
            print(f"Number of Resources: {project_details[5]}")
            bot_response=f'''The details of project {project_details[0]} are \n the projects is to {project_details[1]}  it was started on {project_details[2]} and its end date is {project_details[3]} the  milestoes of this projects are {project_details[4]} and the number of resources allocated to this projects are {project_details[5]}'''

        else:
            bot_response="I'm sorry, I couldn't find any details for the given Project ID." 
            print(bot_response)

    elif prediction==8:
        candidate_name, field_stack_position, day, time = extract_interview_details(input_text,qa_pipeline)
        missing_fields = []
        if not candidate_name:
            missing_fields.append("Candidate Name")
        if not field_stack_position:
            missing_fields.append("Field/Stack/Position")
        if not day:
            missing_fields.append("Day")
        if not time:
            missing_fields.append("Time")
        while missing_fields:
            bot_str="Bot : Some details are missing."
            print(bot_str)
            convert_text_to_speech(engine,bot_str)
            bot_str=f"Bot : Can you please provide the following details: {', '.join(missing_fields)}?"
            print(bot_str)
            convert_text_to_speech(engine,bot_str)
            user_input = convert_to_text(engine)
            new_candidate_name, new_field_stack_position, new_day, new_time = extract_interview_details(user_input,qa_pipeline)
            if not candidate_name and new_candidate_name:
                candidate_name = new_candidate_name
                missing_fields.remove("Candidate Name")
            if not field_stack_position and new_field_stack_position:
                field_stack_position = new_field_stack_position
                missing_fields.remove("Field/Stack/Position")
            if not day and new_day:
                day = new_day
                missing_fields.remove("Day")
            if not time and new_time:
                time = new_time
                missing_fields.remove("Time")
            new_str=f'''Are you sure you want to schedule an interview of {candidate_name} for  {field_stack_position} on {day} at {time}'''
            convert_text_to_speech(engine,new_str)
            new_input=convert_to_text(engine)
            if "yes"  in new_input.lower():
                insert_interview_details(candidate_name,field_stack_position,day,time)
                bot_response=f'''Bot : Interview has been scheduled for {candidate_name} for {field_stack_position} on {day} at {time}'''
                print(bot_response)
            else:
                bot_response=f'''Interview is not schduled for {candidate_name} for {field_stack_position} on {day} at {time}'''
                print(bot_response)
    elif prediction==9:
        inventory = fetch_and_print_inventory()
        if inventory:
            bot_response="Bot : In our inventory we have this information \n"
            print(bot_response)

            for row in inventory:
                bot_response+=f"We have {row[2]} number of {row[1]} and it was last purchased on {row[3]} and currenty we have {row[4]} number of {row[1]} which are not in use.\n"
                print(f"Item ID: {row[0]}, Item Name: {row[1]}, Number of Items: {row[2]}, Last Purchased: {row[3]}, Items Not in Use: {row[4]}, Items Low and Needed to Be Purchased: {row[5]}")
        else:
            bot_response="No inventory data found."
            print(bot_response)
    elif prediction==10:
        project_name, project_number=extract_project_details(input_text,qa_pipeline)
        while not project_number:
            bot_str="Bot : The project number seems to be missing. Can you please provide it?"
            print(bot_str)
            convert_text_to_speech(engine,bot_str)
            print("User : ")
            user_input = convert_to_text(engine)
            _, project_number = extract_project_details(user_input,qa_pipeline)
        project_details=get_client_query_details(project_number)
        if project_details:
            bot_response=f'''These are the latest queries of a client on  project {project_details[2]} \n {project_details[3]} and the status of queries are  {'Resolved' if project_details[4] else 'Not Resolved'}'''
            print(bot_response)
        else:
               bot_response=f"No record found for project_id: {project_number}"
               print(bot_response)
  
    else:
        bot_response = "Bot : I'm sorry, I didn't understand that. Can you please clarify?"

    convert_text_to_speech(engine, bot_response)
    str="Thank you using my service, see you again"
    convert_text_to_speech(engine, str)
    return bot_response
tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("checkpoint-210", use_safetensors=True)

def gradio_interface(user_input):
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")
    engine = pyttsx3.init()
    
    
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Zira" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    str="hello this is Rose How Can I assist you?"
    convert_text_to_speech(engine,str)
    user_input=convert_to_text(engine)
    return chatbot(engine,user_input, qa_pipeline)

with gr.Blocks() as demo:
    gr.Markdown("# ERP Bot")
    with gr.Row():
        
        user_input_box = None
    response_box = gr.Textbox(label="Bot Response", lines=4, interactive=False)
    with gr.Row():
        submit_button = gr.Button("Start")
    submit_button.click(gradio_interface, inputs=user_input_box, outputs=response_box)

demo.launch(share=True)
