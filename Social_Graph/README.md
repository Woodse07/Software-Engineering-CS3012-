<h1> Github API Degrees of Seperation </h1>
<h4> Description: </h4>
Program that prompts the user to login, and will generate a network of their friends, friends of their friends etc. The user can then choose to view a graph of their network, or search for someone on github using their username. The program will then use BFS to scan their network (Option to use DFS), and will return the path(Displayed as a force directed graph) from the user to that person through their network. **note the network that is being searched is only 4 levels deep, going beyond this will exceed the github API rate limit, also the network being displayed is only 3 levels deep, since d3 can't handle the size of the graph at 4 levels.**

<h4> Instructions: </h4>

* Run setup.sh `./setup.sh` if an error about permissions come up, just execute `chmod a+rx setup.sh` beforehand.
  * This will install flask, execute the network generator(this takes time), and spin up flask. You should now be able to view your network on localhost:5000, or whatever url is displayed in the terminal.


* If you want to run the program again, but skip generating the network, you can simply run `python start.py`.


<h4> File Descriptions: </h4>

* **setup.sh**
  * Executes necessary commands to get program up and running.


* **network_generatory.py**
  * Prompts user for github username and password, and returns 2 graphs.
    * The first graph is 3 levels deep, this is the one we will display.
    * The second is 4 levels deep and is the one we will search for connections. The exact same as the first, but with another level.


* **find_match.py**
  * Used when the app is running. When the user puts in a Username to look for, this function will be called and will return the path from the user to that person. A graph is constructed from this path.


* **gml2json.py**
  * Simply converts a gml file to json file. This is used for converting gml to json when the app is running.


* **start.py**
  * Spins up local flask server.


* **templates/index.html**
  * The frontend.
  * Contains all the code for generating the graphs with D3.js.


* **networks/gml2json_cli.py**
  * Command line version of gml2json.py, used in setup.sh to convert the original entire network to json.
  * All graph files are stored in this directory.


* **CLI_files/find_match_cli.py**
  * A command line version of find_match.py. Prompts the user to enter their Github Username and Password, fetches the pre-constructed graph, and then takes in a Username.
  * Returns the degree of seperation between you and that person and the path from you to them.
  * Used in very early stages to make sure I had all the code to calculate the degree of seperation and path was correct.


<h4> The Graph: </h4>

* The main graph has 3 levels, level 1 being you, level 2 being your friends, level 3 being your friends friends.
* The graph being searched has 4 levels, the same as whats being displayed, only with your friends friends friends.

* **Functionality**
  * Load your network button
    * Will load the graph of your network down to 3 levels.


  * Find match button
    * First enter Username of person you're looking for, then click find match. If they are found, fter a second or two a graph will appear of the path from you to that person.


  * Hover over Nodes:
    * Hovering over nodes will display the Username that the node represents and highlight the nodes and edges that the node is linked with.


  * Click and Drag Nodes:
    * The ability to drag nodes and place it in  fixed location. Good for spacing out the graph if it's a little cluttered.

  * Colour & Size:
    * The colour and size of the nodes represent the level of them. The largest red node is the logged in user. The slightly smaller and orange nodes are the users friends, and the smallest yellow nodes are the users friends friends. This makes it very clear whats what when you look at the graph, without having to hover over each node.


* **Example**
  * Graph from 'Load your network' button: ![Graph](images/graph.png)

  * Graph when you hover on a node: ![Graph](images/hover.png)

  * Graph when you drag a node: ![Graph](images/dragging.png)

  * Graph when Username is searched: ![Graph](images/search.png)
