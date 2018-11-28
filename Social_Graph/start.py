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

# Endpoint for getting a match, takes in the Username of person of interest.
# Calls find_match.py, whose biproduct is a gml file of the path.
# Calls gml2json with the biproduct of find_match and retruns the JSON.
@app.route('/get_match', methods=['POST'])
def get_path_post():
	name = request.args.get("name")
	print(name)
	print(find_match.findMatch(Username, Password, name))
	return gml2json.main("temp.gml")

# Endpoint for getting the users network.
# Simply returns the json of their network which was pre constructed on setup.
@app.route('/get_network/', methods=['GET'])
def get_network_post():
	return send_file("networks/smallnetwork.json")

# Asks for username and password of github account on start up.
if __name__ == '__main__':
	Username = raw_input("Github Username: ")
	Password = getpass.getpass("Github Password: ")
	app.run()
