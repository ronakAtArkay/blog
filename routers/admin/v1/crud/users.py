from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from libs.utils import date, genrate_id

from ..schemas import userBase


def create_user(db: Session, user: userBase):
    db_user = models.UserModel(
        id=genrate_id(),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        mobile_number=user.mobile_number,
        image=user.image,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    db_user = (
        db.query(models.UserModel)
        .filter(models.UserModel.is_deleted == False)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_user


def get_user(db: Session, user_number: str):
    db_user = (
        db.query(models.UserModel)
        .filter(
            models.UserModel.mobile_number == user_number,
            models.UserModel.is_deleted == False,
        )
        .first()
    )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def get_user_id(db: Session, id: str):
    db_user = (
        db.query(models.UserModel)
        .filter(
            models.UserModel.id == id, models.UserModel.is_deleted == False
        )
        .first()
    )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def update_user(db: Session, id: str, user_detail: userBase):
    db_user = (
        db.query(models.UserModel)
        .filter(models.UserModel.id == id, models.UserModel.is_deleted == False)
        .first()
    )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.first_name = user_detail.first_name
    db_user.last_name = user_detail.last_name
    db_user.email = user_detail.email
    db_user.password = user_detail.password
    db_user.mobile_number = user_detail.mobile_number
    db_user.updated_at = date()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, id: str):
    db_user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.is_deleted = True
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
