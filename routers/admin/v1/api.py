from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from routers.admin.v1.schemas import blogBase
from routers.admin.v1.crud import blog


router = APIRouter()

@router.post("/create_blog")
def create_blog(blogs : blogBase, db: Session = Depends(get_db)):
    blog_create = blog.create_blog(blogs=blogs, db=db)
    return blog_create


@router.get("/get_blog")
def get_detail(id: str, db: Session = Depends(get_db)):
    get_blog = blog.get_detail(id=id, db=db)
    return get_blog

@router.get("/get_blig_title")
def get_title(title : str, db: Session = Depends(get_db)):
    get_blog = blog.get_detail_title(title=title, db=db)
    return get_blog

@router.put("/update_blog")
def update_blog(id: str, blogs : blogBase, db: Session = Depends(get_db)):
    blog_update = blog.update_blog(id = id, blogs=blogs, db=db)
    return blog_update

@router.delete("/delete_blog")
def delete_blog(id: str, db: Session = Depends(get_db)):
    blog_deleted = blog.delete_blog(id=id, db=db)
    return blog_deleted