 #import FastAPI
from  fastapi import FastAPI

#create an instance
app = FastAPI()

#decorate
@app.get('/')

#function
def index():
    return {'data':'Blog List'}

#decorate
@app.get('/{id}')

#function
def ShowId(id:int):
    #fetch the id with id =id
    return {'data':id}

#decorate
@app.get('/blog/{id}/comments')
#function
def Comments(id:int):
    #fetch comments of blog with id = id
    return {'data':id}

#decorate
@app.get('/about')

#function
def about():
    return {'data':'SAnjay'}
