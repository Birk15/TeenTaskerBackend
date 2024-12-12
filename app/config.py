import os
from dotenv import load_dotenv
from pymongo import MongoClient

# env Datei laden
load_dotenv()

class Config():
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'mySecretKey')
    DB_URI = os.getenv('DB_URI')

client = MongoClient(Config.DB_URI, serverSelectionTimeoutMS=10000)
db = client["TeenTasker"]

# optional - gibt collcetions zurück
def get_collection(name):
    return db[name]