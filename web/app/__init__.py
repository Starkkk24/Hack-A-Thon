from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    # Register blueprints
    from app.auth.routes import app1_bp
    # from app.app2.routes import app2_bp

    app.register_blueprint(app1_bp, url_prefix='/app1')
    # app.register_blueprint(app2_bp, url_prefix='/app2')

    return app
