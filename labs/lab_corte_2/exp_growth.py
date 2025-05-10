from matplotlib import pyplot as pl
import numpy as np

class ExpGrowth:
  
  def __init__(self, p0, alphas, t):
    self.current = p0 # initial population
    self.alpha = None # growth rate
    self.population = []
    
    self.time = t
    self.dt = 0.0001 # time step
    self.time_steps = []
    
    # Configuración del estilo
    pl.style.use('seaborn-v0_8')
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    fig = pl.figure(figsize=(12, 14))
    
    for i, alpha in enumerate(alphas):
      self.initialize()
      self.alpha = alpha
      
      while self.time_steps[-1] < self.time:
        self.update()
        self.observe()

      ax = pl.subplot(len(alphas), 1, i + 1)
      pl.plot(self.time_steps, self.population, color=colors[i], linewidth=2, 
              label=f'α = {alpha}')
      
      pl.xlabel('Tiempo', fontsize=12)
      pl.ylabel('Población', fontsize=12)
      pl.title(f'Crecimiento Exponencial con α = {alpha}', fontsize=14)
      pl.legend(fontsize=10)
      pl.grid(True, linestyle='--', alpha=0.7)
      
      # Ajustar los márgenes
      pl.tight_layout()
      
    pl.show()

  def initialize(self):
    self.population = [self.current]
    self.time_steps = [0]

  def update(self):
    prev_population = self.population[-1]
    self.current = prev_population + self.alpha * prev_population * self.dt

  def observe(self):
    self.population.append(self.current)
    self.time_steps.append(self.time_steps[-1] + self.dt)
      
ExpGrowth(100, [0.1, 0.5, 1, 1.5], 50)