from fastapi import APIRouter,HTTPException
from auth.jwt_handler import signJWT
from db import database, User
from models import UserSchema

app = APIRouter(tags=["user"])

# Rota de registro de usuário
@app.post("/signup", tags=["user"])
async def sign_up(user: UserSchema):
    user_exists = await User.objects.filter(Email=user.Email).exists()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    new_user = await User.objects.create(Email=user.Email, password=user.password)
    return signJWT(new_user.Id)

# Rota de login de usuário
@app.post("/login", tags=["user"])
async def user_login(user: UserSchema):        
    if check_user(user):
        return signJWT((await User.objects.get(Email=user.Email)).Id)
    return {"error": "Dados inválidos"}

async def check_user(data: UserSchema):
    if not database.is_connected:
        await database.connect()
    
    users = await User.objects.all()
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False