import networkx as nx

graph = nx.Graph()

graph.add_node("Valentina")
graph.add_node("Juan Pablo")
graph.add_node("Jimmy Neutron")

graph.add_edges_from(
  [("Valentina", "Carlouss"), ("Carlouss", "Tomas"), ("Tomas", "Valentina")]
)

print(graph)