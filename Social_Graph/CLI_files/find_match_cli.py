from github import Github
import getpass
import networkx as nx

# Simple BFS. 
# Takes in a newtworkX Directed graph, the logged in user, and the Username of
# the person of interest.
# Returns the path from the logged in user to the person of interest.
def find_match_bfs(graph, user, goal):
	visited = set()
	queue = []
	queue.append([user.login])
	visited.add(user.login)
	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node == goal.login:
			return path
		for follower in graph.neighbors(node):
			if follower not in visited:
				new_path = list(path)
				new_path.append(follower)
				queue.append(new_path)
				visited.add(follower)
	return 0

# DFS, takes in the same parameters and returns the path from user to person_of_interest.
# Not implemented into the frontend but I thought it might be useful to have this here, 
# since if the person of interest is very deep into the network, this should find them faster.
# Admittedly won't make much of a difference for the size of graphs we're dealing with here.
def __find_match_dfs(graph, current, goal, visited):
	if current == goal.login:
		return [current]
	
	if graph.has_node(current):
		for neighbor in graph.neighbors(current):
			if neighbor not in visited:
				visited.add(neighbor)
				path = __find_match_dfs(graph, neighbor, goal, visited)

				if path is not None:
					path.insert(0, current)
					return path

def find_match_dfs(graph, user, goal):	
	visited = set()
	visited.add(user.login)
	return __find_match_dfs(graph, user.login, goal, visited)

# From here on we ask the user for their username and password, and repeatedly ask them for users they want to find, and return to them the path in the form "You -> Your friend -> Your friend's friend"

#LOGGING IN THE USER
Username = raw_input("Github Username: ")
Password = getpass.getpass("Github Password: ")
g = Github(Username, Password) #(Username, password) or (Authentication_token) goes here
user = g.get_user()
user.login
print("Successfully logged in user " + user.name)
print("")

#FETCHING PRE-CONSTRUCTED NETWORK
print("Fetching pre-constructed network...")
print("")
G = nx.DiGraph()
G = nx.read_gml("med_network.gml")

#FINDING LINK BETWEEN USER AND PERSON OF INTEREST
while(1):
	person_of_interest = raw_input("Who are you looking for? ")
	print("")
	poi = g.get_user(person_of_interest)
	r = find_match_bfs(G, user, poi)
	if r is not 0:
		print("Found a match!")
		print("Degree of seperation: " + str(len(r)))
		print("Path from " + user.login + " to " + poi.login + ": ")
		path = ""
		for element in r:
			path += element + " -> "
		print(path[:-4])
	else:
		print("No match found :(")
