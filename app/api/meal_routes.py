from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.meal import MealCreate, MealOut
from app.crud import meal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/meals/", response_model=MealOut)
def create_meal_endpoint(meal_in: MealCreate, db: Session = Depends(get_db)):
    return meal.create_meal(db=db, meal=meal_in)

@router.get("/meals/", response_model=list[MealOut])
def read_meals(db: Session = Depends(get_db)):
    return meal.get_meals(db=db)
