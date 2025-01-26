from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
import requests
import sqlite3
import json

app2_bp = Blueprint('app2', __name__, template_folder='templates', static_folder="static")
url = "http://127.0.0.1:5500/auth/web"


@app2_bp.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    
    return render_template("index.html")

@app2_bp.route('/site')
def site():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    
    return render_template("site.html")

@app2_bp.route('/add', methods=["GET", "POST"])
def add():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    if request.method == 'POST':

        url1 = url + "/reg"
        
        name = request.form.get('nm')       # Field name: u
        code = request.form.get('code')     # Field name: n

        data = {
                "name": name,
                "code": code,
                "dept": "site",
                "under": session["user"][0]

            }   
        print(data)
        response = requests.post(url1, data=data)
        ma = response.text
        res = json.loads(ma)
        return render_template("view.html", data=res)
        # return redirect(url_for("app2.index"))
        

    return render_template("add.html")