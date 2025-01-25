from flask import Blueprint, render_template

app1_bp = Blueprint('app1', __name__, template_folder='templates', static_folder="static")

@app1_bp.route('/')
def index():
    return "dcfvgbhj"


@app1_bp.route('/reg')
def reg():
    return render_template("reg.html")

@app1_bp.route('/log')
def log():
    return render_template("log.html")