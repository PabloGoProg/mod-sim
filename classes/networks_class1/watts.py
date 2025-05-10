import networkx as nx
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

class WattsStrogat:

  def __init__(self) -> None:
    self.g = None

    self.inialize()
    for i in range(1000):
      self.update()
      plt.pause(0.2)
      self.observe(i + 1)
    

  def inialize(self, n=20, k=4, p=0.0):
    self.g = nx.Graph()
    for node in range(n):
      for edge in range(1, (k // 2) + 1):
        self.g.add_edge(node, (node + edge) % n)
        self.g.add_edge(node, (node - edge) % n)
      
    self.g.pos = nx.spring_layout(self.g)
    self.g.count = 0

  def update(self):
    self.g.count += 1

    if self.g.count % 20 == 0:
      nodes = list(self.g.nodes())
      chosen_node = random.choice(nodes)

      if self.g.degree(chosen_node) > 0:
        self.g.remove_edge(
          chosen_node,
          random.choice(list(self.g.neighbors(chosen_node)))
        )
        nodes.remove(chosen_node)

        for node in self.g.neighbors(chosen_node):
          nodes.remove(node)
        self.g.add_edge(
          chosen_node,
          random.choice(nodes)
        )

  def observe(self, i):
    plt.clf()
    nx.draw(self.g, cmap=plt.cm.bwr, vmin=0, vmax=1, 
            node_color = [self.g.nodes[i] for i in self.g.nodes()],
            pos=self.g.pos)
    plt.title(f'step {i}')

if __name__ == '__main__':
  WattsStrogat()