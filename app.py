from typing import Callable
from flask import Flask, jsonify
app = Flask(__name__)
from pymongo import MongoClient
from bson.json_util import dumps
MONGODB_URL="mongodb://localhost:27017/"
MONGODB_URL="mongodb://adminuser:password123@192.168.49.2:32258/?retryWrites=true&w=majority" # local

MONGODB_URL="mongodb://adminuser:password123@mongo-nodeport-svc.myapp.svc.cluster.local/?retryWrites=true&w=majority" #prod
import os
class DB:
    def __init__(self,client):
        db = client['test-database']
        self.collection = db.test_collection
    def find(self):
        return self.collection.find()
class FakeDB:
    def __init__(self,client):
        pass
    def find(self):
        return []

def db_production():
    return DB(client=MongoClient(MONGODB_URL))
def db_staging():
    return DB(client=MongoClient(MONGODB_URL))
def db_testing():
    return FakeDB(client=None)


def get_db(config_function: str):
    configs = {"testing":db_testing,"staging":db_staging,"production":db_production}
    return configs[config_function]()

@app.route('/')
def hello():
    documents=get_db("staging").find()
    return jsonify({"version":"v2","data":(list(documents))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
