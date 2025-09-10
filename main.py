from fastapi import FastAPI

from routes import health, character
app = FastAPI()

app.include_router(health.router)
app.include_router(character.router)
