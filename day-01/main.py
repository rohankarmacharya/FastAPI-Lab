from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Developer API"}

@app.get("/developers")
def get_developers():
    return [
        {
            "id": 1,
            "name": "Rohan",
            "role": "Backend Developer"
        },
        {
            "id": 2,
            "name": "Jihyo",
            "role": "Frontend Developer"
        },
    ]