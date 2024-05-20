import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    Id: int = ormar.Integer(primary_key=True)
    Email: str = ormar.String(max_length=128, unique=True, nullable=False)
    password: str = ormar.String(max_length=16, nullable=False)

class Task(ormar.Model):
    class Meta(BaseMeta):
        tablename = "tasks"
        
    id: int = ormar.Integer(primary_key=True)
    Name: str = ormar.String(max_length=1024, nullable=False)
    isDone: bool = ormar.Boolean(default=False)

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
