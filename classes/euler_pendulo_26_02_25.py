from base import Base
from matplotlib import pylab as pl
import numpy as np

class GlucoseInsuline(Base):
  def __init__(self, dt=0.01, I=10, k1=0.1, k2=0.05, itrs=100):
    super().__init__()
    self.dt = dt
    self.I = I
    self.K1 = k1
    self.K2 = k2

    self.t = 0
    self.time_steps = []

    self.current_glucose = 0
    self.current_insuline = 0
    self.state_vars = {
      "glucose": [],
      "insuline": []
    }

    self.initialize()
    for _ in range(itrs):
      self.update()
      self.observe()

    pl.plot(self.time_steps, self.state_vars["insuline"], color="r")
    pl.plot(self.time_steps, self.state_vars["glucose"], color="b")
    pl.title("Glucose and Insuline")
    pl.xlabel("Time")
    pl.ylabel("Glucose and Insuline")
    pl.legend(["Insuline", "Glucose"])
    pl.savefig("glucose_insuline.png")

    pl.plot(self.state_vars["glucose"], self.state_vars["insuline"], color="r")
    pl.title("Glucose vs Insuline")
    pl.xlabel("Glucose")
    pl.ylabel("Insuline")
    pl.legend(["Glucose vs Insuline"])
    pl.savefig("glucose_vs_insuline.png")

  def initialize(self):
    self.current_glucose = 1
    self.current_insuline = 1

    self.state_vars["glucose"].append(self.current_glucose)
    self.state_vars["insuline"].append(self.current_insuline)
    self.time_steps.append(0)

  def observe(self):
    self.state_vars["glucose"].append(self.current_glucose)
    self.state_vars["insuline"].append(self.current_insuline)
    self.time_steps.append(self.t)

  def update(self):
    glucose_temp = self.state_vars['glucose'][-1] + ((-self.K1 * self.current_glucose) - (self.current_insuline * self.current_glucose) + self.I) * self.dt
    insuline_temp = self.state_vars['insuline'][-1] + (self.K2 * (self.I - self.current_insuline)) * self.dt

    self.current_glucose = glucose_temp
    self.current_insuline = insuline_temp

    self.t += self.dt

ej = GlucoseInsuline()
