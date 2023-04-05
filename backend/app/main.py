import uvicorn
import uuid
from fastapi import FastAPI

# import app.router.user as user_api

def create_app():
    app = FastAPI()
    # app.include_router(user_api.router)
    # app.include_router((blade_api.router))
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    # uvicorn app.main:app --reload