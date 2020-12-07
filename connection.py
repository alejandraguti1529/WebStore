from pymongo import MongoClient


def get_db():
    host = "localhost"
    db = "webstore"   
    client = MongoClient(host)
    return  client[db]
