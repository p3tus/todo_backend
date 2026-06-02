import fastapi.middleware.cors
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

from tasks.router import router as task_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks: list[Task] = []


@app.post("/tasks")
def create_task(task: Task):
    task.append(task)
    return task


status_code = 201

app.include_router(task_router)

app = FastAPI()

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "none"}
