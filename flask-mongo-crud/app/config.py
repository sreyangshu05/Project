# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    MONGO_URI = os.getenv('MONGO_URI')
