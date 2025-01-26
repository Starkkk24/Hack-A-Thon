from flask import Blueprint, jsonify, request
import sqlite3
from datetime import datetime
import random
import json
import string

sell = Blueprint('sell', __name__)

def ids_db():
    # Connect to the database
    connection = sqlite3.connect("items_database.db")  # Replace with your DB path
    cursor = connection.cursor()
    
    try:
        # Query to fetch both id and user_id from the all_id table
        cursor.execute("SELECT id, under FROM items")
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



def lun(data):
# Get the current time

    current_date = str(datetime.now().date())

    try:
        print("hy")
        # Connect to the database
        conn = sqlite3.connect("items_database.db")
        cursor = conn.cursor()

        # SQL insert query
        query = """
        INSERT INTO items (id, name, weight, price, des, date, status, under)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        # data['grid'],
            # data['can'],
            # data['cant'],

        # Execute the query
        cursor.execute(query, (
            data['id'],
            data['name'],
            data['weight'],
            data['price'],
            
            data['des'],
            current_date,
            "pending",
            data['under']
        ))

        # Commit the transaction and close the connection
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


@sell.route('/web/add', methods=["POST"])
def add():
    if request.method == 'POST':
        data = request.form.to_dict()
        l = ids_db()
        if not l:
            return [False, 110]
        
        g = unique_code(l[1], "D")
        data = {
        'id': g,
        'name': data["name"],
        'weight': data["weight"],
        'price': data["price"],
        'des': data["des"],
        'under': data["under"]
    }
        if lun(data):
            return [True, 500]
        else:
            return [False, 500]
    return "nothi"

 