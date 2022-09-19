from fastapi import FastAPI
from schemas import *

app = FastAPI()


@app.post("/movie", response_model=MovieOut)
          # response_model_exclude_unset=True,
          # response_model_exclude={'tagline', 'times'}
def post_movie(item: Movie):
    # movie = item.dict()
    # movie["id"] = 3
    # return movie
    return MovieOut(**item.dict(), id=3)
