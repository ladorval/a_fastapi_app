from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import List

app = FastAPI()


class TodoItem(BaseModel):
  title: str
  description: str
  completed: bool = False


todo_db = [{'title': 'The Great Todo List', 'description': 'Start the todo project.', 'completed': False}]

@app.post("/todos/", response_model=TodoItem)
def create_todo(todo: TodoItem):
  todo_db.append(todo)
  return todo

@app.get("/todos/", response_model=List[TodoItem])
def get_todo():
  return todo_db
