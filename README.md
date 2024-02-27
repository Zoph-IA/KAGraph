# KAGraph Package

The `KAGraph` package offers a powerful and intuitive way to work with directed, weighted graphs in Python. It utilizes adjacency lists to efficiently represent graph structures, providing users with a broad range of functionalities for graph manipulation and analysis.

## Installation

To get started with `KAGraph`, you can easily install it using pip:

```bash
pip install KAGraph
```

## Getting Started

Here's a quick example to show you how to create a graph, add edges, and use some of the available methods:

```python
from KAGraph import KAGraph

# Initialize the Graph
print("\nCreating graph...\n")
graph = KAGraph()
print("Graph created\n")

# Add edges to the graph
graph.new_edge('A', 'B', 10)
print("Added edge A-B with cost 10")
graph.new_edge('B', 'C', 20)
print("Added edge B-C with cost 20\n")

# Display the graph
print("Displaying graph")
graph.view_all()
print("------------\nGraph displayed\n")

# Query the cost of a path
print("Querying cost of direct edge A-C\n")
print(graph.getCost('A', 'C'))
print("Edge cost queried\n")
```

## Loading Data Into the Graph

To populate your graph with data from a file, you can follow the pattern shown below. This example assumes you have a text file (`data.txt`) where the first line indicates the number of nodes and edges, and each subsequent line represents an edge with an origin node, a destiny node, and a weight.

### Example `data.txt` Format
```
3 3
A B 10
B C 20
A C 15
```


This file indicates there are 3 nodes and 3 edges in the graph. Each of the following lines describes an edge between two nodes and its weight.

### Loading the Data

Here's how you can read `data.txt` and load its contents into your graph:

```python
from KAGraph import KAGraph

# Initialize your graph
graph = KAGraph()

# Load data from file
with open("data.txt") as file:
    lines = file.readlines()
nodes, edges = lines[0].split() # The first line contains counts of nodes and edges (unused here, but could be useful for validation)
for i in range(1, len(lines)): # Read each edge and add it to the graph, skip the first line with counts
    origin, destiny, weight = lines[i].split()
    graph.new_edge(origin, destiny, int(weight))  # Ensure weight is an integer
```   
Now your graph is populated with the data from `data.txt`

## Features

### Adding and Removing Elements

- **Add Edges**: Create a new connection between two nodes with a specified weight using `new_edge(origin, destiny, weight)`.
- **Remove Edges**: Eliminate a connection between two nodes with `remove_edge(origin, destiny)`.
- **Remove Nodes**: Remove a node along with all its connected edges using `remove_node(node)`.

### Pathfinding and Analysis

- **Find Shortest Path**: Discover the shortest path between two nodes with `find_shortest_path(start, end)`, which returns the sequence of nodes representing the path.
- **Get Cost**: Retrieve the cost of traveling from one node to another with `getCost(origin, destiny)`.

### Graph Inspection

- **View All Edges**: Print a comprehensive list of all edges and their respective weights with `view_all()`.
- **Get Connections**: Output all outgoing connections from a specified node using `getConnections(origin)`.
- **Get Incoming Nodes**: List all nodes with edges leading to a specified node with `getFromNode(node)`.
- **Get Outgoing Nodes**: List all nodes directly reachable from a specified node with `getToNode(node)`.

## Usage Examples

### Creating and Modifying a Graph

```python
from KAGraph import KAGraph

# Initialize a new Graph instance
graph = KAGraph

# Add multiple edges
graph.new_edge('X', 'Y', 7)
graph.new_edge('Y', 'Z', 3)

# Remove an edge
graph.remove_edge('X', 'Y')

# Remove a node and its associated edges
graph.remove_node('Z')
```

### Analyzing Graphs

```python
# Find the shortest path between two nodes
path = graph.find_shortest_path('A', 'D')
print("Shortest Path:", path)

# Determine the cost of a specific path
cost = graph.getCost('A', 'D')
print("Path Cost:", cost)
```

## Contributing

Contributions to `KAGraph` are welcome! Feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
