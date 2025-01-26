from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
import requests
import sqlite3
import json

app4_bp = Blueprint('app4', __name__, template_folder='templates', static_folder="static")
url = "http://127.0.0.1:5500/auth/web"


@app4_bp.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    
    return render_template("listing.html")


@app4_bp.route('/pro')
def pro():
    if 'user' not in session:
        return redirect(url_for("app1.reg"))
    
    return render_template("pro.html")
