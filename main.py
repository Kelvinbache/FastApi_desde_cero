import uvicorn

from fastapi import FastAPI

# from routers import items, users
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# # # #Routes that we are going to give permission to
origins = {
    "http://localhost:8000",
}

#This is how we create a connection with the cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["Get, POST"],
    allow_headers=["*"],)


# app.include_router(users.router)
# app.include_router(items.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}



if __name__ == "__main__":
   uvicorn.run("main:app",port=8000, log_level="info", reload=True)