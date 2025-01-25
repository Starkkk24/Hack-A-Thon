from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


import sqlite3

def create_database():
    # Connect to SQLite (it will create the database file if it doesn't exist)
    conn = sqlite3.connect('user.db')
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
    # Create table with user_id, user_name, dept, and code columns
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        user_name TEXT NOT NULL,
        dept TEXT NOT NULL,
        code TEXT NOT NULL
    );
    ''')
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database and table
create_database()



@auth.route('/reg', methods=['GET'])
def auth_reg():

    return jsonify(message="This is API endpoint 1"), 200


@auth.route('/log', methods=['GET'])
def auth_log():
    return jsonify(message="This is API endpoint 2"), 200
