from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src import models
from src.database import engine
from src.routers import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


app.include_router(users.router, prefix='/api/users')


@app.get("/api")
def main():
    return {"message": "Api responsive"}
