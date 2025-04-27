from fastapi import FastAPI
from . import meal_router
from .database.session import engine, Base

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Create the tables in the database
    Base.metadata.create_all(bind=engine)

app.include_router(meal_router, prefix="/api")
