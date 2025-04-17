from fastapi import FastAPI
from app.routes import tasks, emotions, reflections, health

app = FastAPI(title="Life OS v5 - Cloud Edition")

app.include_router(tasks.router)
app.include_router(emotions.router)
app.include_router(reflections.router)
app.include_router(health.router)
