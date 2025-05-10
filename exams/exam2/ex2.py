from matplotlib import pylab as pl

class PopulationGrowth():
  
  def __init__(self):
    self.results = []
    self.current = None
    self.r = None
    
    r_values = [2.5 + (0.5 * i) for i in range(4)]
    for r in r_values:
      self.initialize(0.2, r)
      for _ in range(100):
        self.update()
        self.observe()
      pl.title(f'Plot with r = {r}')
      pl.xlabel("Time")
      pl.ylabel("Population")
      pl.savefig(f'./ex2_plots/simulacion_r_{r}.png')
      pl.cla()
        
  def initialize(self, x_init, r):
    self.current = x_init
    self.r = r
    self.results = [self.current]
    
  def update(self):
    x_prev = self.results[-1]
    self.current = (self.r * x_prev) * (1 - x_prev)

  def observe(self):
    self.results.append(self.current)
    pl.plot(self.results)
    
PopulationGrowth()

class PopulationGrowth():
  
  def __init__(self):
    self.results = []
    self.current = None
    self.r = None
    
    r_values = pl.linspace(2.5, 4, 1000)
    for r in r_values:
      self.initialize(0.2, r)
      for _ in range(100):
        self.update()
        self.observe()
      pl.plot([r] * len(self.results), self.results, 'k.', markersize=0.5)
      pl.title("Diagrama de Bifurcaciones")
    pl.savefig('./ex2_plots/bifurcaciones.png')
      
  def initialize(self, x_init, r):
    self.current = x_init
    self.r = r
    self.results = [self.current]
    
  def update(self):
    x_prev = self.results[-1]
    self.current = (self.r * x_prev) * (1 - x_prev)

  def observe(self):
    self.results.append(self.current)
    
PopulationGrowth()