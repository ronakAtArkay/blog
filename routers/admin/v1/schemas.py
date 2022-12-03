from pydantic import BaseModel, EmailStr, Field


class userBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    mobile_number: str = Field(min_length=10, max_length=10)
    image: str

    class Config:
        orm_mode = True



class blogBase(BaseModel):
    title : str
    description : str

    class Config:
        orm_mode = True


class userBlogBase(BaseModel):
    title : str
    description : str

    class Config:
        orm_mode = True
