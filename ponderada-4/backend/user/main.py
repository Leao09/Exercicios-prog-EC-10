from fastapi import FastAPI

from routes.profile import app as profile_router

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

app.include_router(profile_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8004)
