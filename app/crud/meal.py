from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.schemas.meal import MealCreate

def create_meal(db: Session, meal: MealCreate):
    db_meal = Meal(**meal.model_dump())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def get_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Meal).offset(skip).limit(limit).all()
