from fastapi import FastAPI, HTTPException, status
from schemas_api import Contact
import uvicorn
from db_manager import MongoDBManagerContacs
from bson import ObjectId





app = FastAPI()
db = MongoDBManagerContacs()

@app.get('/contacts')
def get_all_contacts():
    try:
        contacts =  db.get_all_contacts()
        if not contacts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"There is no contacts")
        return contacts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")


@app.post('/contacts')
def create_contact(contact:Contact):
    try:
        contact_py = contact.model_dump()
        new_id = db.insert_contact(contact_py)
        return {'message':"Contact created successfully",
                'id':str(new_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not create contact: {str(e)}")

@app.put('/contacts/{id_contact}')
def update_contact(id_contact:str, new_info:Contact):
    contact = new_info.model_dump()
    if db.update_contact(ObjectId(id_contact), contact):
        return {"status": "update"}
    else:
        return {"status":"error"}    


@app.delete('/contacts/{id_contact}')
def delete_contact(id_contact:str):
    if db.delete_contact(ObjectId(id_contact)):
        return {"status": "deleted"}
    else:
        return {"status":"error"}    
    
if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
