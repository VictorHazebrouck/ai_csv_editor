from flask import Flask
from app.public.views import public
from app.public.views import index
from app.api.routes import main

def create_app():
    app = Flask(__name__)

    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(public, url_prefix='/public')
    app.register_blueprint(main, url_prefix='/api')

    return app