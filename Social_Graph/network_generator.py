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

#CONSTRUCTING NETWORK FOR USER 3 LEVELS DEEP
print("Please allow time for the network to be constructed..")
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
			G.add_edge(follower.login, child.login)
	#		grandchildren = g.get_user(child.login).get_followers()
	#	for grandchild in grandchildren:
	#		if grandchild.login not in followerSet and grandchild.login not in childrenSet and grandchild.login != user.login:
	#			G.add_node(grandchild.login)
	#			G.add_edge(child.login, grandchild.login)

nx.write_gml(G,"smallnetwork.gml")
			
		



