import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1>Something</h1><p>Okay this could've been awesome</p>"

@app.route('/summarize', methods=['GET'])
def summary():
	
app.run()