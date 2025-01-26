from flask import Flask
from api.auth import auth
from api.man import man
from api.sell import sell

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(man, url_prefix='/man')
app.register_blueprint(sell, url_prefix='/sell')

@app.route('/')
def main():
    return "empty"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
