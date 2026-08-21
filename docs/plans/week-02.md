# Week 2 — Real Backend Development

## Day 8 — Async Python
Now we go deeper into:
- `async`
- `await`

And understand the difference between:

**Synchronous**
```text
A → wait → B → wait → C
```

**Asynchronous**
```text
A ────────┐
B ────────┼──→ results
C ────────┘
```

*This is especially important for AI APIs because we'll constantly be waiting for:*
- LLM APIs
- GitHub APIs
- Databases
- Vector searches

## Day 9 — Database Integration
We'll introduce PostgreSQL.

**Learn:**
- SQLAlchemy
- Async database access
- Models
- Sessions
- CRUD
- Transactions

*Potentially compare this with Prisma since you already know Prisma.*

## Day 10 — Authentication
**We'll build:**
```text
Register
   ↓
Login
   ↓
JWT
   ↓
Protected endpoint
```

**Learn:**
- OAuth2
- JWT
- Password hashing
- `OAuth2PasswordBearer`
- Authentication dependencies
- Current user

## Day 11 — Authorization
**Authentication:**
> *Who are you?*

**Authorization:**
> *What are you allowed to do?*

We'll implement something like:
- `ADMIN`
- `USER`
- `VIEWER`

*And protect endpoints using dependencies.*

## Day 12 — Middleware & Request Lifecycle
We'll understand what happens between:
```text
Client
 ↓
Middleware
 ↓
Router
 ↓
Dependency
 ↓
Service
 ↓
Database
 ↓
Response
```

**We'll build:**
- Request logging
- Timing middleware
- CORS
- Request IDs

## Day 13 — Background Tasks & Queues
We'll learn the difference between:
- `BackgroundTasks`

And actual job queues such as:
- Redis
- Celery
- RQ

*This will be especially relevant to AI applications.*

**For example:**
```text
Upload document
      ↓
API returns immediately
      ↓
Background worker
      ↓
Extract text
      ↓
Chunk
      ↓
Generate embeddings
      ↓
Store vectors
```
*That's basically part of the future AI Concierge architecture.*

## Day 14 — Testing
**We'll learn:**
- `pytest`
- `FastAPI TestClient`
- Async tests
- Dependency overrides
- Mocking external APIs
- Testing authentication
- Integration tests

*We'll aim for meaningful tests rather than: "Endpoint returned 200, therefore everything is perfect."*
