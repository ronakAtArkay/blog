from pydantic import BaseModel

class blogBase(BaseModel):
    title : str
    description : str

    class Config:
        orm_mode = True
