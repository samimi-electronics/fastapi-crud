from pydantic import BaseModel

class TaskBaseSchema(BaseModel):
    title: str
    description: str

class TaskSchema(TaskBaseSchema):
    id: int

class UpsertTaskSchema(TaskBaseSchema):
    pass