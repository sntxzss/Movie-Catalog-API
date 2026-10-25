from data import DIRECTORS, MOVIES
from fastapi import FastAPI

app = FastAPI(title="Movie Catalog")

@app.get("/movies")
def get_movies(genre: str = None, year_from: int = None, year_to: int = None, q: str = None, limit: int = 10, offset: int = 0):
    results = MOVIES
    if genre:
        results = [m for m in results if m["genre"].lower() == genre.lower()]
    if year_from:
        results = [m for m in results if m["year"] >= year_from]
    if year_to:
        results = [m for m in results if m["year"] <= year_to]
    if q:
        results = [m for m in results if q.lower() in m["title"].lower()]
    total = len(results)
    items = results[offset:offset + limit]
    return {"total": total, "limit": limit, "offset": offset, "items": items}

@app.get("/movies/{m_id}")
def search_by_id(m_id: int):
    for movie in MOVIES:
        if movie["id"] == m_id:
            return movie

@app.get("/directors/{d_id}")
def dir_id(d_id: int):
    for directors in DIRECTORS:
        if directors["id"] == d_id:
            return directors

@app.get("/directors/{director_id}/movies")
def get_director_movies(
    director_id: int,
    genre: str = None,
    year_from: int = None,
    year_to: int = None,
    q: str = None,
    limit: int = 10,
    offset: int = 0
):
    movies = [m for m in MOVIES if m["director_id"] == director_id]
    if genre:
        movies = [m for m in movies if m["genre"].lower() == genre.lower()]
    if year_from:
        movies = [m for m in movies if m["year"] >= year_from]
    if year_to:
        movies = [m for m in movies if m["year"] <= year_to]
    if q:
        movies = [m for m in movies if q.lower() in m["title"].lower()]
    total = len(movies)
    items = movies[offset:offset + limit]
    return {"total": total, "limit": limit, "offset": offset, "items": items}