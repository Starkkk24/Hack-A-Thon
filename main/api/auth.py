from flask import Blueprint, jsonify, request
import sqlite3
import random
import string

auth = Blueprint('auth', __name__)



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
            query1 = "INSERT INTO sub_all (id, user_id, under) VALUES (?, ?, ?)"
            cursor.execute(query1, (id, user, under))
            tn = under


        query1 = "INSERT INTO all_id (id, user_id, dept) VALUES (?, ?, ?)"
        cursor.execute(query1, (id, user, dept))
        
        # Commit the transaction
        conn.commit()
        
        return [True, id, user, name, dept, tn, code]

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


def check_user_and_fetch_data(user_id):
    user_id = str(user_id)
    print(user_id, 100)
    connection = sqlite3.connect("user.db")  # Replace with your database file path
    cursor = connection.cursor()
    
    try:
        # Check if user_id exists in the all_id table
        cursor.execute("SELECT id FROM all_id WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()

        if not result:
            # user_id does not exist in all_id table
            return [False, 201]

        # Extract the id associated with the user_id
        user_id_in_all_id = result[0]

        # Determine which table to search
        if user_id_in_all_id.startswith("M") or user_id_in_all_id.startswith("C"):
            # Search in the main table
            cursor.execute("SELECT * FROM main WHERE id = ?", (user_id_in_all_id,))
        else:
            # Search in the sub table
            cursor.execute("SELECT * FROM sub WHERE id = ?", (user_id_in_all_id,))

        # Fetch all rows from the query
        data = cursor.fetchall()

        # Return the data
        return [True, data]

    except Exception as e:
        try:
            load = number(user_id)
            return [True, load]
        except Exception as e:
            print(f"Error: {e}")
            return [False, "202"]
        finally:
            # Close the connection
            connection.close()
    finally:
        # Close the connection
        connection.close()


def number(user_id):
    user_id = str(user_id)
    print(user_id)
    connection = sqlite3.connect("user.db")  # Replace with your database file path
    cursor = connection.cursor()
    
    try:
        # Check if user_id exists in the all_id table
        cursor.execute("SELECT id FROM all_id WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()

        if not result:
            # user_id does not exist in all_id table
            return [False, 201]

        # Extract the id associated with the user_id
        user_id_in_all_id = result[0]

        # Determine which table to search
        if user_id_in_all_id.startswith("M") or user_id_in_all_id.startswith("C"):
            # Search in the main table
            cursor.execute("SELECT * FROM main WHERE id = ?", (user_id_in_all_id,))
        else:
            # Search in the sub table
            cursor.execute("SELECT * FROM sub WHERE id = ?", (user_id_in_all_id,))

        # Fetch all rows from the query
        data = cursor.fetchall()

        # Return the data
        return [True, data]

    except Exception as e:
        print(f"Error: {e}")
        return [False, "202"]
    finally:
        # Close the connection
        connection.close()


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

def log_def(user, code):
    data = check_user_and_fetch_data(user)
    print(user, 200)
    print(data, 200)
    if data[0]:
        load = list(data[1][0])
        if load[1] == user:
            if load[4] == code:
                return data
            else:
                return [False, 203]
    else:
        return [False, 204]

def unique_code_n(existing_codes):
    while True:
        n = random.randint(10000, 99999)
        if str(n) not in existing_codes:  # Add the new code to the list
            return str(n)

def ids_sub_db():
    #  Connect to the database
    connection = sqlite3.connect("user.db")  # Replace with your DB path
    cursor = connection.cursor()
    
    try:
        # Query to fetch both id and user_id from the all_id table
        cursor.execute("SELECT id, user_id FROM sub_all")
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
# ef insert_user(id, user, name, dept, code, type, under=""):
def cre_site(name, code, un):
    load = ids_sub_db()
    print(load)
    if load[0] == False:
        return [False, "105"]
    ur = load[2]
    load = load[1]
    urs = unique_code_n(ur)
    idz = unique_code(load, "S")
    
    if load[0]:
        load1 = insert_user(idz, urs, name, "site", code, "S", un)
        return load1 
    else:
        return [False, "106"]

@auth.route('/web/reg', methods=['POST'])
def auth_reg():
    un = ""
    data = request.form.to_dict()
    print(data)
    if data['dept'] == "Manager":
        t = "M"
    elif data["dept"] == "site":
        t = "S"
        ret = cre_site(data["name"], data["code"], data["under"])
        return ret
        # un = data["under"]
    elif data["dept"] == "Normal":
        t = "C"
    else:
        return jsonify(message=False), 200
    
    ret = reg_def(t, data["user"], data["name"], data["dept"], data["name"], un)
    return jsonify(message=ret), 200


@auth.route('/web/log', methods=['GET'])
def auth_log():
    data = request.form.to_dict()
    print(data)
    user_id = request.args.get('userid')
    code = request.args.get('code')
    print(user_id, code)
    load = log_def(user_id, code)
    return jsonify(message=load), 200



