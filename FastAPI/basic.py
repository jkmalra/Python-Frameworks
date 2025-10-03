from email import message

from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Jaskaran": "Singh"}

@app.get("/name")
def name():
    return {"name": "jakirat singh"}

@app.post("/name")
def postname():
    return {"name": "jaskaran singh"}

@app.get("/message")
def getmessage():
    if message:
        return {"message": message}
    else:
        return {"message": None}