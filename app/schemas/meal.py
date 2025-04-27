from pydantic import BaseModel
from typing import List
from datetime import date

class MealCreate(BaseModel):
    name: str
    tags: List[str]
    ingredients: List[str]
    last_cooked: date

class MealOut(MealCreate):
    id: int
