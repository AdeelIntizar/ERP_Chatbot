import psycopg2
db_params = {
    'dbname': 'ERP', 
    'user': 'postgres',
    'password': 'adeel123',  
    'host': 'localhost',  
    'port': '5432'  
}
def create_and_insert_employees():
    try:

        conn = psycopg2.connect(**db_params)  
        cursor = conn.cursor()
        create_table_query = '''
        CREATE TABLE employees (
            employee_id SERIAL PRIMARY KEY,
            employee_name VARCHAR(100),
            position VARCHAR(50),
            joining_date DATE,
            salary NUMERIC(12, 2),
            designation VARCHAR(50)
        );
        '''
        
        insert_employees_query = '''
        INSERT INTO employees (employee_name, position, joining_date, salary, designation) VALUES
        ('John Doe', 'AI Engineer', '2021-01-01', 120000.00, 'Senior'),
        ('Jane Smith', 'ML Engineer', '2020-05-15', 95000.00, 'Junior'),
        ('Mark Johnson', 'Full Stack Engineer', '2019-08-30', 110000.00, 'Team Lead'),
        ('Emily Davis', 'Data Analyst', '2021-06-20', 70000.00, 'Junior'),
        ('David Martinez', 'UI/UX Designer', '2020-02-10', 80000.00, 'Senior'),
        ('Sarah Wilson', 'Backend Engineer', '2021-07-01', 72000.00, 'Junior'),
        ('Michael Brown', 'MERN Stack Engineer', '2020-11-12', 85000.00, 'Senior'),
        ('Rachel Miller', 'Frontend Engineer', '2019-03-25', 95000.00, 'Senior'),
        ('James Anderson', 'AI Engineer', '2021-09-09', 105000.00, 'Junior'),
        ('Lily Clark', 'ML Engineer', '2021-03-20', 80000.00, 'Junior'),
        ('Daniel Thomas', 'HR', '2018-01-01', 60000.00, 'Associate'),
        ('Olivia Taylor', 'Project Manager', '2017-05-15', 120000.00, 'Team Lead'),
        ('Henry Lee', 'Backend Engineer', '2019-06-30', 115000.00, 'Senior'),
        ('Sophia Harris', 'Frontend Engineer', '2020-04-05', 75000.00, 'Junior'),
        ('William Lewis', 'UI/UX Designer', '2018-02-22', 95000.00, 'Senior'),
        ('Charlotte Young', 'AI Engineer', '2019-09-30', 100000.00, 'Team Lead'),
        ('Mason Hall', 'Data Analyst', '2020-07-21', 78000.00, 'Junior'),
        ('Isabella Allen', 'MERN Stack Engineer', '2021-05-11', 81000.00, 'Junior'),
        ('Aiden Walker', 'Project Manager', '2020-10-03', 115000.00, 'Senior'),
        ('Grace Scott', 'Backend Engineer', '2021-02-19', 95000.00, 'Senior'),
        ('Lucas Wright', 'ML Engineer', '2021-08-18', 88000.00, 'Senior'),
        ('Ethan Adams', 'UI/UX Designer', '2020-12-25', 70000.00, 'Junior'),
        ('Madison Baker', 'AI Engineer', '2018-09-14', 120000.00, 'Senior'),
        ('Jackson Carter', 'Data Analyst', '2019-02-12', 85000.00, 'Senior'),
        ('Mila Gonzalez', 'MERN Stack Engineer', '2018-12-30', 95000.00, 'Associate'),
        ('Elijah Nelson', 'Backend Engineer', '2020-11-07', 100000.00, 'Team Lead'),
        ('Harper Perez', 'Frontend Engineer', '2021-04-13', 72000.00, 'Junior'),
        ('Abigail Mitchell', 'UI/UX Designer', '2020-08-25', 95000.00, 'Senior'),
        ('Evelyn Roberts', 'Project Manager', '2017-11-03', 110000.00, 'Team Lead'),
        ('Charlotte Green', 'Data Analyst', '2021-07-18', 78000.00, 'Junior'),
        ('Liam King', 'ML Engineer', '2019-10-20', 95000.00, 'Senior');
        '''
        cursor.execute(create_table_query)
        cursor.execute(insert_employees_query)
        conn.commit()

        print("Employees table created and records inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()






def insert_employee_performance():
    try:
        conn = psycopg2.connect(**db_params) 
        cursor = conn.cursor()
        create_table_query ='''
        CREATE TABLE employee_performance (
        performance_id SERIAL PRIMARY KEY,
        employee_id INT REFERENCES employees(employee_id),
        employee_name VARCHAR(100),
        position VARCHAR(50),
        designation VARCHAR(50),
        performance TEXT
            );'''

        insert_performance_query = '''
        INSERT INTO employee_performance (employee_id, employee_name, position, designation, performance) VALUES
        (1, 'John Doe', 'AI Engineer', 'Senior', 'Behaviour: Outstanding, but technically need to work on.'),
        (2, 'Jane Smith', 'ML Engineer', 'Junior', 'Unreliable, needs improvement in commitment.'),
        (3, 'Mark Johnson', 'Full Stack Engineer', 'Team Lead', 'Excellent, never disappoints. A reliable leader.'),
        (4, 'Emily Davis', 'Data Analyst', 'Junior', 'Performance meets expectations, can improve speed of analysis.'),
        (5, 'David Martinez', 'UI/UX Designer', 'Senior', 'Highly creative but needs better collaboration with developers.'),
        (6, 'Sarah Wilson', 'Backend Engineer', 'Junior', 'Needs improvement in technical skills, has potential.'),
        (7, 'Michael Brown', 'MERN Stack Engineer', 'Senior', 'Excellent technical skills, needs improvement in communication.'),
        (8, 'Rachel Miller', 'Frontend Engineer', 'Senior', 'Outstanding in front-end development, a key player in the team.'),
        (9, 'James Anderson', 'AI Engineer', 'Junior', 'Needs improvement in problem-solving skills, promising future.'),
        (10, 'Lily Clark', 'ML Engineer', 'Junior', 'Unreliable in meeting deadlines, can improve communication.'),
        (11, 'Daniel Thomas', 'HR', 'Associate', 'Understands employee issues well, sometimes lacks in technical understanding.'),
        (12, 'Olivia Taylor', 'Project Manager', 'Team Lead', 'Excellent leadership, makes the team always strive for success.'),
        (13, 'Henry Lee', 'Backend Engineer', 'Senior', 'Highly skilled technically, needs to focus on team collaboration.'),
        (14, 'Sophia Harris', 'Frontend Engineer', 'Junior', 'Good understanding of front-end concepts, needs better consistency.'),
        (15, 'William Lewis', 'UI/UX Designer', 'Senior', 'Creative and innovative, highly dependable in projects.'),
        (16, 'Charlotte Young', 'AI Engineer', 'Team Lead', 'Needs to improve delegation skills, technically strong leader.'),
        (17, 'Mason Hall', 'Data Analyst', 'Junior', 'Good at analysis but needs to improve reporting efficiency.'),
        (18, 'Isabella Allen', 'MERN Stack Engineer', 'Junior', 'Technical skills are good, needs improvement in problem-solving.'),
        (19, 'Aiden Walker', 'Project Manager', 'Senior', 'Excellent strategic thinker, drives the team towards success.'),
        (20, 'Grace Scott', 'Backend Engineer', 'Senior', 'Outstanding in backend technologies, needs to improve communication.'),
        (21, 'Lucas Wright', 'ML Engineer', 'Senior', 'Exceptional work on machine learning models, sometimes too focused on detail.'),
        (22, 'Ethan Adams', 'UI/UX Designer', 'Junior', 'Needs to improve collaboration with development teams, creative but isolated.'),
        (23, 'Madison Baker', 'AI Engineer', 'Senior', 'Excellent technical skills, can sometimes be too self-sufficient.'),
        (24, 'Jackson Carter', 'Data Analyst', 'Senior', 'Highly reliable, analysis is precise and on time.'),
        (25, 'Mila Gonzalez', 'MERN Stack Engineer', 'Associate', 'Needs to work on coding skills but shows promise.'),
        (26, 'Elijah Nelson', 'Backend Engineer', 'Team Lead', 'Technical excellence, struggles with delegation and team collaboration.'),
        (27, 'Harper Perez', 'Frontend Engineer', 'Junior', 'Hardworking but needs more technical knowledge.'),
        (28, 'Abigail Mitchell', 'UI/UX Designer', 'Senior', 'Excellent eye for design, always meets deadlines.'),
        (29, 'Evelyn Roberts', 'Project Manager', 'Team Lead', 'Strong leadership, excellent project execution skills.'),
        (30, 'Charlotte Green', 'Data Analyst', 'Junior', 'Capable of good analysis, but needs to work on report writing skills.'),
        (31, 'Liam King', 'ML Engineer', 'Senior', 'Consistently delivers, needs to work on documentation quality.');
        '''
        cursor.execute(create_table_query)

        cursor.execute(insert_performance_query)

        conn.commit()
        print("Performance records inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()







def create_interview_table():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS interview (
            candidate_id SERIAL PRIMARY KEY,
            candidate_name VARCHAR(255),
            candidate_position VARCHAR(255),
            interview_day VARCHAR(50),  -- This allows storing days like 'Monday'
            interview_time VARCHAR(50)  -- This allows storing time like '3 pm'
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()  
        print("Interview table created successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()






def create_client_queries_table():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS client_queries (
            query_id SERIAL PRIMARY KEY,
            project_id INT REFERENCES Projects(project_id),
            project_name VARCHAR(255),
            latest_query TEXT,
            resolved BOOLEAN
        );
        '''
        cursor.execute(create_table_query)
        conn.commit() 
        print("Client queries table created successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def insert_client_queries():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO client_queries (project_id, project_name, latest_query, resolved)
        VALUES
        (1, 'Developing a Shopify Web Application', 'What is the current status of the payment gateway integration?', FALSE),
        (2, 'AI Model for Spoof Detection', 'Can we integrate the model with our security system?', TRUE),
        (3, 'AI Recommendation System for Economic Experts', 'Are the training results available for the model?', FALSE),
        (4, 'Mobile App for Smart Home Automation', 'Have all the smart devices been successfully connected?', TRUE),
        (5, 'AI-Powered Diagnostic Tool for Healthcare', 'Can we get a report on the current accuracy of the model?', FALSE),
        (6, 'Blockchain-Based Voting System', 'Is the voting system ready for user testing?', TRUE),
        (7, 'Web Application for Virtual Team Collaboration', 'When will the real-time chat feature be implemented?', FALSE),
        (8, 'AI-Powered Fraud Detection System', 'Has the feature engineering for fraud detection been completed?', TRUE),
        (9, 'Cloud-Based Inventory Management System', 'Can you provide an update on the inventory tracking feature?', FALSE),
        (10, 'Smart Wearable Device for Health Monitoring', 'Are there any updates on the wearable device design?', TRUE),
        (11, 'Developing a Shopify Web Application', 'What is the current status of the product page design?', FALSE),
        (12, 'AI Model for Spoof Detection', 'When can we start integrating the model with security systems?', TRUE),
        (13, 'AI Recommendation System for Economic Experts', 'Do we need to collect more data for the recommendation system?', FALSE),
        (14, 'Mobile App for Smart Home Automation', 'Can you update the status of the mobile app user interface?', TRUE),
        (15, 'AI-Powered Diagnostic Tool for Healthcare', 'Is the model currently optimized for faster diagnosis?', FALSE),
        (16, 'Blockchain-Based Voting System', 'Is there any delay in the blockchain development phase?', TRUE),
        (17, 'Web Application for Virtual Team Collaboration', 'Are there any issues with the task management feature?', FALSE),
        (18, 'AI-Powered Fraud Detection System', 'Can we get an update on the system integration process?', TRUE),
        (19, 'Cloud-Based Inventory Management System', 'Is there a bug in the real-time inventory tracking system?', FALSE),
        (20, 'Smart Wearable Device for Health Monitoring', 'Are there any challenges with health analysis on the wearable device?', TRUE);
        '''

        cursor.execute(insert_query)
        conn.commit() 
        print("Client queries inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()




def create_inventory_table_and_insert_data():
    try:

        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS inventory (
            item_id SERIAL PRIMARY KEY,
            item_name VARCHAR(255),
            number_of_items INT,
            last_purchased DATE,
            items_not_in_use INT,
            items_low_and_needed_to_be_purchased INT
        );
        '''
        cursor.execute(create_table_query)


        insert_query = '''
        INSERT INTO inventory (item_name, number_of_items, last_purchased, items_not_in_use, items_low_and_needed_to_be_purchased)
        VALUES 
        ('Microsoft Office License', 50, '2023-10-15', 5, 10),
        ('Windows OS License', 30, '2023-09-20', 0, 10),
        ('Adobe Photoshop License', 25, '2023-08-10', 3, 6),
        ('Zoom License', 20, '2023-07-05', 0, 5),
        ('Slack License', 40, '2023-06-12', 8, 10),
        ('IntelliJ IDEA License', 10, '2023-11-25', 2, 4),
        ('Jira License', 15, '2023-10-18', 0, 4),
        ('Google Drive Storage', 60, '2023-09-30', 5, 12),
        ('Microsoft Teams License', 50, '2023-08-22', 1, 3),
        ('GitHub Enterprise License', 35, '2023-07-10', 0, 5),
        ('Dropbox Storage', 30, '2023-05-17', 0, 7),
        ('Zoom Meeting Equipment', 10, '2023-09-01', 3, 7),
        ('Smartphone Devices for Office', 12, '2023-06-25', 0, 3),
        ('Office Workstations', 25, '2023-05-20', 0, 5),
        ('Projector for Meeting Room', 5, '2023-10-10', 0, 2);
        '''
        cursor.execute(insert_query)

        # Commit the transaction
        conn.commit()

        print("Inventory table created and data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def create_project_table():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Projects (
            project_id SERIAL PRIMARY KEY,
            project_name VARCHAR(255) NOT NULL,
            project_details TEXT,
            start_date DATE,
            end_date DATE,
            milestones TEXT,
            number_of_resources INTEGER
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'Projects' created successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



def insert_into_project_table():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        projects = [
            ('Developing a Shopify Web Application', 'Develop an e-commerce platform using Shopify.', '2024-01-01', '2024-06-01', 'Complete product page and payment gateway integration.', 4),
            ('AI Model for Spoof Detection', 'Develop an AI model to detect deepfake or spoofed videos using neural networks.', '2024-02-01', '2024-07-01', 'Train on dataset, integrate model with security systems.', 6),
            ('AI Recommendation System for Economic Experts', 'Create a recommendation system for recommending economic experts to firms based on skills and experience.', '2024-03-01', '2024-09-01', 'Data collection, model training, deployment.', 5),
            ('Mobile App for Smart Home Automation', 'Develop a mobile application to control home automation devices.', '2024-04-01', '2024-08-01', 'Connect devices, integrate user interface.', 3),
            ('AI-Powered Diagnostic Tool for Healthcare', 'Develop an AI model for diagnosing diseases based on medical images.', '2024-05-01', '2024-10-01', 'Train on medical datasets, model optimization.', 7),
            ('Blockchain-Based Voting System', 'Design a decentralized voting system using blockchain technology for secure and transparent elections.', '2024-06-01', '2024-12-01', 'Blockchain development, user interface design, testing.', 5),
            ('Web Application for Virtual Team Collaboration', 'Build a web application for remote teams to collaborate on projects with real-time communication.', '2024-07-01', '2024-12-01', 'Real-time chat, file sharing, task management.', 4),
            ('AI-Powered Fraud Detection System', 'Develop an AI-based system for detecting fraudulent activities in financial transactions.', '2024-08-01', '2024-11-01', 'Model training, feature engineering, system integration.', 6),
            ('Cloud-Based Inventory Management System', 'Create a cloud application for tracking inventory in real-time across multiple locations.', '2024-09-01', '2024-12-01', 'Inventory tracking, cloud deployment, reporting tools.', 5),
            ('Smart Wearable Device for Health Monitoring', 'Design a wearable device that monitors health metrics and provides feedback to users.', '2024-10-01', '2025-03-01', 'Wearable device design, data collection, health analysis.', 6)
        ]
        insert_query = '''
        INSERT INTO Projects (project_name, project_details, start_date, end_date, milestones, number_of_resources)
        VALUES (%s, %s, %s, %s, %s, %s);
        '''
        for project in projects:
            cursor.execute(insert_query, project)

        conn.commit()
        print("10 projects have been successfully added to the table.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



# create_project_table()
# insert_into_project_table()
# create_and_insert_employees()
# create_interview_table()
# insert_employee_performance()
# create_client_queries_table()
# insert_client_queries()
# create_inventory_table_and_insert_data()
