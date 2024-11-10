from fastapi import FastAPI
from app.web import explorer, creature, user


app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)
