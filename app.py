import pymongo
import socket
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return 'Hello ja'