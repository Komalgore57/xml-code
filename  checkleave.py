from typing import Union

from fastapi import FastAPI

app = FastAPI()

import sqlite3




@app.get("/")
def read_root(id: int=0 ):
    if id==0:
        return {'id':0}
    id=1
    # conn = sqlite3.connect('test.db')
    # cursor = conn.execute(f"SELECT leave from COMPANY WHERE ID=1 ;")
    print(1)
    # try:
        
    #     for i in cursor:
            
    #         print(int(i[0]))  
    #         return {'leave': i[0] }
            # if(i[0]):
            #     return {"Hello": "World"}
    # except:
    #     return {"ERROR":"TRUE"}
    return {'hello' : 'world'}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}