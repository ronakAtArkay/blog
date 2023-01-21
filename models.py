from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(200), primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    email = Column(String(200))
    password = Column(String(200))
    mobile_number = Column(String(200))
    image = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    is_deleted = Column(Boolean, default=False)


class BlogModel(Base):
    __tablename__ = "blogs"

    id = Column(String(200), primary_key=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(String(200), nullable=True, default=None)
    image = Column(String(200), default="uploads/default.png")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    is_deleted = Column(Boolean, default=False)


class UserBlogModel(Base):
    __tablename__ = "user_blogs"

    id = Column(String(200), primary_key=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(String(200), nullable=True, default=None)
    image = Column(String(200), default="uploads/default.png")
    user_id = Column(String(200), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    is_deleted = Column(Boolean, default=False)

    user = relationship("UserModel", backref="user_blogs")
