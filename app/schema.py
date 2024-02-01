from typing import Optional
from pydantic import BaseModel,EmailStr, conint
from datetime import datetime
from pydantic import BaseModel, PydanticUserError


class PostBase(BaseModel):
    title : str
    contant : str
    published : bool = True
    

class postcreate(PostBase):
    pass

class postupdate(PostBase):
    pass

class userout(BaseModel):
    id : int
    email : EmailStr

    class Config:
        from_attributes = True

class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : userout

    
    class Config:
        from_attributes = True

class Postout(BaseModel):
    Post : Post
    votes: int

    class Config:
        from_attributes = True

class usercreate(BaseModel):
    email : EmailStr
    password : str
    phone_NO : str


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type  : str

class TokenData(BaseModel):
     id : Optional[str] =None

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1)