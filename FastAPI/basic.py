from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Jaskaran": "Singh"}

@app.get("/name")
def name():
    return {"name": "jakirat singh"}