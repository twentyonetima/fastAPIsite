from typing import List

from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name: str


class Director(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    year_of_birth: int
    age: int = Field(
        ..., gt=18, lt=99, description='Director age must be more than 18'
    )

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 18:
    #         raise ValueError('Director age must be more than 18')
    #     return v


class Movie(BaseModel):
    title: str
    tagline: str
    description: str
    year: int
    country: str
    genres: List[Genre] = []
    date: date
    times: str


class MovieOut(Movie):
    id: int
