# Week 1 — Day 1: FastAPI Fundamentals

Our goal today is not to memorize FastAPI APIs. It's to understand what is actually happening when a request reaches our FastAPI application.

## 1. What is FastAPI?
Let's start with the simplest definition:
> **FastAPI is a Python framework for building web APIs.**

**Just for building web APIs?**
Not only, but that's its main purpose. FastAPI is mainly designed to build web APIs — endpoints that receive HTTP requests and return responses. It can also handle things like WebSockets, file uploads, background tasks, authentication, middleware, etc.

**And what about AIs?**
Yep. AI applications are a common use case for FastAPI, but FastAPI itself isn't an AI framework. 

For example:
```text
Frontend -> FastAPI -> AI model/API -> Response
```
You can use FastAPI to expose your AI functionality as an API. 

**Examples:**
- Chatbot API
- LLM-powered API
- Image classification API
- Recommendation API
- ML model inference API

**So:**
FastAPI doesn't build the AI; it provides the web/API layer around the AI.
`FastAPI = Python framework mainly focused on building APIs, with other web capabilities too.`

For example, imagine your frontend wants to ask your backend:
```http
GET /developers/69
```

Your FastAPI application can receive that request and return:
```json
{
  "id": 69,
  "name": "Rohan",
  "role": "Backend Developer"
}
```
That's an API.

**Why is it called FastAPI?**
1. **It is built on technologies designed for high-performance asynchronous applications.**
   - Asynchronous apps are apps that can start a task and not waste time doing nothing while that task is finishing. 
   - *Asynchronous = don't waste time waiting; work on other things while something else is in progress.*
   - This is especially useful for things like database queries, API calls, file operations, etc. where your program spends time waiting.
2. **It provides a lot of functionality out of the box, such as:**
   - Request validation
   - JSON serialization
   - OpenAPI documentation
   - Swagger UI
   - Dependency Injection (DI)
   
And we write relatively little code to get all of that.

---

## 2. Before FastAPI, what is a web framework actually doing?
When a client makes a request:
```text
Browser / Mobile App / Frontend -> GET /developers/69 -> Your Backend -> Find the route -> Run your function -> Return response
```

FastAPI handles a lot of machinery around this. Our job is mostly to tell FastAPI: *"When someone sends this kind of request to this URL, run this Python function."*

For example:
```python
@app.get("/developers")
def get_developers():
    return [
        {"id": 1, "name": "Rohan", "role": "Backend Developer"},
        {"id": 2, "name": "Jihyo", "role": "Frontend Developer"}
    ]
```
We are essentially saying: When a `GET` request comes to `/developers`, run `get_developers()`. That's the core idea behind routes.

---

## 3. ASGI - The thing underneath FastAPI
**ASGI - Asynchronous Server Gateway Interface**

Think of ASGI as a standard communication interface between a Python web server and a Python web application.

We have:
```text
Client -> Uvicorn -> ASGI -> FastAPI -> Our route/function
```

**Why do we need ASGI?**
Because the web server and our application need a common way to communicate. 
Similar idea: `Browser -> HTTP -> Python Web Server -> Application`

ASGI defines how an asynchronous Python server communicates with an asynchronous Python web application. **FastAPI is an ASGI framework.** That's the important part for now.

---

## 4. Uvicorn
**Uvicorn is an ASGI server.**

FastAPI isn't the thing listening directly on a port like `localhost:8000`. Uvicorn does that.

Think of it like this:
```text
Our machine -> Port 8000 -> Uvicorn -> ASGI -> FastAPI -> Python Code
```

**So:** 
- **FastAPI** - Your application/framework.
- **Uvicorn** - The server that runs your FastAPI application.

**Starting a FastAPI application**
Suppose your file is `main.py` and contains:
```python
from fastapi import FastAPI
app = FastAPI()
```

You can run it with: 
```bash
uvicorn main:app --reload
```

Let's break that down:
- `main:app` means: look in `main.py` -> use the `app` variable.
- `--reload` means: Restart the server automatically when your code changes.

---

## 5. `FastAPI()` application
Now let's look at this:
```python
from fastapi import FastAPI
app = FastAPI()
```

The important line is: `app = FastAPI()`. Here, `FastAPI()` creates your FastAPI application. 

You can think of `app` as the central object that represents your backend application. You attach routes to it:
```python
@app.get("/hello")
def hello():
    return {"message": "Hello"}
```

Notice this: `@app.get("/hello")`. That `@` thing is a Python decorator. You don't need to deeply understand decorators today. For now, understand it as: *"Register this function as the handler for GET /hello."*

---

## 6. Routes
A route connects an HTTP request to a Python function.

For example:
```python
@app.get("/developers")
def get_developers():
    return {"message": "Getting developers"}
```

- The **route** is: `GET /developers`
- The **handler** is: `get_developers()`

So: 
```text
GET /developers -> get_developers() -> {"message": "Getting developers"}
```
That's one of the most important concepts in FastAPI.

---

## 7. HTTP Methods
| Method | Usually means |
|--------|---------------|
| `GET` | Get/read data |
| `POST` | Create something |
| `PUT` | Replace/update something |
| `PATCH` | Partially update something |
| `DELETE` | Delete something |

For example, our Developer API might have:
```http
GET    /developers
GET    /developers/{id}
POST   /developers
PATCH  /developers/{id}
DELETE /developers/{id}
```

In FastAPI, the HTTP method is part of the route definition:
```python
@app.get("/developers")
def get_developers():
    ...

@app.post("/developers")
def create_developer():
    ...

@app.patch("/developers/1")
def update_developer():
    ...

@app.delete("/developers/1")
def delete_developer():
    ...
```

So these are different endpoints:
- `GET /developers`
- `POST /developers`

...even though the URL path is identical.

---

## 8. Request -> Handler -> Response
This is the mental model. Suppose your client sends: `GET /developers`.

FastAPI receives it and looks for a matching route:
```python
@app.get("/developers")
def get_developers():
    return [
        {"id": 1, "name": "Rohan"},
        {"id": 2, "name": "Jihyo"}
    ]
```

Then:
```text
Request -> GET /developers 
   -> FastAPI finds matching route 
   -> get_developers() 
   -> Python function executes 
   -> Returns Python data 
   -> FastAPI converts it to HTTP response -> JSON
```

The client receives:
```json
[
  {
    "id": 1,
    "name": "Rohan"
  },
  {
    "id": 2,
    "name": "Alice"
  }
]
```

**Here's the cool part:**
You didn't manually write:
```python
json.dumps(...)
```
You didn't manually create:
```http
HTTP/1.1 200 OK
Content-Type: application/json
```
FastAPI handles that stuff for you.

---

## 9. Swagger / OpenAPI
This is one of FastAPI's nicest features. When your application is running, FastAPI automatically generates API documentation.

Usually at: `http://localhost:8000/docs`

You'll get **Swagger UI**. It can show:
```http
GET    /developers
POST   /developers
GET    /developers/{id}
DELETE /developers/{id}
```
And you can actually execute requests directly from the browser! So instead of opening Postman every five seconds while developing, you can often just go to `/docs` and test your API.

**But what is OpenAPI?**
OpenAPI is a specification for describing an API. Swagger UI is a tool that uses that API description to give you an interactive interface.

So don't mix them up:
```text
FastAPI
   │
   ├── Generates OpenAPI schema
   │
   └── Provides Swagger UI
             ↓
          /docs
```

FastAPI also gives you ReDoc, usually at: `/redoc`.
So you'll commonly see:
- `/docs`
- `/redoc`
- `/openapi.json`

We'll explore these properly later.

---

## 10. `async def` vs `def`
Now we reach one of the more important Python/FastAPI concepts.

You can write:
```python
@app.get("/hello")
def hello():
    return {"message": "Hello"}
```
**or:**
```python
@app.get("/hello")
async def hello():
    return {"message": "Hello"}
```
Both are valid. So what's the difference?

**`def`**: A normal synchronous Python function.
Think: *Do this function's work normally.*

**`async def`**: An asynchronous function.
Think: *This function can cooperate with asynchronous operations.*

This becomes particularly useful when you're waiting for things like:
```text
Database -> Network request -> External API -> File operation
```

For example:
```python
@app.get("/users")
async def get_users():
    users = await database.fetch_users()
    return users
```
While the application is waiting for the database operation, the async system can work on other requests rather than simply sitting there doing nothing.