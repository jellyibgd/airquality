import pymongo
import socket
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://eieiei:pzwlqA1Efucye7n4@cluster-83va3.mongodb.net/")
db = client.student_scores

@app.route("/")
def hello():
	return 'Hello ja'	

@app.route("/insertscore")
def insertscore():
	id = request.args.get('id')
	q1 = request.args.get('quiz1')
	q2 = request.args.get('quiz2')
	q3 = request.args.get('quiz3')
	q4 = request.args.get('quiz4')
	q5 = request.args.get('quiz5')
	summ = request.args.get('sum')

	db.scores.insert_one({'id': int(id),'quiz 1': int(q1),'quiz 2': int(q2),'quiz 3': int(q3),'quiz 4': int(q4),'quiz 5': int(q5),'sum': int(summ)})
	return 'done laew wei'

@app.route("/findscore")
def findscore():
	id = request.args.get('id')
	x = db.scores.find_one({'id': int(id)})
	del x['_id']
	return jsonify({'data': x})