from .. import models , schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create(request: schemas.User, db: Session):
    hashPassword = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashPassword) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'msg': 'Response', 'code': 1, 'data': new_user}

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'User {id} not found')
    return {'msg': 'Response', 'code': 1, 'data': user}