from fastapi import FastAPI, HTTPException, Response,status,Depends,APIRouter
from .. import models,schema,utils
from ..database import get_db,engine
from sqlalchemy.orm import Session,declarative_base 

router = APIRouter()

#for user 
@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schema.userout)
def create_user(user : schema.usercreate,db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{id}",response_model=schema.userout)
def get_user(id : int , db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id).first()
    print(user_query)
    if not user_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"id is not exixts {id}")
    return user_query