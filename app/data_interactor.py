from pymongo import MongoClient
import os

# Details connection
MONGO_HOST = os.getenv('MONGO_HOST','localhost')
MONGO_PORT = os.getenv('MONGO_PORT','27017')

class MongoDB:
    def __init__(self):
        self.client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
    
    def create_database(self,database_name:str):
        self.client[database_name]

    def create_collection(self,database:str,collection_name:str):
        self.client[database][collection_name]

    def get_collection(self,database : str, collection_name:str):
        return self.client[database].get_collection(collection_name)


