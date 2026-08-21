# Week 1 — FastAPI & HTTP Fundamentals

## Day 1 — FastAPI Fundamentals
- What FastAPI is
- ASGI
- Uvicorn
- `FastAPI()` application
- Routes
- HTTP methods
- Request → handler → response
- Swagger/OpenAPI
- `async def` vs `def`

**Mini project:** Basic Developer API

## Day 2 — Routing & Parameters
- Path parameters
- Query parameters
- Optional parameters
- Type conversion
- Parameter validation
- Route ordering
- Multiple HTTP methods

**Example:**
```http
GET /projects
GET /projects/123
GET /projects?language=go
```

## Day 3 — Request Bodies & Pydantic
*This is a big one.*

- Pydantic
- `BaseModel`
- Request schemas
- Nested models
- Optional fields
- Defaults
- Validation
- Field constraints
- Automatic API documentation

**We'll build:**
```http
POST /projects
PUT /projects/{id}
```

## Day 4 — Response Models
- `response_model`
- Response validation
- Returning dictionaries vs models
- `status_code`
- `HTTPException`
- Custom error responses (404, 400, 422, etc.)

**We'll learn the difference between:**
```text
Request schema
       ↓
Business logic
       ↓
Response schema
```

## Day 5 — Dependency Injection
*One of FastAPI's most important concepts.*

**We'll learn:**
- `Depends()`

**And use it for:**
- Shared logic
- Authentication
- Database sessions
- Current user
- Configuration
- Permissions

*This will become extremely important when we eventually build the AI Concierge.*

## Day 6 — Project Structure
We'll move beyond `main.py` into something closer to:

```text
app/
├── main.py
├── api/
├── schemas/
├── services/
├── dependencies/
├── models/
└── core/
```
*We'll understand why we're separating these things rather than blindly copying a folder structure.*

## Day 7 — Mini Project #1
We'll build a small but properly structured API.

**Something like:** Developer Portfolio API

```http
/projects
/skills
/experience
/blogs
```

**It'll have:**
- Routers
- Pydantic schemas
- Services
- Dependency injection
- Validation
- Error handling
- OpenAPI documentation

*That gives us our first checkpoint.*
