import databases
import ormar
import sqlalchemy

from config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class Task(ormar.Model):
    class Meta(BaseMeta):
        tablename = "tasks"
        
    id: int = ormar.Integer(primary_key=True)
    Name: str = ormar.String(max_length=1024, nullable=False)
    isDone: bool = ormar.Boolean(default=False)

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
