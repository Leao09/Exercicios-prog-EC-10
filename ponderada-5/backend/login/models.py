from pydantic import BaseModel, Field

# Classe para representar os usuários do sistema
class UpdateTaskSchema(BaseModel):
    isDone: bool

class UserSchema(BaseModel):
    Email: str = Field(default=None)
    password: str = Field(default=None)
    name: str = Field(default=None)

    class Config:
        schema_extra = {
            "schema_user": {
                "Email": "teste@mail.com",
                "password": "123"
            }
        }
# Classe para o login dos usuários
