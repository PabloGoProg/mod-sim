import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

class WolframRule30:
  def __init__(self, width=100, height=100):
    self.width = width
    self.height = height
    self.rules = {
      (0,0,0): 0,
      (0,0,1): 1,
      (0,1,0): 1,
      (0,1,1): 1,
      (1,0,0): 1,
      (1,0,1): 0,
      (1,1,0): 0,
      (1,1,1): 0
    }

    self.config = np.zeros((self.height, self.width), dtype=int)
    self.config[0, self.width // 2] = 1
    self.time = 1

    self.fig, self.ax = plt.subplots()
    self.img = self.ax.imshow(self.config, cmap='gray', vmin=0, vmax=1, interpolation='none')
    self.ax.set_title("Regla 30 - Autómata Celular")

    self.ani = animation.FuncAnimation(self.fig, self.update, frames=self.height - 1, interval=100, repeat=False)
    plt.show()

  def update(self, frame):
    if self.time < self.height:
      prev_row = self.config[self.time - 1]
      new_row = np.zeros(self.width, dtype=int)
      for i in range(self.width):
        left = prev_row[(i - 1) % self.width]
        center = prev_row[i]
        right = prev_row[(i + 1) % self.width]
        new_row[i] = self.rules[(left, center, right)]
      self.config[self.time] = new_row
      self.time += 1
      self.img.set_array(self.config)

automaton = WolframRule30()
