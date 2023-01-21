from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from libs.utils import date, genrate_id
from routers.admin.v1.schemas import blogBase


def create_blog(db: Session, blogs: blogBase):
    db_blog = models.BlogModel(
        id=genrate_id(), title=blogs.title, description=blogs.description
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_blog_by_id(db: Session, id: str):
    return db.query(models.BlogModel).filter(models.BlogModel.id == id, models.BlogModel.is_deleted == False).first()

def get_detail(db: Session, id: str):
    db_blog = get_blog_by_id(db=db, id=id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="detail not found")
    return db_blog


def update_blog(db: Session, id: str, blogs: blogBase):
    db_blog = get_blog_by_id(db=db, id=id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="detail not found")
    db_blog.title = blogs.title
    db_blog.description = blogs.description
    db_blog.updated_at = date()
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def delete_blog(db: Session, id: str):
    db_blog = get_blog_by_id(db=db, id=id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="detail not found")
    db_blog.is_deleted = True
    db_blog.updated_at = date()
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return "data are deleted successfully"
