from flask import Flask, request, redirect, render_template, jsonify, session, url_for
import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super-secret-key"

users = {
    1:  {"name": "Alex Martin",    "email": "alex.martin@email.com"},
    2: {"name": "Bob Nakamura",  "email": "bob@example.com"},
    3: {"name": "Clara Osei",    "email": "clara@example.com"},
}


@app.route("/")
def homePage():
    return render_template("FirstPage_To-do-list.html")


@app.route("/account")
def account():
    return render_template("SecondPage_account.html")


@app.route("/account/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    return jsonify({"id": user_id, **user})


@app.route("/settings")
def settings():
    return render_template("ThirdPage_Settings.html")


app.run(debug=True)
