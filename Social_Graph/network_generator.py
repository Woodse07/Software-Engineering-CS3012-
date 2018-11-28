from github import Github
import getpass
import networkx as nx


#LOGGING IN THE USER
Username = raw_input("Github Username: ")
Password = getpass.getpass("Github Password: ")
g = Github(Username, Password) #(Username, password) or (Authentication_token) goes here
user = g.get_user()
user.login
print("Successfully logged in user " + user.name)
print("")


# Note: I understand this could be implemented a lot nicer, I'll come back to this
#CONSTRUCTING NETWORK FOR USER 4 LEVELS DEEP
#** THIS IS FAR AS I CAN GO WITHOUT EXCEEDING THE API RATE LIMIT
print("Please allow time for the network to be constructed..")
# Create a directed graph object
G = nx.DiGraph()
# Add the logged in user as the root and specify this as level 1
G.add_node(user.login)
G.node[user.login]['level'] = 1
# Get all friends of the user
followers = user.get_followers()
followerSet = set()
# For every friend of the user, maintain a set of followers
# Add a node of a friend, and connect the user and the friend
for follower in followers:
	followerSet.add(follower.login)
	G.add_node(follower.login)
	G.node[follower.login]['level'] = 2
	G.add_edge(user.login, follower.login)
	children = g.get_user(follower.login).get_followers()
	childrenSet = set()
	# For every friend of a friend, again, maintain a set, and if the friend of a friend is
	# the user or any of the users friends, add this node and connect.
	for child in children:
		if child.login not in followerSet and child.login != user.login:	
			childrenSet.add(child.login)
			G.add_node(child.login)
			G.node[child.login]['level'] = 3
			G.add_edge(follower.login, child.login)
			# This was for testing how much I could do with the API rate limit.
			#grandchildren = g.get_user(child.login).get_followers()
			#grandchildrenSet = set()
			#for grandchild in grandchildren:
			#	if grandchild.login not in followerSet and grandchild.login not in childrenSet and grandchild.login != user.login:
			#		grandchildrenSet.add(grandchild.login)
			#		G.add_node(grandchild.login)
			#		G.add_edge(child.login, grandchild.login)
					#grandgrandchildren = g.get_user(grandchild.login).get_followers()
					#for grandgrandchild in grandgrandchildren:
					#	if grandgrandchild.login not in followerSet and grandgrandchild.login not in childrenSet and grandgrandchild.login not in grandchildrenSet and grandgrandchild.login != user.login:
					#		print(grandgrandchild.login)
					#		G.add_node(grandgrandchild.login)
					#		G.add_edge(grandchild.login, grandgrandchild.login)

nx.write_gml(G,"networks/smallnetwork.gml")

#Refer to comments above.
G = nx.DiGraph()
G.add_node(user.login)
followers = user.get_followers()
followerSet = set()
for follower in followers:
	followerSet.add(follower.login)
	G.add_node(follower.login)
	G.add_edge(user.login, follower.login)
	children = g.get_user(follower.login).get_followers()
	childrenSet = set()
	for child in children:
		if child.login not in followerSet and child.login != user.login:	
			childrenSet.add(child.login)
			G.add_node(child.login)
			G.node[child.login]['level'] = 3
			G.add_edge(follower.login, child.login)
			grandchildren = g.get_user(child.login).get_followers()
			grandchildrenSet = set()
			for grandchild in grandchildren:
				if grandchild.login not in followerSet and grandchild.login not in childrenSet and grandchild.login != user.login:
					grandchildrenSet.add(grandchild.login)
					G.add_node(grandchild.login)
					G.add_edge(child.login, grandchild.login)

nx.write_gml(G,"networks/med_network.gml")
			
			
			
		



