import numpy as np
from base import Base
from matplotlib import pylab as pl
import matplotlib.animation as animation

weight, height = 150, 150
state_space = [0, 1]
neighborhood_radius = 1

class GameOfLife(Base):
  
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
    self.ani = animation.FuncAnimation(self.fig, self.update_animation, interval=500)

    pl.show()
    
  def initialize(self):
    self.time = 0
    self.config = np.zeros((self.width, self.height))
    
    for i in range(self.width):
      for j in range(self.height):
        v = np.random.rand()
        if v > 0.85: 
          self.config[i][j] = 1
        else:
          self.config[i][j] = 0
        
    self.next_config = np.zeros((self.width, self.height), dtype=int)
        
  def update(self):
    self.time += 1
    
    for x in range(self.width):
      for y in range(self.height): # Iteración sobre cada celula del AC
        current_state = self.config[x][y]
        count_ones = 0
        
        for di in range(-self.neighborhood_radius, self.neighborhood_radius + 1):
          for dj in range(-self.neighborhood_radius, self.neighborhood_radius + 1):
            if di == 0 and dj == 0:
              continue
            
            # Calcular la posición del vecino
            nx = (x + di) % self.width
            ny = (y + dj) % self.height
            
            # Contar el estado del vecino
            neighbor_state = self.config[nx][ny]
            if neighbor_state == 0:
              count_ones += 1
        
        if current_state == 0 and (count_ones < 2 or count_ones > 3):
          self.next_config[x][y] = 1
        elif current_state == 1 and count_ones == 3:
          self.next_config[x][y] = 0
        else:
          self.next_config[x][y] = current_state
        
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
  
s = GameOfLife()