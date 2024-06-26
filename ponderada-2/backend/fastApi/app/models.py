from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    id: int = Field(default=None)
    Name: str = Field(default=None)
    isDone: bool = Field(default=None)
    # Configuração criada para documentação do modelo

    class Config:
        schema_extra = {
            "post_teste": {
                "Name": "ir na padaria",
                "isDone": "false",
            }
        }

# Classe para representar os usuários do sistema
class UpdateTaskSchema(BaseModel):
    isDone: bool

class UserSchema(BaseModel):
    Email: str = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "schema_user": {
                "Email": "teste@mail.com",
                "password": "123"
            }
        }
# Classe para o login dos usuários
