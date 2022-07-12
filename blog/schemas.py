from pydantic import BaseModel


class Blog(BaseModel):
    id:str
    title:str
    body:str

