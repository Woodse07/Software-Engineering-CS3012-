from github import Github
import getpass
import networkx as nx


def find_match(followers, user, goal):

	queue = []
	queue.append([user.login])
	while queue:
		path = queue.pop(0)
		node = path[-1]
		print(node)
		if node == goal.login:
			return path
		for follower in g.get_user(node).get_followers():
			new_path = list(path)
			new_path.append(follower.login)
			queue.append(new_path)


#LOGGING IN THE USER
Username = raw_input("Github Username: ")
Password = getpass.getpass("Github Password: ")
g = Github(Username, Password) #(Username, password) or (Authentication_token) goes here
user = g.get_user()
user.login
print("Successfully logged in user " + user.name)
print("")


#FINDING PERSON OF INTEREST
person_of_interest = raw_input("Who do you want to look for? ")
print("Looking for " + person_of_interest + "...")
poi = g.get_user(person_of_interest)
if poi is None:
	print(person_of_interest + " does not exist!")
print("Found: " + poi.name)
print("")


#CONSTRUCTING NETWORK FOR USER 3 LEVELS DEEP
G = nx.DiGraph()

#FINDING LINK BETWEEN USER AND PERSON OF INTEREST
followers = user.get_followers()
found = 0
dos = 0
r = find_match(followers, user, poi)
if r is not 0:
	print("Found a match!")
	print("Degree of seperation: " + str(len(r)-1))
	print("Path from " + user.name + " to " + poi.name + ": ")
	path = ""
	for element in r:
		path += element + " -> "
	print(path[:-4])
			
		



