
import uvicorn

from app.models import Base, Film
from app.settings import DATABASE_URL

from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import schemas
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def recreate_database():
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


#recreate_database()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to my film collection"}

#get all films
@app.get("/films")
def get_films(page_size: int = 10, page: int = 1):
    if page_size > 50 or page_size < 0:
        page_size = 50
    session = Session()
    films = session.query(Film).limit(page_size).offset((page - 1) * page_size).all()
    session.close()
    result = jsonable_encoder({"Films": films})
    return JSONResponse(status_code=200, content={"status_code": 200, "result": result})


#Craete a new film
@app.post("/films", status_code=status.HTTP_201_CREATED)
def create_film(film: schemas.FilmCreate):
    session = Session()
    film = Film(**film.dict())
    session.add(film)
    session.commit()
    session.close()
    return {"data":film}

# Get film buy id
@app.get("/films/{film_id}", response_model=schemas.Film)
def read_film(film_id: int):
    db = Session()
    film = db.query(Film).filter(Film.id == film_id).first()
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return film


# Update a film
@app.put("/films/{film_id}", response_model=schemas.FilmBase,status_code=status.HTTP_200_OK)
def update_film(film_id: int, updated_film: schemas.FilmBase):
    db = Session()
    film = db.query(Film).filter(Film.id == film_id).first()
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")

    for key, value in updated_film.dict().items():
        setattr(film, key, value)

    db.commit()
    db.refresh(film)
    return film

# Delete a film
@app.delete("/films/{film_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_film(film_id: int):
    db = Session()
    film = db.query(Film).filter(Film.id == film_id).first()
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    db.delete(film)
    db.commit()


@app.exception_handler(Exception)
def exception_handler(request, exc):
    return {"message":"Internal Server Error"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)