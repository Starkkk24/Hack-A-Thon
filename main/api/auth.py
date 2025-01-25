from flask import Blueprint, jsonify, request
import sqlite3
import random
import string

auth = Blueprint('auth', __name__)



import sqlite3

def ids_db():
    # Connect to the database
    connection = sqlite3.connect("user.db")  # Replace with your DB path
    cursor = connection.cursor()
    
    try:
        # Query to fetch both id and user_id from the all_id table
        cursor.execute("SELECT id, user_id FROM all_id")
        result = cursor.fetchall()
        
        # Separate id and user_id into two lists
        id_list = [row[0] for row in result]
        user_id_list = [row[1] for row in result]
        # print(id_list)
        print(user_id_list)
        return [True, id_list, user_id_list]
    except Exception as e:
        # Handle any exceptions and return an error code
        print(f"Error: {e}")
        return [False, "102"]
    finally:
        # Close the connection
        connection.close()



def unique_code(existing_codes, static_start):
    while True:
        
        # Generate a random 4-letter code
        random_part = ''.join(random.choices(string.ascii_uppercase, k=4))
        new_code = static_start + random_part
        
        # Check if the code is unique
        if new_code not in existing_codes:  # Add the new code to the list
            return new_code



def insert_user(id, user, name, dept, code, type, under=""):
    tn = ""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("user.db")  # Use the correct database file name
        cursor = conn.cursor()
        
        # SQL query to insert data
        if type == "M" or type == "C":
            query = "INSERT INTO main (id, user_id, name, dept, code) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (id, user, name, dept, code))
        
            # Execute the query
        else:
            query = "INSERT INTO sub (id, user_id, name, dept, code, under) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (id, user, name, dept, code, under))
            tn = under


        query1 = "INSERT INTO all_id (id, user_id, dept) VALUES (?, ?, ?)"
        cursor.execute(query1, (id, user, dept))
        
        # Commit the transaction
        conn.commit()
        
        return [True, id, user, name, dept, tn]

    except sqlite3.IntegrityError as e:
        # Log detailed IntegrityError information
        return [False, "103"]
    except Exception as e:
        # Log unexpected errors
        return [False, "104"]
    finally:
        # Ensure connection is closed
        if 'conn' in locals():
            conn.close()


def reg_def(type, user_id, name, dept, code, un):
    load = ids_db()
    if load[0] == False:
        return [False, "105"]
    ur = load[2]
    load = load[1]
    if user_id in ur:
        return [False, "101"]
    if load[0]:
        idz = unique_code(load[1], type)
        load1 = insert_user(idz, user_id, name, dept, code, type, un)
        return load1 
    else:
        return [False, "106"]

def log_def():
    pass

@auth.route('/web/reg', methods=['POST'])
def auth_reg():
    un = ""
    data = request.form.to_dict()
    if data["dept"] == "Manager":
        t = "M"
    elif data["dept"] == "site":
        t = "S"
        un = data["under"]
    elif data["dept"] == "Normal":
        t = "C"
    
    ret = reg_def(t, data["user"], data["name"], data["dept"], data["code"], un)
    
    return jsonify(message=ret), 200


@auth.route('/web/log', methods=['GET'])
def auth_log():
    user_id = request.args.get('userid')
    code = request.args.get('code')


    return jsonify(message="This is API endpoint 2"), 200
