import psycopg2
db_params = {
    'dbname': 'ERP',  
    'user': 'postgres',  
    'password': 'adeel123',  
    'host': 'localhost',  
    'port': '5432'  
}

def create_money_table_and_insert_data():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        create_money_table_query = '''
        CREATE TABLE IF NOT EXISTS Money (
            money_id SERIAL PRIMARY KEY,
            project_id INTEGER REFERENCES Projects(project_id) ON DELETE CASCADE,
            project_name VARCHAR(255) NOT NULL,
            amount DECIMAL(15, 2),  -- Can be NULL for now
            reason TEXT  -- Can be NULL for now
        );
        '''
        cursor.execute(create_money_table_query)
        conn.commit()
        select_projects_query = '''
        SELECT project_id, project_name
        FROM Projects;
        '''
        cursor.execute(select_projects_query)
        projects = cursor.fetchall()
        insert_money_query = '''
        INSERT INTO Money (project_id, project_name, amount, reason)
        VALUES (%s, %s, %s, %s);
        '''
        for project in projects:
            project_id = project[0]
            project_name = project[1]
            cursor.execute(insert_money_query, (project_id, project_name, None, None))

        conn.commit()
        print("Money table created and projects inserted successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


create_money_table_and_insert_data()









