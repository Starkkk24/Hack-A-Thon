from flask import Flask
from api.auth import auth

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
# app.register_blueprint(blueprint2, url_prefix='/api/v2')

@app.route('/')
def main():
    return "empty"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
