from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

from dependencies import get_db
from routers.admin.v1.crud import blog, user_blog, users
from routers.admin.v1.schemas import blogBase, userBase, userBlogBase

router = APIRouter()

# start user

@router.post("/user", tags=["user"])
def create_user(user: userBase, db: Session = Depends(get_db)):
    user_create = users.create_user(user=user, db=db)
    return user_create

# end user

# start blog

@router.post("/blog", tags=["blog"])
def create_blog(blogs: blogBase, db: Session = Depends(get_db)):
    blog_create = blog.create_blog(blogs=blogs, db=db)
    return blog_create


@router.get("/blog/{id}", tags=["blog"])
def get_detail(id: str = Path(min_length=36, max_length=36), db: Session = Depends(get_db)):
    get_blog = blog.get_detail(id=id, db=db)
    return get_blog


@router.put("/blog/{id}", tags=["blog"])
def update_blog(blogs: blogBase,id: str= Path(min_length=36, max_length=36), db: Session = Depends(get_db)):
    blog_update = blog.update_blog(id=id, blogs=blogs, db=db)
    return blog_update


@router.delete("/blog/{id}", tags=["blog"])
def delete_blog(id: str= Path(min_length=36, max_length=36), db: Session = Depends(get_db)):
    blog_deleted = blog.delete_blog(id=id, db=db)
    return blog_deleted

# end blog

# start userBlog

@router.post("/userblog", tags=["userBlog"])
def create_userblog(scheme: userBlogBase, users_id: str, db: Session = Depends(get_db)):
    userblog_create = user_blog.create_userblog(scheme=scheme, users_id=users_id, db=db)
    return userblog_create


@router.get("/userblog/{id}", tags=["userBlog"])
def get_userblog(id: str= Path(min_length=36, max_length=36), db: Session = Depends(get_db)):
    userblog_detail = user_blog.get_userblog(id=id, db=db)
    return userblog_detail


@router.put("/userblog/{id}", tags=["userBlog"])
def update_userblog(scheme: userBlogBase,id: str= Path(min_length=36, max_length=36), db: Session = Depends(get_db)):
    userblog_update = user_blog.update_userblog(id=id, scheme=scheme, db=db)
    return userblog_update


@router.delete("/userblog/{id}", tags=["userBlog"])
def delete_userblog(id: str= Path(min_length=36, max_length=36), db: Session = Depends(get_db)):
    userblog_delete = user_blog.delete_userblog(id=id, db=db)
    return userblog_delete

# end userblog