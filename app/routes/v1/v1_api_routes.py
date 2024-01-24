from fastapi import APIRouter
from app.routes.v1.tasks_api_routes import tasks_router;

apiv1_router = APIRouter(prefix="/api/v1")

apiv1_router.include_router(tasks_router)