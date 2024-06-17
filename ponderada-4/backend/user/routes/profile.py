from fastapi import APIRouter, Body,HTTPException
from db import database, Profile
from model import ProfileSchema
from logs import LoggerSetup

logger_setup = LoggerSetup()
LOGGER = logger_setup.logger

app = APIRouter(tags=["profile"])

# Rota de registro de usuário
@app.get("/profile")
async def read_profile():
    LOGGER.info("Reading all profiles")
    if not database.is_connected:
        await database.connect()

    return await Profile.objects.all()


@app.get("/profle/{id}")
async def read_infos(id: int):
    LOGGER.info("Reading a profile")
    if not database.is_connected:
        await database.connect()

    return await Profile.objects.get(id=id)

# create a task


@app.post("/profile",)
async def create_user(profile: ProfileSchema = Body(default=None)):
    LOGGER.info("Creating a profile")
    if not database.is_connected:
        await database.connect()

    await Profile.objects.create(Name=profile.name,
                                 Email=profile.email,
                                 Description=profile.description,
                                 Age=profile.age,)
    return {"success": "Successfully created"}


@app.put("/profile/{id}")
async def update_info(id: int, profile: ProfileSchema = Body(default=None)):
    LOGGER.info("Update a profile")
    if not database.is_connected:
        await database.connect()
    
    task = await Profile.objects.get_or_none(id=id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    response = await task.update(Name=profile.name,
                                 Email=profile.email,
                                 Description=profile.description,
                                 Age=profile.age,)
    
    return response


@app.delete("/profile/{id}")
async def delete_task(id: int):
    LOGGER.info("Delete a profile")
    if not database.is_connected:
        await database.connect()

    return await Profile.objects.delete(id=id)