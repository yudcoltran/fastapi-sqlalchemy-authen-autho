
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from . import token

router = APIRouter(
    tags=["Authen"]
)

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify(plain, hashed):
    return pwd_cxt.verify(plain, hashed)

@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'User not exist')
    if not verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Wrong password')
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}