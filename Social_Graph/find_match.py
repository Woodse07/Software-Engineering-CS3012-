from github import Github
import getpass
import networkx as nx

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
