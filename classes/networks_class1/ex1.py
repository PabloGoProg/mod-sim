import networkx as nx
from matplotlib import pylab as pl
import random

class NetService():

  def __init__(self, n):
    self.g = None
    self.next_g = None

    self.inialize()
    for i in range(n):
      self.update()
      pl.pause(0.2)
      self.draw(i + 1)

  def inialize(self):
    self.g = nx.complete_graph(20)
    self.g.pos = nx.spring_layout(self.g)

    for i in self.g.nodes():
      self.g.nodes[i]['s'] = 1 if random.random() < 0.5 else 0
    
    self.next_g = self.g.copy()
    self.next_g.pos = self.g.pos.copy()

  def update(self):
    for idx, node in enumerate(self.g.nodes()):
      count = self.g.nodes[node]['s']
      count += sum(self.g.nodes[neighbor]['s'] for neighbor in self.g.neighbors(node))

      ratio = count / (self.g.degree(node) + 1)
      self.next_g.nodes[idx]['s'] = 1 if ratio > random.random() \
                                        else 0 if ratio < random.random() \
                                        else 1 if random.random() < random.random() else 0

    self.g, self.next_g = self.next_g, self.g

  def draw(self, i):
    pl.cla()
    nx.draw(self.g, cmap=pl.cm.bwr, vmin=0, vmax=1, 
            node_color = [self.g.nodes[i]['s'] for i in self.g.nodes()],
            pos=self.g.pos)
    pl.title(f'step {i}')

if __name__ == "__main__":
  net = NetService(100)
