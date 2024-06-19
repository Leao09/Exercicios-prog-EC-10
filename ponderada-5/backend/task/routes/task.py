from fastapi import APIRouter, Depends, Body, HTTPException
from models import TaskSchema
from auth.jwt_bearer import jwtBearer
from db import database, Task
from logs.logger import LoggerSetup

logger_setup = LoggerSetup()
LOGGER = logger_setup.logger


app = APIRouter(tags=["task"])

# return all tasks


@app.get("/task")
async def read_task():
    LOGGER.info("Reading all tasks")
    if not database.is_connected:
        await database.connect()

    return await Task.objects.all()


@app.get("/task/{id}")
async def read_tasks(id: int):
    LOGGER.info("Reading a task")
    if not database.is_connected:
        await database.connect()

    return await Task.objects.get(id=id)

# create a task


@app.post("/task", dependencies=[Depends(jwtBearer()), Depends(jwtBearer.role_verification("user"))])
async def create_task(task: TaskSchema = Body(default=None)):
    LOGGER.info("Creating a task")
    if not database.is_connected:
        await database.connect()

    await Task.objects.create(Name=task.Name,)
    return {"success": "Successfully created"}


@app.put("/task/{id}", dependencies=[Depends(jwtBearer()), Depends(jwtBearer.role_verification("admin"))])
async def update_task(id: int):
    LOGGER.info("Update a task")
    if not database.is_connected:
        await database.connect()
    
    task = await Task.objects.get_or_none(id=id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.isDone = not task.isDone
    await task.update()
    
    return task


@app.delete("/task/{id}", dependencies=[Depends(jwtBearer()), Depends(jwtBearer.role_verification("admin"))])
async def delete_task(id: int):
    LOGGER.info(" Delete a task")
    if not database.is_connected:
        await database.connect()

    return await Task.objects.delete(id=id)
