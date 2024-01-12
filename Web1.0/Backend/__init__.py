from flask import (
    Flask, redirect, render_template, request, flash, jsonify, send_file
)
import time


app = Flask(__name__)

app.secret_key = b'hypermedia rocks'

@app.route("/")
def index():
    return "Hello World"


@app.route("/Contacts", methods=["GET"])#This is when this endpoint is accessed with a GET Request
def contacts():
    query = request.args.get("q")
    if query is not None: 
        contacts_set = Contact.search(query)
    else:
        contacts_set = Contact.all()
    return render_template("index.html",contacts_set)