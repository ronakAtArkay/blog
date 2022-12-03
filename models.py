from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from database import Base


class BlogModel(Base):
    __tablename__ = "blogs"

    id = Column(String(200), primary_key = True, nullable = False)
    title = Column(String(200), nullable = False)
    description = Column(String(200), nullable = True, default = None)
    image = Column(String(200), default = "uploads/default.png")
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
    is_deleted = Column(Boolean, default = False)

