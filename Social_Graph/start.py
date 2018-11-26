from flask import Flask
from flask import send_file
from flask import request
from flask import render_template
import getpass
import find_match
import gml2json

app = Flask(__name__)

@app.route('/')
def get_path():
	return render_template("index.html")

@app.route('/get_match', methods=['POST'])
def get_path_post():
	name = request.args.get("name")
	print(name)
	print(find_match.findMatch(Username, Password, name))
	return gml2json.main("temp.gml")

@app.route('/get_network/', methods=['GET'])
def get_network_post():
	return send_file("networks/smallnetwork.json")

if __name__ == '__main__':
	Username = raw_input("Github Username: ")
	Password = getpass.getpass("Github Password: ")
	app.run()
