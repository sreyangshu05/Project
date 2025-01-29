from flask import Flask
from flask_pymongo import PyMongo
from app.routes import user_routes

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    mongo.init_app(app)
    app.register_blueprint(user_routes)

    return app
