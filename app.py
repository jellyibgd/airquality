import pymongo
import socket
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://airpeoject:cYhdo8-kacnuc-wubtak@cluster0-rnpzg.gcp.mongodb.net/")
db = client.air_quality

@app.route("/")
def check():
    return 'API is running..'

@app.route("/register")
def register():
    usr = request.args.get('username')
    pwd = request.args.get('password')
    form = {"username": usr, "password": pwd}
    db.data.insert_one(form)
    return 'Success'