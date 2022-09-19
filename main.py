from fastapi import FastAPI, Query, Path, Body
from schemas import *

app = FastAPI()


@app.post("/movie")
def post_movie(item: Movie, director: Director, quantity: int = Body(...)):
    return {"item": item, "director": director, "quantity": quantity}


@app.post('/director')
def post_director(director: Director = Body(..., embed=True)):
    return {'director': director}


@app.get('/movie')
def get_movie(q: List[str] = Query(['test1', 'test2'], description="Search book", deprecated=True)):
    return q


@app.get('/movie/{pk}')
def get_single_movie(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=2500)):
    return {"pk": pk, "pages": pages}
