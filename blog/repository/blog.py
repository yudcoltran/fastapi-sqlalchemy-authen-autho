from .. import models , schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def show(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Item {blog_id} not found')
    return {'msg': 'Response', 'code': 1, 'data': blog}


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {'msg': 'Response', 'code': 1, 'data': new_blog}

def destroy(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Item {blog_id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'msg': 'Response', 'code': 1}

def update(blog_id: int, request: schemas.Blog, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Item {blog_id} not found')
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return {'msg': 'Response', 'code': 1, 'data': request}

