from flask import Flask

def create_app():
    app = Flask(__name__)
    from .router import router

    app.register_blueprint(router,url_prefix='/api/v1')

    return app