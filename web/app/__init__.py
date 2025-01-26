from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    # Register blueprints
    from app.auth.routes import app1_bp
    from app.man.routes import app2_bp
    from app.sell.route import app3_bp
    from app.buy.routes import app4_bp
    # from app.app2.routes import app2_bp

    @app.route('/')
    def main1():
        return redirect(url_for('app1.reg'))
    

    app.register_blueprint(app1_bp, url_prefix='/app1') # auth
    app.register_blueprint(app2_bp, url_prefix='/app2') # man
    app.register_blueprint(app3_bp, url_prefix='/app3') # sell
    app.register_blueprint(app4_bp, url_prefix='/app4') # sell
    #cSapp.register_blueprint(app4_bp, url_prefix='/app4')

    return app
