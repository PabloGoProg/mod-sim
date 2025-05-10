from base import Base
import numpy as np
from matplotlib import pylab as pl
import matplotlib.animation as animation

weight, height = 100, 100
state_space = [0, 1]
neighborhood_radius = 1

class CA(Base):
  
  def __init__(self, 
               width=weight,
               height=height, 
               state_space=state_space, 
               neighborhood_radius=neighborhood_radius
               ):
    super().__init__()
    self.width = width
    self.height = height
    self.state_space = state_space
    self.neighborhood_radius = neighborhood_radius
  
    self.time = None
    self.config = None
    self.next_config = None
    
    self.initialize()
    
    # Configurar la visualización
    self.fig, self.ax = pl.subplots()
    self.img = self.ax.imshow(self.config, vmin=0, vmax=len(self.state_space) - 1, cmap='gray')
    self.ax.set_title(f"Time: {self.time}")

    # Crear la animación automática
    self.ani = animation.FuncAnimation(self.fig, self.update_animation, interval=1000)

    pl.show()
    
  def initialize(self):
    self.time = 0
    self.config = np.zeros((self.width, self.height), dtype=int)
    
    for i in range(self.width):
      for j in range(self.height):
        self.config[i][j] = np.random.choice(self.state_space)
        
    self.next_config = np.zeros((self.width, self.height), dtype=int)
        
  def update(self):
    self.time += 1
    
    for x in range(self.width):
      for y in range(self.height): # Iteración sobre cada celula del AC
        current_state = self.config[x][y]
        count_ones = 0
        
        for di in range(- self.neighborhood_radius, self.neighborhood_radius + 1):
          for dj in range(-self.neighborhood_radius, self.neighborhood_radius + 1):
            if di == 0 and dj == 0:
              continue
            
            # Calcular la posición del vecino
            nx = (x + di) % self.width
            ny = (y + dj) % self.height
            
            # Contar el estado del vecino
            neighbor_state = self.config[nx][ny]
            if neighbor_state == 1:
              count_ones += 1
        
        if count_ones > 4 and current_state == 0: 
          self.next_config[x][y] = 1
        elif count_ones >= 3 and current_state == 1:
          self.next_config[x][y] = 1
        elif count_ones < 2 and current_state == 1:
          self.next_config[x][y] = 0
        
    self.config = self.next_config.copy()
  
  def observe(self, iter: int):
    # Los automatas celulares se plotean usando imagenes
    pl.cla()
    pl.imshow(self.config, vmin=0, vmax=len(self.state_space) - 1, cmap='gray') # Config de la imagen
    pl.title(f"Time: {self.time}")
    pl.show()
    
  def update_animation(self, frame):
    """Función de actualización para la animación automática"""
    self.update()
    self.img.set_array(self.config)
    self.ax.set_title(f"Time: {self.time}")
  
s = CA()
