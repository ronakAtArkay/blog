from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from routers.admin.v1.crud import blog, user_blog, users
from routers.admin.v1.schemas import blogBase, userBase, userBlogBase

router = APIRouter()

@router.post("/user", tags=["user"])
def create_user(user: userBase, db: Session = Depends(get_db)):
    user_create = users.create_user(user=user, db=db)
    return user_create


@router.post("/create_blog", tags=["blog"])
def create_blog(blogs : blogBase, db: Session = Depends(get_db)):
    blog_create = blog.create_blog(blogs=blogs, db=db)
    return blog_create


@router.get("/get_blog", tags=["blog"])
def get_detail(id: str, db: Session = Depends(get_db)):
    get_blog = blog.get_detail(id=id, db=db)
    return get_blog

@router.get("/get_blig_title", tags=["blog"])
def get_title(title : str, db: Session = Depends(get_db)):
    get_blog = blog.get_detail_title(title=title, db=db)
    return get_blog

@router.put("/update_blog", tags=["blog"])
def update_blog(id: str, blogs : blogBase, db: Session = Depends(get_db)):
    blog_update = blog.update_blog(id = id, blogs=blogs, db=db)
    return blog_update

@router.delete("/delete_blog", tags=["blog"])
def delete_blog(id: str, db: Session = Depends(get_db)):
    blog_deleted = blog.delete_blog(id=id, db=db)
    return blog_deleted



@router.post("/create_userblog", tags=["userBlog"])
def create_userblog(scheme : userBlogBase, users_id : str, db : Session = Depends(get_db)):
    userblog_create = user_blog.create_userblog(scheme= scheme, users_id= users_id, db=db)
    return userblog_create

@router.get("/get_userblog", tags=["userBlog"])
def get_userblog(id : str, db: Session = Depends(get_db)):
    userblog_detail = user_blog.get_userblog(id=id, db=db)
    return userblog_detail

@router.put("/updated_userblog", tags=["userBlog"])
def update_userblog(id:str,scheme : userBlogBase , db: Session = Depends(get_db)):
    userblog_update = user_blog.update_userblog(id=id,scheme=scheme, db=db)
    return userblog_update

@router.delete("/delete_userblog", tags=["userBlog"])
def delete_userblog(id:str, db : Session = Depends(get_db)):
    userblog_delete = user_blog.delete_userblog(id=id, db=db)
    return userblog_delete