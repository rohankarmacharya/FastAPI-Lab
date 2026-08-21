# FastAPI Learning

This repo contains my FastAPI learning notes and examples.
## Step 1 — Check your Python installation

Open your terminal:

```
python3 --version
```

I'd recommend **Python 3.12+** for this learning project.

Then:

```
pip3 --version
```

And check whether `venv` works:

```
python3 -m venv --help
```

If all three work, we're good.

---

## Step 2 — Create our learning project

I'd keep this separate from the eventual portfolio project.

```
mkdir fastapi-learning
cd fastapi-learning
```

Then create a virtual environment:

```
python3 -m venv .venv
```

Activate it:

```
source .venv/bin/activate
```

Your terminal should now show something like:

```
(.venv) rohankarmacharya@...
```

That `(.venv)` is important.

It means the packages we're installing belong to this project rather than your system Python.

---

## Step 3 — Upgrade pip

```
python -m pip install --upgrade pip
```

Then install FastAPI and Uvicorn:

```
pip install fastapi uvicorn
```

### What are these?

**FastAPI**

The actual web framework.

It gives us things like:

```
Routes
Request handling
Validation
Dependency injection
OpenAPI
Swagger UI
```

**Uvicorn**

The server that actually runs our FastAPI application.

Think:

```
FastAPI = application
Uvicorn = server
```

---

## Step 4 — Create our first application

Create:

```
fastapi-learning/
├── .venv/
└── main.py
```

Put this in `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Hello, FastAPI!"}
```

That's our entire application for now.

Don't worry if some of this syntax isn't familiar yet. **We're going to dissect every piece in code.**

---

## Step 5 — Run it

From the project directory:

```
uvicorn main:app --reload
```

You should see something similar to:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Open:

```
http://127.0.0.1:8000
```

You should get:

```json
{  "message": "Hello, FastAPI!"}
```

Boom. That's your first FastAPI API.

---

## Step 6 — The really cool part

Open:

```
http://127.0.0.1:8000/docs
```

You'll get **Swagger UI**.

FastAPI automatically generated an interactive API documentation page from your Python code.

Also try:

```
http://127.0.0.1:8000/redoc
```

That's another automatically generated API documentation interface.

This is one of the things you'll quickly start loving about FastAPI.
