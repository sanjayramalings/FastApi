#import FastAPI
from  fastapi import FastAPI

#create an instance
app = FastAPI()

#decorate
@app.get('/')

#function
def index():
    return {'data':{'name':'hello'}}
#decorate
@app.get('/about')

#function
def about():
    return {'data':'SAnjay'}
