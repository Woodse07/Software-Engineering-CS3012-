from github import Github

g = Github() #(Username, password) or (Authentication_token) goes here

user = g.get_user()
user.login
print("Logged in users name: " + user.name)
print("")
print("Logged in User has the following repositories: ")
for repo in g.get_user().get_repos():
	print(repo.name)
