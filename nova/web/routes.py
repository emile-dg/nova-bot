from web import app
from flask import render_template, request
from web import chat_mgr

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reply")
def reply():
    user_msg = request.args.get("msg", None)
    if user_msg and len(user_msg) > 0:
        return {"reply": chat_mgr.respond(user_msg)}
    else:
        return {"reply": ""}