from flask import Flask
from database.database import db
from flask import jsonify, request
from database.models import Task

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

# Verifica se o parâmetro create_db foi passado na linha de comando
import sys
if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    # cria o banco de dados
    with app.app_context():
        db.create_all()
    # Finaliza a execução do programa
    print("Database created successfully")
    sys.exit(0)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/tasks", methods=["GET"])
def get_users():
    tasks = Task.query.all()
    return_tasks = []
    for task in tasks:
        return_tasks.append(task.serialize())
    return jsonify(return_tasks)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_user(id):
    task = Task.query.get(id)
    return jsonify(task.serialize())

@app.route("/tasks", methods=["POST"])
def create_user():
    data = request.json
    task = Task(name=data["name"], description=data["description"], date=data["date"])
    db.session.add(task)
    db.session.commit()
    return jsonify(task.serialize())

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    task = Task.query.get(id)
    task.name = data["name"]
    task.description = data["description"]
    task.date = data["date"]
    db.session.commit()
    return jsonify(task.serialize())

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_user(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify(task.serialize())