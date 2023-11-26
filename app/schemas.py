from pydantic import BaseModel, EmailStr
from typing import List

class FilmBase(BaseModel):
    title: str
    description: str
    release_year: int
    language_id: int
    rental_duration: int
    rental_rate: float
    length: int
    replacement_cost: float
    rating: str
    special_features: List[str]

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    id: int

    class Config:
        orm_mode = True
