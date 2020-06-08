from api import app, chat_mgr
from flask import render_template, request

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reply")
def reply():
    user_msg = request.args.get("m", None)
    if user_msg and len(user_msg) > 0:
        return {"message": chat_mgr.respond(user_msg)}
    else:
        return {"message": ""}