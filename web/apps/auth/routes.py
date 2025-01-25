from . import blueprint1
from flask import render_template

@blueprint1.route('/')
def index():
    return render_template('templates/reg.html', title="Blueprint 1")
