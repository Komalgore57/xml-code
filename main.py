from read import *
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(employID: int=0 ,company : str='cvc'):
    result=process(company,employID)
    
    return {'body':result}