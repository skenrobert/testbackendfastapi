from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union
from sqlalchemy.orm import Session
from db.models import user
from db.database import Base, engine
from db.database import get_db

import hubspot
from pprint import pprint
from hubspot.crm.contacts import PublicGdprDeleteInput, ApiException


router = APIRouter(prefix="/users",# prefix this page
                   tags=["users"],# for swagger documentation 
                   responses={404: {"message":"no found"}})# overrall error 404 


class User(BaseModel):
    id: int
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str


# {
# "email": "test@orbidi.com",
# "firstname": "Test",
# "lastname": "Orbidi",
# "phone": "(322) 123-4567",
# "website": "orbidi.com"
# }


# Starting November 30, 2022, API keys will be sunset as an authentication method. Learn more about this change: https://developers.hubspot.com/changelog/upcoming-api-key-sunset and how to migrate an API key integration: https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app to use a private app instead.

# client = hubspot.Client.create(access_token="pat-na1-bfa3f0c0-426b-4f0e-b514-89b20832c96a")

# public_gdpr_delete_input = PublicGdprDeleteInput(object_id="string", id_property="string")
# try:
#     api_response = client.crm.contacts.gdpr_api.purge(public_gdpr_delete_input=public_gdpr_delete_input)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling gdpr_api->purge: %s\n" % e)

    
users_list = [User(id=1,email="robert", firstname="middle name and lastname", lastname="middle name and lastname",phone ="44444444",
                    website="www.test.com"),
              User(id=2,email="kenny", firstname="middle name and lastname", lastname="middle name and lastname",phone ="44444444",
                    website="www.test.com")]



@router.get("/",  response_model=list[User], status_code=200)
async def users():
    try:
        return users_list
    except:
        raise HTTPException(status_code=404, detail="users no found")
        
        
@router.get("/", response_model=User, status_code=200)
async def show_userquery(id: int):
    return search_user(id)
   
   
@router.post("/", response_model=User, status_code=201)
async def store(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="user already exists")
    
    users_list.routerend(user)
    return user
       

  
def search_user(id: int):
    #search in users_list
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "user no found"
        



