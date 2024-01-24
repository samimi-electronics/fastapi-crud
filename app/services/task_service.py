from sqlalchemy.orm import Session
from app.schemas.task_schemas import TaskSchema, UpsertTaskSchema
from app.models.task import Task

def create_task(db: Session, task: UpsertTaskSchema):
    db_task = Task()
    db_task.title = task.title
    db_task.description = task.description
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10) -> list[TaskSchema]:
    return db.query(Task).offset(skip).limit(limit).all()

def get_task_by_id(db: Session, task_id: int) -> None:
    return db.query(Task).filter(Task.id == task_id).first()

# async def update_task(updateDto: UpsertTaskSchema):
#     return

def delete_task_by_id(db: Session, task_id: int) -> None:
    found_task = db.query(Task).filter(Task.id == task_id)
    if (found_task is not None):
        found_task.delete()
        db.commit()