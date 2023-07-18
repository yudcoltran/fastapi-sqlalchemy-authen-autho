from fastapi import APIRouter, Depends
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import user
from . import oauth2
router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/")
async def create_user(request: schemas.User, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return user.create(request, db)

@router.get("/{id}")
async def show_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)