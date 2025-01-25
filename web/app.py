from flask import Flask, render_template
# from blueprint1 import blueprint1
# from blueprint2 import blueprint2

app = Flask(__name__)

# Register blueprints
# app.register_blueprint(blueprint1, url_prefix='/blueprint1')
# app.register_blueprint(blueprint2, url_prefix='/blueprint2')

@app.route('/')
def home():
    return render_template("reg.html")

if __name__ == '__main__':
    app.run(debug=True)
