from flask import make_response
import sys
from flask import Flask
from database.database import db
from flask import jsonify, request, render_template
from database.models import Task, User
import requests as http_request
from flask_jwt_extended import JWTManager, set_access_cookies
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__, template_folder='templates')
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
app.config["JWT_SECRET_KEY"] = "goku-vs-vegeta"
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)
# Verifica se o parâmetro create_db foi passado na linha de comando
if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    # cria o banco de dados
    with app.app_context():
        db.create_all()
    # Finaliza a execução do programa
    print("Database created successfully")
    sys.exit(0)


@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    print(username, password)
    # Query your database for username and password
    user = User.query.filter_by(name=username, password=password).first()
    print(user)
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401

    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({"token": access_token, "user_id": user.id})


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    print(username, password)
    # Verifica os dados enviados não estão nulos
    if username is None or password is None:
        # the user was not found on the database
        return render_template("error.html", message="Bad username or password")
    # faz uma chamada para a criação do token
    token_data = http_request.post(
        "http://localhost:5000/token", json={"username": username, "password": password})
    if token_data.status_code != 200:
        return render_template("error.html", message="Bad username or password")
    # recupera o token
    response = make_response(render_template("content.html"))
    set_access_cookies(response, token_data.json()['token'])
    return response


@app.route("/content", methods=["GET"])
@jwt_required()
def content():
    return render_template("content.html")

@app.route("/user-register", methods=["GET"])
def user_register():
    return render_template("register.html")

@app.route("/error", methods=["GET"])
def error():
    return render_template("error.html")


@app.route("/user-login", methods=["GET"])
def user_login():
    return render_template("login.html")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return_tasks = []
    for task in tasks:
        return_tasks.append(task.serialize())
    return jsonify(return_tasks)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get(id)
    return jsonify(task.serialize())


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = Task(name=data["name"],
                description=data["description"], date=data["date"])
    db.session.add(task)
    db.session.commit()
    return jsonify(task.serialize())


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.json
    task = Task.query.get(id)
    task.name = data["name"]
    task.description = data["description"]
    task.date = data["date"]
    db.session.commit()
    return jsonify(task.serialize())


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify(task.serialize())


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return_users = []
    for user in users:
        return_users.append(user.serialize())
    return jsonify(return_users)


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return jsonify(user.serialize())


@app.route("/users", methods=["POST"])
def create_user():
    username = request.form.get("username")
    email = request.form.get("email")
    passworld = request.form.get("password")
    user = User(name=username, email=email,
                password=passworld)
    db.session.add(user)
    db.session.commit()
    return render_template("login.html")


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    user = User.query.get(id)
    user.name = data["name"]
    user.email = data["email"]
    user.password = data["password"]
    db.session.commit()
    return jsonify(user.serialize())


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize())
