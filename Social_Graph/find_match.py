from github import Github
import getpass
import networkx as nx
from networkx.readwrite import json_graph

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


#def __find_match_dfs(graph, current, goal, visited):
#	if current == goal.login:
#		return [current]
#	
#	if graph.has_node(current):
#		for neighbor in graph.neighbors(current):
#			if neighbor not in visited:
#				visited.add(neighbor)
#				path = __find_match_dfs(graph, neighbor, goal, visited)
#
#				if path is not None:
#					path.insert(0, current)
#					return path
#
#def find_match_dfs(graph, user, goal):	
#	visited = set()
#	visited.add(user.login)
#	return __find_match_dfs(graph, user.login, goal, visited)


def findMatch(Username, Password, person_of_interest):
	#LOGGING IN THE USER
	g = Github(Username, Password) #(Username, password) or (Authentication_token) goes here
	user = g.get_user()
	user.login
	print("Successfully logged in user " + user.name)
	print("")

	#FETCHING PRE-CONSTRUCTED NETWORK
	print("Fetching pre-constructed network...")
	print("")
	G = nx.DiGraph()
	G = nx.read_gml("networks/med_network.gml")

	#FINDING LINK BETWEEN USER AND PERSON OF INTEREST
	poi = g.get_user(person_of_interest)
	r = find_match_bfs(G, user, poi)
	if r is not 0:
		print("Found a match!")
		print("Degree of seperation: " + str(len(r)))
		print("Path from " + user.login + " to " + poi.login + ": ")
		path = ""
		graph = nx.DiGraph()
		for i in range(0, len(r)):
			graph.add_node(r[i])
			if i+1 < len(r):
				graph.add_edge(r[i], r[i+1])
			path += r[i] + " -> "
		nx.write_gml(graph, "temp.gml")
		return(path[:-4])

	else:
		return("No match found :(")
