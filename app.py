from flask import Flask, request, redirect, render_template, jsonify, session, url_for
import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super-secret-key"

# users = {
#     1:  {"name": "Alex Martin",    "email": "alex.martin@email.com"},
#     2: {"name": "Bob Nakamura",  "email": "bob@example.com"},
#     3: {"name": "Clara Osei",    "email": "clara@example.com"},
# }

# Database
engine = sa.create_engine("sqlite:///users.db", echo=True)
metadata = sa.MetaData()

# User table
user_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("email", sa.String(255), unique=True, nullable=False),
    sa.Column("username", sa.String(255), unique=True, nullable=False),
    sa.Column("password", sa.String(255), nullable=False),
)

settings_table = sa.Table(
    "settings",
    metadata,
    sa.Column("user_id", sa.Integer, sa.ForeignKey(
        "user.id"), primary_key=True),
    sa.Column("reminders", sa.Boolean, nullable=False),
    sa.Column("alerts", sa.Boolean, nullable=False),
    sa.Column("darkMode", sa.Boolean, nullable=False),
    sa.Column("textSize", sa.CHAR(1), nullable=False),
    sa.Column("language", sa.String(255), nullable=False),
    sa.Column("pinUrgantTask", sa.Boolean, nullable=False),
    sa.Column("autoHideTask", sa.Boolean, nullable=False),
    sa.Column("sortBy", sa.String(255), nullable=False),
)

metadata.create_all(engine)


@app.route("/")
def homePage():
    return render_template("FirstPage_To-do-list.html")


@app.route("/account")
def account():
    return render_template("SecondPage_account.html")


# @app.route("/account/<int:user_id>")
# def get_user(user_id):
#     user = users.get(user_id)
#     return jsonify({"id": user_id, **user})


@app.route("/settings")
def settings():
    return render_template("ThirdPage_Settings.html")


app.run(debug=True)
