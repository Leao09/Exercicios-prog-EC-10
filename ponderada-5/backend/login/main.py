from fastapi import FastAPI
from db import database, User

from routes.user import app as user_router

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)