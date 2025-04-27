# Next Meals App

## Architecture



| Folder | Purpose |
|--------|---------|
`models/` | SQLAlchemy models (database tables)
`schemas/` | Pydantic models (request/response validation)
`crud/` | Functions to Create, Read, Update, Delete data
`database/` | DB session, engine setup
`api/` | API routes split by feature
`main.py` | Tie everything together (FastAPI app launcher)