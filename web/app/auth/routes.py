from flask import Blueprint, render_template

app1_bp = Blueprint('app1', __name__, template_folder='templates')

@app1_bp.route('/')
def index():
    return "dcfvgbhj"
