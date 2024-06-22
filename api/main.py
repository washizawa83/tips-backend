from fastapi import FastAPI

from api.controller import tips


app = FastAPI()
app.include_router(tips.router)
