import time
from unittest import result
from matplotlib import pylab as pl
from numpy import sqrt

def show_sample_biffurcation():
  def xeq1(r):
    return sqrt(r)

  def xeq2(r):
    return - sqrt(r)

  domain = pl.linspace(0, 10)

  pl.plot(domain, xeq1(domain), 'b-', linewidth=3)
  pl.plot(domain, xeq2(domain), 'r--', linewidth=3)

  pl.plot([0], [0], "go")
  pl.axis([-10, 10, -5, 5])
  pl.xlabel("r")
  pl.ylabel("x")
  pl.title("Bifurcation diagram")
  pl.grid()
  pl.show()

# show_sample_biffurcation()

# Example of system with biffurcation

# from base import Base

class biffurcations():
  def __init__(self):
    super().__init__()
    self.dt = 0.001
    self.t = 0
    self.timesetps = [0]

    self.x = -4
    self.results = []
    self.r = -98
  
    self.initialize()
    for _ in range(100):
      self.update()
      self.observe()

    pl.plot(self.timesetps, self.results)
    pl.xlabel("t")
    pl.ylabel("x")
    pl.grid()
    pl.show()

  def initialize(self):
    self.x = 0.1
    self.results.append(self.x)

  def observe(self):
    self.timesetps.append(self.t)
    self.results.append(self.x)

  def update(self):
    prev_x = self.results[-1]
    self.x = prev_x + ((self.r - (self.x ** 2)) * self.dt)

    self.t += self.dt

biffurcations()