from flask import jsonify  # Import jsonify to format output as JSON
from flask import Blueprint, jsonify, request
import sqlite3

man = Blueprint('man', __name__)


@man.route('/web/insert', methods=['POST'])
def auth_reg():
    data = request.form.to_dict()
    print(data)
    return "nothi"

def clear_table(db_path, table_name):
    import sqlite3

    # Connect to your SQLite database
    conn = sqlite3.connect('items_database.db')  # Update the database name
    cursor = conn.cursor()

    # Delete all data from the 'items' table
    cursor.execute("DELETE FROM items")

    # Commit the transaction to apply the deletion
    conn.commit()

    # Check the deletion (optional)
    cursor.execute("SELECT * FROM items")
    print(cursor.fetchall())  # Should return an empty list []

    # Close the connection to the database
    conn.close()



@man.route('/web/del')
def se():
    clear_table("items_database.db", "items")
    return ["output"]
   
    

@man.route('/web/get-site', methods=["POST"])
def site_man():
    
    data = request.form.to_dict()
# Connect to your database
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    # Define the dynamic value for 'under'
    dynamic_value = data["under"]  # Safely get the value of "under"
    

    # Query to fetch site manager ID and name
    query = "SELECT id, user_id, name FROM sub WHERE under = ?"

    # Execute the query
    cursor.execute(query, (dynamic_value,))

    # Fetch all results
    results = cursor.fetchall()

    # Close the connection
    conn.close()

    # Separate the data into lists for IDs and names
    ids = [row[0] for row in results]
    user_ids = [row[1] for row in results]
    names = [row[2] for row in results]

    # Return the response with grouped lists
    response = {
        "id": ids,
        "user_ids": user_ids,
        "names": names
    }

    return jsonify(response)




@man.route('/web/gt', methods=["POST"])
def list_pro():
    
    data = request.form.to_dict()
# Connect to your database
    conn = sqlite3.connect('items_database.db')
    cursor = conn.cursor()

    # Define the dynamic value for 'under'
    dynamic_value = data["id"]  # Safely get the value of "under"
    print(dynamic_value)

    # Query to fetch site manager ID and name
    query = "SELECT id, name, date, status FROM items WHERE under = ?"

    # Execute the query
    cursor.execute(query, (dynamic_value,))

    # Fetch all results
    results = cursor.fetchall()
    print(results)
    # Close the connection
    conn.close()

    # Separate the data into lists for IDs and names
    ids = [row[0] for row in results]
    name = [row[1] for row in results]
    date = [row[2] for row in results]
    status = [row[3] for row in results]

    # Return the response with grouped lists
    response = {
        "id": ids,
        "name": name,
        "date": date,
        "stu": status
    }

    return jsonify(response)


