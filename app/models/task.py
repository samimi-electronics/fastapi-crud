from sqlalchemy import Column, Integer, String
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    description = Column(String(255), nullable = True)