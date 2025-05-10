import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

g.add_edges_from([
  ('A', 'B'),
  ('A', 'C'),
  ('A', 'E'),
  ('B', 'C'),
  ('B', 'A'),
  ('B', 'C'),
  ('E', 'A'),
  ('E', 'C'),
])

nx.draw(g, with_labels=True)
plt.show()