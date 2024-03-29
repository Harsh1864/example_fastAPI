
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post,user,auth,vote
from .config import Setting
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}

# models.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine, checkfirst=True)





         