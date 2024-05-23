from fastapi import APIRouter, Depends, Body, HTTPException, Request
from app.models import TaskSchema, UpdateTaskSchema
from app.auth.jwt_bearer import jwtBearer
from app.db import database, Task


app = APIRouter(tags=["task"])

# return all tasks


@app.get("/task")
async def read_task():
    if not database.is_connected:
        await database.connect()

    return await Task.objects.all()


@app.get("/task/{id}")
async def read_tasks(id: int):
    if not database.is_connected:
        await database.connect()

    return await Task.objects.get(id=id)

# create a task


@app.post("/task", dependencies=[Depends(jwtBearer())], tags=["task"])
async def create_task(task: TaskSchema = Body(default=None)):
    if not database.is_connected:
        await database.connect()

    await Task.objects.create(Name=task.Name,)
    return {"success": "Successfully created"}


@app.put("/task/{id}", dependencies=[Depends(jwtBearer())])
async def update_task(new_task: TaskSchema, id: int):
    if not database.is_connected:
        await database.connect()
    
    task = await Task.objects.get_or_none(id=id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.isDone = new_task.isDone
    await task.update()
    
    return task


@app.delete("/task/{id}", dependencies=[Depends(jwtBearer())])
async def delete_task(id: int):
    if not database.is_connected:
        await database.connect()

    return await Task.objects.delete(id=id)
