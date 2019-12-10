import pymongo
import socket
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)


@app.route("/")
def check():
    return 'API is running..'


@app.route("/register")
def register():
    client = pymongo.MongoClient(
        "mongodb+srv://airpeoject:cYhdo8-kacnuc-wubtak@cluster0-rnpzg.gcp.mongodb.net/")
    db = client.air_quality
    usr = request.args.get('username')
    pwd = request.args.get('password')
    form = {"username": usr, "password": pwd}
    db.data.insert_one(form)
    return 'Success'


@app.route("/addplaces")
def addplaces():
    client = pymongo.MongoClient(
        "mongodb+srv://airpeoject:cYhdo8-kacnuc-wubtak@cluster0-rnpzg.gcp.mongodb.net/")
    db = client.air_quality
    usr = request.args.get('username')
    station = request.args.get('station')
    db.data.update(
     { "username": usr },
     { $set: { "places": station } }
    )
    return 'Success'


@app.route("/search")
def search():
    query = request.args.get('q')
    r = requests.get("https://website-api.airvisual.com/v1/search?q="+query +
                     "&units.temperature=celsius&units.distance=kilometer&AQI=US&language=en")
    data = r.json()
    return data


@app.route("/fetch")
def fetch():
    query = request.args.get('q')
    r = requests.get("https://website-api.airvisual.com/v1/stations/"+station)
    data = r.json()
    return data

@app.route("/userfetch")
def userfetch():
    username = request.args.get('usr')
    return 'Success'