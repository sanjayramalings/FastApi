from fastapi import FastAPI

app=FastAPI()

@app.get('/{id}')
def ShowId(id:int):
    #fetch the id with id =id
    return {'data':id}


@app.get('/blog/unpublished')
def ShowUnpub():
    #fetch comments of blog with id = id
    return {'data':'None'}

@app.get('/blog/{id}')
def Comments(id:int):
    #fetch comments of blog with id = id
    return {'data':id}

