# main.py

from fastapi import FastAPI

app = FastAPI() # creates our FastAPI application

@app.get("/") #an HTTP GET request to the root path ("/") will trigger this function
async def root(): # defines the function that handles that request
    return {"message": "Hello, FastAPI!"} # returns a python dictionary that will be automatically converted to JSON and sent as the response

    # So: GET / -> FastAPI -> root() -> Python dictionary -> JSON response