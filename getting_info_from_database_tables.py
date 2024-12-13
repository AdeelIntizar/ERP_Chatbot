import psycopg2

db_params = {
    'dbname': 'ERP',  
    'user': 'postgres',  
    'password': 'adeel123',  
    'host': 'localhost',  
    'port': '5432'  
}
def details_for_money_request(project_id):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        select_query = '''
        SELECT money_id, project_id, project_name, amount, reason
        FROM Money
        WHERE project_id = %s;
        '''
        cursor.execute(select_query, (project_id,))
        project_details = cursor.fetchone()

        if project_details:
            return project_details
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_money_table(project_id, updated_amount, updated_reason):

    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()


        update_query = '''
        UPDATE Money
        SET amount = %s, reason = %s
        WHERE project_id = %s;
        '''
        cursor.execute(update_query, (updated_amount, updated_reason, project_id))
        
        conn.commit()
        print("Money table updated successfully.")

    except Exception as e:
        print(f"Error updating the Money table: {e}")

    finally:

        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_employee_performance(employee_id):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Query to fetch the employee performance details
        query = '''
        SELECT employee_id, employee_name, position, designation, performance
        FROM employee_performance
        WHERE employee_id = %s;
        '''

        # Execute the query with the employee ID as the parameter
        cursor.execute(query, (employee_id,))
        employee_details = cursor.fetchone()

        # Check if employee details are found
        if employee_details:
            return employee_details
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def get_project_details(project_id):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Query to fetch the project details
        query = '''
        SELECT project_name, project_details, start_date, end_date, milestones, number_of_resources
        FROM Projects
        WHERE project_id = %s;
        '''

        # Execute the query with the project ID as the parameter
        cursor.execute(query, (project_id,))
        project_details = cursor.fetchone()

        # Check if project details are found
        if project_details:
            return project_details
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def insert_interview_details(candidate_name, candidate_position, interview_day, interview_time):
    try:

        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Insert interview details into the interview table
        insert_query = '''
        INSERT INTO interview (candidate_name, candidate_position, interview_day, interview_time)
        VALUES (%s, %s, %s, %s);
        '''
        cursor.execute(insert_query, (candidate_name, candidate_position, interview_day, interview_time))
        conn.commit()  

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_client_query_details(project_id):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Query to get project details from the client_queries table based on project_id
        query = '''
        SELECT * FROM client_queries WHERE project_id = %s;
        '''
        
        cursor.execute(query, (project_id,))
        result = cursor.fetchone()  # Fetch one row

        # Return the result if found, otherwise None
        return result

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def fetch_and_print_inventory():
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Fetch all records from the inventory table
        fetch_query = "SELECT * FROM inventory;"
        cursor.execute(fetch_query)

        # Get all rows from the result
        inventory_data = cursor.fetchall()

        # Return and print data outside the function
        return inventory_data

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()