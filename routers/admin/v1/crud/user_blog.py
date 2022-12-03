from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
from libs.utils import date, genrate_id
from ..schemas import userBlogBase


def create_userblog(db: Session, users_id: str, scheme = userBlogBase):
    db_userblog = models.UserBlogModel(id = genrate_id(), title = scheme.title, description = scheme.description, user_id = users_id)
    db.add(db_userblog)
    db.commit()
    db.refresh(db_userblog)
    return db_userblog

def get_userblog(db: Session, id : str):
    db_userblog = db.query(models.UserBlogModel).filter(models.UserBlogModel.id == id, models.UserBlogModel.is_deleted == False).first()
    if db_userblog is None:
        raise HTTPException(status_code=404, detail="detail not found")
    return db_userblog

def update_userblog(db: Session, id: str, scheme = userBlogBase):
    db_userblog = db.query(models.UserBlogModel).filter(models.UserBlogModel.id == id, models.UserBlogModel.is_deleted == False).first()
    if db_userblog is None:
        raise HTTPException(status_code=404, detail="detail not faound")
    db_userblog.title = scheme.title
    db_userblog.description = scheme.description
    db_userblog.updated_at = date()
    db.add(db_userblog)
    db.commit()
    db.refresh(db_userblog)
    return db_userblog


def delete_userblog(db : Session, id : str):
    db_userblog = db.query(models.UserBlogModel).filter(models.UserBlogModel.id == id, models.UserBlogModel.is_deleted == False).first()
    if db_userblog is None:
        raise HTTPException(status_code=404, detail="detail not found")
    db_userblog.is_deleted = True
    db_userblog.updated_at = date()
    db.add(db_userblog)
    db.commit()
    db.refresh(db_userblog)
    return "Data are deleted successfully"