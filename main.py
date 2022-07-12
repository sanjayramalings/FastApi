import re
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app=FastAPI()

#creating a new class instace with Employee Table and imporint Basemodel from Pydantic
class EmployeeTable(BaseModel):
    title:str
    name:str
    join_date:str
    current_working_status:Optional[bool]
 
@app.post('/Id')
#req is the request body it takes the Employee Scheamclass 
def Createemployee(req:EmployeeTable):
    return{'data':f'New employee create with Title:{req.title},Name :{req.name},joined at :{req.join_date}'}


#if __name__=="__main__":
#    uvicorn.run(app,host="127.0.0.1",port='9000')