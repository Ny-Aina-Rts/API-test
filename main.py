from datetime import datetime
from math import trunc
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.responses import PlainTextResponse, HTMLResponse

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return "pong"

@app.get("/home", response_class=HTMLResponse)
def home():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Welcome home!</h1>
        </body>
        </html>
    """

@app.get("/{path:path}", include_in_schema=False)
def not_found(path: str):
    return HTMLResponse(
        content="""
            <!DOCTYPE html>
            <html>
            <head>
                <title>404 Not Found</title>
            </head>
            <body>
                <h1>404 NOT FOUND</h1>
            </body>
            </html>
        """,
        status_code=404
    )

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime
class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

posts_storage: List[Post] = []

@app.post("/posts", response_model=List[Post], status_code=201)
def create_posts(posts: List[Post]):
    posts_storage.extend(posts)
    return posts_storage

@app.get("/posts", response_model=List[Post], status_code=200)
def get_posts():
    return posts_storage

@app.put("/posts", response_model=List[Post], status_code=200)
def update_or_create_post(post: Post):
    for i, stored_post in enumerate(posts_storage):
        if stored_post.title == post.title:
            posts_storage[i] = post
            return posts_storage
    posts_storage.append(post)
    return posts_storage

posts_storage: List[Post] = []

@app.post("/posts", response_model=List[Post], status_code=201)
def create_posts(posts: List[Post]):
    posts_storage.extend(posts)
    return posts_storage

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

posts_storage: List[Post] = []

@app.post("/posts", response_model=List[Post], status_code=201)
def create_posts(posts: List[Post]):
    posts_storage.extend(posts)
    return posts_storage

@app.get("/posts", response_model=List[Post], status_code=200)
def get_posts():
    return posts_storage

@app.put("/posts", response_model=List[Post], status_code=200)
def update_or_create_post(post: Post):
    for i, stored_post in enumerate(posts_storage):
        if stored_post.title == post.title:
            posts_storage[i] = post
            return posts_storage
    posts_storage.append(post)
    return posts_storage