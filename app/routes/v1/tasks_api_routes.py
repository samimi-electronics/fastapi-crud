from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.database import SessionLocal
from app.schemas.task_schemas import TaskSchema, UpsertTaskSchema
from app.services import task_service
from sqlalchemy.orm import Session

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# db_dependency = Annotated[Session, Depends(get_db)]

class UpsertSuccessResponse(BaseModel):
    message: str

@tasks_router.post(path="/", status_code=201)
def create_task(task: UpsertTaskSchema, db: Session = Depends(get_db)) -> UpsertSuccessResponse:
    task_service.create_task(db=db, task=task)
    return { "message": "Task created successfully" }

@tasks_router.get("/", status_code=200)
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[TaskSchema]:
    return task_service.get_tasks(db=db, skip=skip, limit=limit)

@tasks_router.get("/{task_id}/", status_code=200)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task_by_id(db=db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with id => {task_id} was not found")
    return task

@tasks_router.delete("/{task_id}/", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_service.delete_task_by_id(db=db, task_id=task_id)
    return { "message": f"Task with id {task_id} deleted successfully" }