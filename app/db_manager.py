from data_interactor import MongoDB
from bson import ObjectId
import os

MONGO_DB = os.getenv('MONGO_DB','contactdb')

class MongoDBManagerContacs:
    def __init__(self):
        self.mongo_client = MongoDB()
        self.mongo_client.create_database(MONGO_DB)
        self.mongo_client.create_collection(MONGO_DB,"contacts")
        self.contacts_collection = self.mongo_client.get_collection(MONGO_DB,"contacts")


    def insert_contact(self,contact_data:dict):
        resulte = self.contacts_collection.insert_one(contact_data)
        return resulte.inserted_id
    
    
    def delete_contact(self,contact_id:ObjectId):
        resulte = self.contacts_collection.delete_one({"_id":contact_id})
        if resulte.deleted_count == 0:
            return False
        else:
            return True
        

    def update_contact(self,contact_id : ObjectId, contact_data:dict):
        resulte = self.contacts_collection.update_one({"_id":contact_id},{'$set':contact_data})
        if resulte.modified_count == 0:
            return False
        else:
            return True
        

    def get_all_contacts(self):
        cursor = self.contacts_collection.find({})
        lst = []
        for doc in cursor:
            doc['_id'] = str(doc['_id'])
            lst.append(doc)
        return lst
        