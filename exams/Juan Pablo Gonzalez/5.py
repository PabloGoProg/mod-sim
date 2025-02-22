from unittest import result
from matplotlib import pyplot as plt
import math

class Ex5():

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.current_x = x
    self.current_y = y
    self.results = []

    self.initialize()

    for i in range(100):
      self.update()
      self.observe()

    plt.grid()
    plt.show()

  def initialize(self):
    self.results.append([self.current_x])
    self.results.append([self.current_y])

  def observe(self):
    self.results[0].append(self.current_x)
    self.results[1].append(self.current_y)

    plt.plot(self.results[0])
    plt.plot(self.results[1])


  def update(self):
    x_p, y_p = self.results[0][-1], self.results[1][-1]

    self.current_x = x_p + x_p * (1 - (x_p / 5)) - (1 - (1 / (y_p + 1))) * x_p
    self.current_y = x_p * y_p

x = Ex5(2, 3)
