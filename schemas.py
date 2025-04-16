from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str
    completed: bool = False

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(ToDoBase):
    pass

class ToDoOut(ToDoBase):
    id: int

    class Config:
        orm_mode = True
