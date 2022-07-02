from pydantic import BaseModel
from typing import Optional


class MovieAPI(BaseModel):
    movie: str


class AnimeAPI(BaseModel):
    anime: str


class MusicAPI(BaseModel):
    music: list


class BookAPI(BaseModel):
    book: str


class GamesAPI(BaseModel):
    game: str


class MangaAPI(BaseModel):
    manga: str


class ComicsAPI(BaseModel):
    comic: str

