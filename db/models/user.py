from pydantic import BaseModel
from typing import Optional
from db.database import Base
from sqlalchemy import Column,Integer,String , Boolean,DateTime 
from datetime import datetime 
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel):
    id: int
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str