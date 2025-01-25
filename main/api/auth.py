from flask import Blueprint, jsonify, request
import sqlite3

auth = Blueprint('auth', __name__)

import random
import string

import sqlite3

def ids_db():
    # Connect to the database
    connection = sqlite3.connect("user.db")  # Replace with your DB path
    cursor = connection.cursor()
    
    try:
        # Query to fetch all IDs from the all_id table
        cursor.execute("SELECT id FROM all_id")
        result = cursor.fetchall()
        
        # Extract the IDs into a list
        id_list = [row[0] for row in result]
        return [True, id_list]
    except Exception as e:
        print(f"Error: {e}")
        return [False, 0]
    finally:
        # Close the connection
        connection.close()


def unique_code(existing_codes, static_start):
    while True:
        # Generate a random 4-letter code
        random_part = ''.join(random.choices(string.ascii_uppercase, k=4))
        new_code = static_start + random_part
        
        # Check if the code is unique
        if new_code not in existing_codes:
            existing_codes.append(new_code)  # Add the new code to the list
            return new_code

def reg_def(type, user_id, name, dept, code):
    load = ids_db()
    if load[0]:
        idz = unique_code(load[1], type)

    else:
        return [False, "unknown error"]

@auth.route('/web/reg', methods=['GET', 'POST'])
def auth_reg():
    data = request.form.to_dict()
    print(unique_code([]))
    return jsonify(message="This is API endpoint 1"), 200


@auth.route('/log', methods=['GET'])
def auth_log():
    return jsonify(message="This is API endpoint 2"), 200
