from matplotlib import pylab as pl
import numpy as np
from collections import defaultdict

class ACEspecies():
  
  def __init__(self):
    self.width = 300
    self.height = 300
    self.config = None
    self.nextconfig = None
    self.time = 0
    
    self.initialize()
    while True:
      self.update()
      self.observe()
    
  def initialize(self):
    self.config = np.zeros([self.width, self.height]) 
    
    # Llenamos de especie 1
    for x in range(1, self.width - 1):
      for y in range(1, self.height // 2):
        state = 1 if np.random.rand() < 0.45 else 0
        self.config[x, y] = state
    
    # Llenamos de especie 2
    for x in range(1, self.width - 1):
      for y in range(self.height // 2, self.height - 1):
        state = 2 if np.random.rand() < 0.8 else 0
        self.config[x, y] = state
        
    self.nextconfig = np.zeros([self.width, self.height])
    
  def update(self):
    self.time += 1
    
    # Obviamos las pimeras y ultimas filas y columnas para representar bordes fijos
    for x in range(1, self.width - 1):
      for y in range(1, self.height - 1):
        counts = {0: 0, 1: 0, 2: 0}
        
        for dx in [-1, 0, 1]:
          for dy in [-1, 0, 1]:
            
            # Contamos la cantidad de cada especie
            state = self.config[x + dx, y + dy]
            counts[state] += 1
            
        value_counts = list(counts.values())
        self.nextconfig[x, y] = value_counts.index(max(value_counts))
    self.config = self.nextconfig
    
  def observe(self):
    pl.cla()
    pl.imshow(self.config)
    pl.title(f'Tiempo: {self.time}')
    pl.show()
    
ACEspecies()