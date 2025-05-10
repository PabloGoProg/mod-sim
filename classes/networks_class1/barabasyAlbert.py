import networkx as nx
from matplotlib import pyplot as plt
import random

class BarabasyAlbert:
  def __init__(self, m0, n):
    self.m0 = m0
    self.n = n
    self.G = None

    self.initialize(m0, n)
    for i in range(100):
      self.observe()
      self.update(self.aleatory_adjunction)
      plt.pause(0.1)
    
    self.draw_convergence()

    self.initialize(m0, n)
    for i in range(100):
      self.observe()
      self.update(self.strong_preferential_selection)
      plt.pause(0.1)

    self.draw_convergence()

    self.initialize(m0, n)
    for i in range(100):
      self.observe()
      self.update(self.negative_preferential_selection)
      plt.pause(0.1)

    self.draw_convergence()
        
  def initialize(self, m0, n):
    self.G = nx.barabasi_albert_graph(m0, n)
    self.G.pos = nx.spring_layout(self.G)
    self.G.count = 0

  def observe(self):
    plt.cla()
    nx.draw(self.G, self.G.pos, with_labels=True)

  def update(self, selection_method):
    self.G.count += 1

    if self.G.count % 10 == 0:
      nodes = self.G.nodes()
      newcomer = max(nodes) + 1

      for _ in range(self.n):
        j = self.preferential_selection()
        self.G.add_edge(newcomer, j)

      self.G.pos[newcomer] = (0, 0)
    self.G.pos = nx.spring_layout(self.G, pos=self.G.pos, iterations=3)

  def preferential_selection(self):
    number_of_degrees = len(self.G.edges())
    r = random.uniform(0, number_of_degrees)

    degree_sum = 0
    for node in self.G.nodes():
      degree_sum += self.G.degree(node)
      if r < degree_sum:
        return node
      
  def aleatory_adjunction(self):
    num_nodes = len(self.G.nodes())
    r = random.uniform(0, num_nodes)
    return r
  
  def strong_preferential_selection(self):
    number_of_degrees = len(self.G.edges())
    r = random.uniform(0, number_of_degrees) ** 2

    degree_sum = 0
    for node in self.G.nodes():
      degree_sum += self.G.degree(node) ** 2
      if r < degree_sum:
        return node
      
  def negative_preferential_selection(self):
    number_of_degrees = len(self.G.edges())
    r = random.uniform(0, (1 / number_of_degrees))

    degree_sum = 0
    for node in self.G.nodes():
      degree_sum += 1 / self.G.degree(node)
      if r < degree_sum:
        return node
    
  def draw_convergence(self):
    plt.figure()
    grados = [self.G.degree(node) for node in self.G.nodes()]
    plt.pie(grados, labels=[f'Nodo {n}' for n in self.G.nodes()], autopct='%1.1f%%')
    plt.title('Distribución de Conexiones por Nodo')
    plt.show()

if __name__ == '__main__':
  m0 = 10
  n = 4
  ba = BarabasyAlbert(m0, n)
    