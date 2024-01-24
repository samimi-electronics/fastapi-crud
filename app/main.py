from fastapi import FastAPI
from app.database import engine
from app.routes.v1.v1_api_routes import apiv1_router
import app.models.task;

app.models.task.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(apiv1_router)