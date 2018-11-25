from flask import Flask
from flask import send_file
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def get_path():
	return render_template("d3test2.html")

@app.route('/', methods=['POST'])
def get_path_post():
	name = request.form['name']
	return "<h1>Working!</h1>"

@app.route('/get_network/', methods=['GET'])
def get_network_post():
	return send_file("smallnetwork.json")

if __name__ == '__main__':
	app.run()
