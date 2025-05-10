import networkx as nx
from matplotlib import pylab as pl
import random

# Votante directo
class NetService():
  
  def __init__(self, n, k=2):
    self.g = None
    self.k = k

    self.inialize()

    for i in range(n):
      self.update()
      pl.pause(0.2)
      self.draw(i + 1)

  def inialize(self):
    self.g = nx.karate_club_graph()
    self.g.pos = nx.spring_layout(self.g)

    for node in self.g.nodes():
      self.g.nodes[node]['s'] = random.choice(range(self.k))

  def update(self):
    speaker = random.choice(list(self.g.nodes()))
    speaker_ngs = list(self.g.neighbors(speaker))

    if len(speaker_ngs) > 0:
      listener = random.choice(speaker_ngs)
      listener_s = self.g.nodes[listener]['s']

      if random.random() < 0.5:
        self.g.nodes[speaker]['s'] = listener_s

  def draw(self, i):
    pl.cla()
    nx.draw(self.g, cmap=pl.cm.bwr, vmin=0, vmax=self.k - 1, 
            node_color = [self.g.nodes[i]['s'] for i in self.g.nodes()],
            pos=self.g.pos)
    pl.title(f'step {i}')

if __name__ == "__main__":
  net = NetService(1000)
