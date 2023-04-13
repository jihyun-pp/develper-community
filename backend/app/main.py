import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.router.user as user_api
import app.router.board as board_api
import app.router.reply as reply_api

def create_app():
    app = FastAPI()
    app.include_router(user_api.router)
    app.include_router(board_api.router)
    app.include_router(reply_api.router)
    return app

app = create_app()

app.add_middleware(
    # Cross-Origin Resource Sharing - https://fastapi.tiangolo.com/tutorial/cors/
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[]
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)