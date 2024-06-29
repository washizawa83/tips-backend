from fastapi import FastAPI

from api.features.tips.presentaation.controller import tips


app = FastAPI()
app.include_router(tips.router)
