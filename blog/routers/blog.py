from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import blog
from . import oauth2

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get("/", status_code=200)
async def get_all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.craete(request, db)

@router.get("/{blog_id}", status_code=200)
async def get_a_blog(blog_id, db: Session = Depends(database.get_db)):
    return blog.show(blog_id, db)

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_blog(blog_id, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.destroy(blog_id, db)

@router.put("/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
async def update(blog_id, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(blog_id, request, db)