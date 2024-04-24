from sqlalchemy import Column, Integer, String
from database.database import db

class Task(db.Model):
  __tablename__ = 'tasks'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  description = Column(String(50), nullable=False)
  date = Column(String(50), nullable=False)

  def __repr__(self):
    return f'<Task:[id:{self.id}, name:{self.name}, description:{self.description}, date:{self.date}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "date": self.date }

