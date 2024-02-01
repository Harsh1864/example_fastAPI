from jose import  JWTError,jwt
from datetime import datetime,timedelta
from . import schema,database,models
from fastapi import Depends,status,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

def create_access_token(data : dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_HOURS)

    to_encode.update({"exp" : expire})

    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encode_jwt

def verify_access_token(token : str,credential_expresion):
    try:
     payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
     print(payload)
     id : str = payload.get("user.id")
     print(type(id))
     if id is None:
        raise credential_expresion
     token_data = schema.TokenData(id=str(id))
     print(token_data)
    except JWTError:
     raise credential_expresion
    
    return token_data

def get_current_user(token:str = Depends(oauth_scheme),db :Session = Depends(database.get_db)):
   credential_expresion = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",
                                        headers={"WWW-Authentication":"Bearer"})
   token = verify_access_token(token,credential_expresion)

   user = db.query(models.User).filter(models.User.id == token.id).first()
   
   return user

