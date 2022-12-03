import models
from routers.admin.v1.schemas import blogBase
from sqlalchemy.orm import Session
from libs.utils import genrate_id, date
from fastapi import HTTPException

def create_blog(db: Session, blogs : blogBase):
    db_blog = models.BlogModel(id = genrate_id(), title = blogs.title, description = blogs.description)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_detail(db: Session, id:str):
    db_blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if db_blog:
        return db_blog
    raise HTTPException(status_code=404, detail="detail not found")

def get_detail_title(db: Session, title: str):
    db_blog = db.query(models.BlogModel).filter(models.BlogModel.title == title).first()
    if db_blog:
        return db_blog
    raise HTTPException(status_code=404, detail="detail not found")

def update_blog(db: Session,id: str, blogs : blogBase):
    db_blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if db_blog:
        db_blog.title = blogs.title
        db_blog.description = blogs.description
        db_blog.updated_at = date()
        db.add(db_blog)
        db.commit()
        db.refresh(db_blog)
        return db_blog
    raise HTTPException(status_code=404, detail="detail not found")

def delete_blog(db: Session, id : str):
    db_blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    if db_blog:
        db_blog.is_deleted = True
        db.add(db_blog)
        db.commit()
        db.refresh(db_blog)
        return "data are deleted successfully"

    raise HTTPException(status_code=404, detail="detail not found")