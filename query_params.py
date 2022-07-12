from lib2to3.pgen2.token import OP
from typing import Optional
from fastapi import FastAPI


app= FastAPI()

@app.get('/')
def showId():
    return{'Hello'}
#doubt
@app.get('/blog')
def index(pub:bool=True,limit:int=90,sort:Optional[str]=None):
    #only get published blogs

    if pub:
        return{'data':f'no of published blogs {limit}'}
    else:
        return{'data':'no published blogs'}
        
@app.get('/blog/{id}/comments')
def index(id,limit=None):
    return {f'id={id}',f'limit ={limit}'}