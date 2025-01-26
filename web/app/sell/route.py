from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
import requests
import sqlite3
import json
import random
import string


app3_bp = Blueprint('app3', __name__, template_folder='templates', static_folder="static")
url = "http://127.0.0.1:5500/auth/web"


@app3_bp.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    
    return render_template("home.html")



@app3_bp.route('/add-pro')
def add():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    if request.method == 'POST':
        user = request.form.get('n')       # Field name: u
        code = request.form.get('c')
    return render_template("add1.html")
