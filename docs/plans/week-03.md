# Week 3 — Advanced FastAPI + AI Preparation
*We can make this week optional depending on how comfortable you are after Week 2.*

## Day 15 — Streaming
*Very important for our AI project.*

**We'll learn:**
- HTTP Streaming
- SSE
- `StreamingResponse`

**Eventually:**
```text
User
 ↓
FastAPI
 ↓
LLM
 ↓
token → token → token → token
 ↓
Browser
```

## Day 16 — WebSockets
We'll learn the difference between:

**HTTP**
```text
Client → Server
       ← Response
```

versus:

**WebSocket**
```text
Client ←────────→ Server
       persistent
       connection
```

**Useful for:**
- Chat
- Live notifications
- AI streaming
- Real-time applications

## Day 17 — External APIs
We'll integrate FastAPI with an external API.

**For example:**
```text
FastAPI
   ↓
GitHub API
   ↓
repositories
   ↓
Pydantic
   ↓
response
```

**We'll learn proper:**
- HTTP clients
- Timeouts
- Retries
- Error handling
- Async requests

## Day 18 — Configuration & Environment
We'll properly handle:
- `.env`
- `settings`
- `secrets`
- development
- production

*using Pydantic Settings.*

## Day 19 — Dockerizing FastAPI
We'll go from:
`python main.py`

to:
```text
Docker
 ↓
FastAPI
 ↓
PostgreSQL
```
*and learn what actually happens inside the container.*

## Day 20 — Production Architecture
We'll put everything together:

```text
                    Client
                       │
                       ▼
                  FastAPI
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Router         Service       Dependency
                       │
                       ▼
                   Database
```

**Then discuss:**
- Reverse proxy
- Workers
- Environment configuration
- Logging
- Health checks
- Observability
- Deployment

## Day 21 — Mini Project #2
We'll build something closer to a real application.

**I'm thinking:** AI Document API

```text
Upload document
      ↓
Extract text
      ↓
Process
      ↓
Store
      ↓
Ask questions
      ↓
FastAPI
      ↓
LLM
```

*This becomes the perfect bridge into our AI Concierge.*
