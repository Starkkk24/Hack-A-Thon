from flask import Blueprint, jsonify, request
import sqlite3

man = Blueprint('man', __name__)


@man.route('/web/insert', methods=['POST'])
def auth_reg():
    data = request.form.to_dict()
    print(data)
    return "nothi"

 