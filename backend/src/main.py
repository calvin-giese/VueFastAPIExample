from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpointTest import test

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(test.router)

@app.get("/")
def home():
    return {"message": "Hello, world!"}