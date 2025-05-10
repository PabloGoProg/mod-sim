from matplotlib import pylab as pl
'''
eq: x_t+1 = r*x_t * 1 - x_t
'''

class Chaos:
  
  def __init__(self, x_init) -> None:
    self.results = []
    self.x = None
    self.r = None
    self.r_values = pl.linspace(2.5, 4, 1000)
    
    for r in self.r_values:
      self.initialize(x_init)
      self.r = r
      for _ in range(100):
        self.observe()
        self.update()
      pl.plot([r] * len(self.results), self.results, 'k.', markersize=0.5, alpha=0.5)
  
  def initialize(self, x_init):    
    self.x = x_init
    self.results = [self.x]
    
  def update(self):
    x_prev = self.results[-1]
    self.x = (self.r * x_prev) * (1 - x_prev)
  
  def observe(self):
    self.results.append(self.x)

Chaos(0.9)
pl.show()