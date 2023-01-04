import os
from pymongo import MongoClient

def get_database_client():
    CONNECTION_STRING = os.environ['MONGODB_CONNSTRING']
    # CONNECTION_STRING = 'mongodb://root:example@localhost:27017/?authMechanism=DEFAULT' # to be used locally without docker
    client = MongoClient(CONNECTION_STRING)
    return client