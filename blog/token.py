from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from . import schemas

SECRET_KEY = "8ed267d0620ab4e84ab101ada4f7e5b5720d78f8c104c568716e3f5916ccaca2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict ):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp":expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def verify_token(token:str, credentials_exception):
   try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
   except JWTError:
        raise credentials_exception