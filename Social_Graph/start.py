from flask import Flask
from flask import send_file
from flask import request
from flask import render_template
import getpass
import find_match

app = Flask(__name__)

@app.route('/')
def get_path():
	return render_template("d3test2.html")

@app.route('/get_match', methods=['POST'])
def get_path_post():
	name = request.args.get("name")
	print(name)
	return find_match.findMatch(Username, Password, name)

@app.route('/get_network/', methods=['GET'])
def get_network_post():
	return send_file("smallnetwork/networks.json")

if __name__ == '__main__':
	Username = raw_input("Github Username: ")
	Password = getpass.getpass("Github Password: ")
	app.run()
