from sqlalchemy import Column, Integer, String, Date, ARRAY
from app.database.session import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tags = Column(ARRAY(String))
    ingredients = Column(ARRAY(String))
    last_cooked = Column(Date)
