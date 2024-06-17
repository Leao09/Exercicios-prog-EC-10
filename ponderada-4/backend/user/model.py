from pydantic import BaseModel, Field

class ProfileSchema(BaseModel):
    name: str = Field(default=None)
    email: str = Field(default=None)
    description: str = Field(default=None)
    age: int = Field(default=None)

