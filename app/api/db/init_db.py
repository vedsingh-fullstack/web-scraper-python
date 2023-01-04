import os
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = os.environ['MONGODB_CONNSTRING']
    # CONNECTION_STRING = 'mongodb://root:example@localhost:27017/?authMechanism=DEFAULT'
    client = MongoClient(CONNECTION_STRING)
    db = client["dnl_db"]

    return db