from data_interactor import MongoDB
from bson import ObjectId
import os

MONGO_DB = os.getenv('MONGO_DB','contactdb')

class MongoDBManagerContacs:
    def __init__(self):
        self.mongo_server = MongoDB()
        self.mongo_server.create_database(MONGO_DB)
        self.mongo_server.create_collection("contacs")
        self.contacs_collection = self.mongo_server.get_collection("contacs")
    def insert_documents(self,documente:dict):
        self.contacs_collection.insert_one(documente)
    def delete_document(self,document:dict):
        self.contacs_collection.delete_one(document)
    def update_document(self,document:dict):
        self.contacs_collection.update_one(document)
    def get_all_documents(self):
        self.contacs_collection.find_one_and_delete({"_id": ObjectId("507f1f77bcf86cd799439011")})



# class Database:
#     def __init__(self,database_name:str = None, file_name :str = None):
        
#         if database_name is None and file_name is None:
#             raise ValueError("we need name or file name for database")


#         if database_name:
#             # create or use in database
#             self.name = database_name
#             self._create_database()
#         else:
#             # initialize new one
#             self._initialize_schema(file_name)

#     def _initialize_schema(self,file_name:str):

#         with open(file_name, 'r') as file:
#             # split by command
#             commends_sql = file.read().split(';')
#             for commend in commends_sql:
#                 # ignore comments
#                 if commend.strip():
#                     self.cursor.execute(commend)
#                     self.conn.commit()
#             self.cursor.execute("SELECT DATABASE();")
#             # name of database
#             name = self.cursor.fetchone()[0]
#             self.name = name
#             self.conn.database = self.name

#     def _create_database(self):
#         sql = f"CREATE DATABASE IF NOT EXISTS `{self.name}`;"
#         self.cursor.execute(sql)
#         # defulte database
#         self.conn.database = self.name


#     def create_table(self, table_name:str, fields:tuple[str]):
#         fields = ','.join(fields)
#         if not fields:
#             raise ValueError
#         sql = f"""
#         CREATE TABLE IF NOT EXISTS `{table_name}` (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         {fields});"""

#         self.cursor.execute(sql)

#     def create_contact(self,table_name:str, new_contact:dict):
#         fields = ','.join(list(new_contact.keys()))
#         values = tuple(new_contact.values())
#         flags = ','.join(['%s' for _ in range(len(list(new_contact.keys())))])
     
#         sql = f"""
#                INSERT INTO `{table_name}` ({fields})
#                VALUES ({flags});"""
       
#         self.cursor.execute(sql,values)
#         # get new contact id
#         new_id = self.cursor.lastrowid
#         self.conn.commit()
#         return new_id

#     def get_all(self,table_name:str):
#         sql = f"SELECT * FROM `{table_name}`;"
#         self.cursor.execute(sql)
#         result = [row for row in self.cursor]
#         if result:
#             return result
#         else:
#             return None

#     def update_record(self,table_name:str,record_id:int, update_info:dict):
#         updates = []
#         for field in list(update_info.keys()):
#             updates.append(f"{field} = %s")

#         sql = f"""UPDATE  `{table_name}` SET {','.join(updates)} WHERE id = %s;"""
#         lst_update_info = list(update_info.values())
#         lst_update_info.append(record_id)
#         values = tuple(lst_update_info)

#         self.cursor.execute(sql,values)
#         self.conn.commit()
#         # check if update
#         if self.cursor.rowcount != 0:
#             return True
#         else:
#             return False

#     def delete_record(self,table_name:str, record_id:int):
#         sql = f"DELETE FROM {table_name} WHERE id = %s"
#         value = (record_id,)

#         self.cursor.execute(sql,value)
#         self.conn.commit()

#         # check if delete
#         if self.cursor.rowcount != 0:
#             return True
#         else:
#             return False





