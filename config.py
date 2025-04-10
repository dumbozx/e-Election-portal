import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key-change-this' # IMPORTANT: Use environment variable
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///election.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False