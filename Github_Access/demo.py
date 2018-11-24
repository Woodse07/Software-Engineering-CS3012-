from github import Github

<<<<<<< HEAD
Username = raw_input("Github Username: ")
Password = raw_input("Github Password: ")
g = Github(Username, Password) #(Username, password) or (Authentication_token) goes here
=======
g = Github("") #(Username, password) or (Authentication_token) goes here
>>>>>>> 0335faf8ccb3b96230cb33d33282c51033982d36

user = g.get_user()
user.login
print("Successfully logged in user " + user.name)
print("")
print(user.name + " has the following repositories: ")
for repo in g.get_user().get_repos():
	print(repo.name)
print("")
repo = g.get_repo("Woodse07/Software-Engineering-CS3012-")
print("Contents of " + user.name + "'s Software Engineering Repo: ")
for contents in repo.get_contents(""):
	print(contents)
print("")
print("Branches of " + user.name + "'s Software Engineering Repo: ")
for branch in repo.get_branches():
	print(branch)
print("")
print("Authors and Dates of all commits of " + user.name + "'s Software Engineering Repo: ")
count = 0
for commit in repo.get_commits():
	print(commit.commit.author)
	print(commit.commit.author.date)
	print("")
	count += 1
print("Total amount of commits: " + str(count))

