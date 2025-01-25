from flask import Flask, render_template
from web.apps.auth import blueprint1

# Set the template folder path
app = Flask(__name__, template_folder='web/templates')

# Register blueprints
app.register_blueprint(blueprint1, url_prefix='/auth')

@app.route('/')
def home():
    return render_template("home.html")  # This will now find the template

if __name__ == '__main__':
    app.run(debug=True)
