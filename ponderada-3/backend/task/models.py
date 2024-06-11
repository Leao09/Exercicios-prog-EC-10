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

# Classe para o login dos usuários
