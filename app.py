from flask import Flask, render_template, request, redirect, session, url_for
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for sessions

def load_accounts():
    try:
        with open("accounts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_accounts(accounts):
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        accounts = load_accounts()
        username = request.form["username"]
        password = request.form["password"]
        if username in accounts and accounts[username]["password"] == password:
            session["username"] = username
            return redirect("/main")
        else:
            return render_template("login.html", error="Invalid login")
    return render_template("login.html")

@app.route("/main")
def main_menu():
    if "username" not in session:
        return redirect("/")

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)