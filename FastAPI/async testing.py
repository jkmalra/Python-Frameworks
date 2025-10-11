import asyncio
import time
from bisect import bisect_left

from fastapi import FastAPI


@app = FastAPI()
async def boiling():
    print("water is boiling...")
    await asyncio.sleep(4)
    print("water Boiled")

@app.get("/")
async def root():
async def chopping():
    print("chopping...")
    await asyncio.sleep(3)
    print("vegetable chopped")

async def working():
    print("working...")
    await asyncio.sleep(2)

async def main():
    await asyncio.gather(boiling(), chopping())

asyncio.run(main())