from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
import requests
import sqlite3
import json
import random
import string


app3_bp = Blueprint('app3', __name__, template_folder='templates', static_folder="static")
url = "http://127.0.0.1:5500/sell/web"


@app3_bp.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    
    return render_template("home.html")



@app3_bp.route('/add-pro', methods=["GET", "POST"])
def add():
    url1 = url + "/add"
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    if request.method == 'POST':
        name = request.form.get('1')       # Field name: u
        wei = request.form.get('2')
        price = request.form.get('3')
        desp = request.form.get('4')
        data = {
        
        'name': name,
        'weight': wei,
        'price': price,
        'des': desp,
        'under': session["user"][0]
    }
        response = requests.post(url1, data=data)
        if response.text[0]:
            return render_template("home.html")
        else:
            return render_template("app1.html")

    return render_template("add1.html")
