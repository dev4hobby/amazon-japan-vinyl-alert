from urllib.parse import quote_plus
from pymongo import MongoClient
from settings import DATABASES

class Mongo():
    def __init__(self, user=None, password=None, host=None, port=None, collection=None):
        host = host and host or DATABASES.get('host')
        port = port and port or int(DATABASES.get('port'))
        collection = collection and collection or DATABASES.get('collection')
        user = user and user or DATABASES.get('user')
        password = password and qutoe_plus(password) or quote_plus(DATABASES.get('password'))

        print(f"mongodb+srv://{user}:{password}@{host}?retryWrites=true&w=majority")
        self.client = MongoClient(f"mongodb+srv://{user}:{password}@{host}?retryWrites=true&w=majority", int(port))
        self.db = self.client.get_database(collection)

    def get_vinyl_list(self):
        return list(self.db.featured.find({}))[:10]

    def upsert_vinyl(self, vinyl:dict):
        ret = self.db.featured.update_many({'title': {'$eq': vinyl.get('title')}}, {"$set": vinyl}, upsert=True)
        if ret.upserted_id:
            return True
        return False