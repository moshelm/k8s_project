from pydantic import BaseModel
from typing import Optional

class Contact(BaseModel):
    first_name:Optional[str]
    last_name:Optional[str]
    phone_number:Optional[str]