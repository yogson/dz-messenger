from fastapi import FastAPI

from handlers.users import root_router

app = FastAPI()

app.include_router(root_router)