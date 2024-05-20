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

class User(db.Model):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False)
  password = Column(String(50), nullable=False)

  def __repr__(self):
    return f'<User:[id:{self.id}, name:{self.name}, email:{self.email}, password:{self.password}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "password": self.password}