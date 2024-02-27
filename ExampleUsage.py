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