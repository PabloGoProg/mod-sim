from base import Base
import numpy as np
from matplotlib import pylab as pl

class ThreeVariables(Base):

  def __init__(self, constants: dict, vars: dict) -> None:
    super().__init__()
    self.s = constants['s']
    self.r = constants['r']
    self.b = constants['b']

    self.x = vars['x']
    self.y = vars['y']
    self.z = vars['z']

    self.results = {
      'x': [],
      'y': [],
      'z': []
    }

    self.dt = 0.001
    self.i = 35
    self.t = 0
    self.timesteps = [0.0]

    self.initialize()
    while self.t < self.i:
      self.update()
      self.observe()

    pl.subplot(3, 1, 1)
    pl.plot(self.timesteps, self.results['x'])

    pl.subplot(3, 1, 2)
    pl.plot(self.timesteps, self.results['y'])

    pl.subplot(3, 1, 3)
    pl.plot(self.timesteps, self.results['z'])

    pl.show()

    # Graphic on 3D
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(self.results['x'], self.results['y'], self.results['z'])
    pl.show()

  def initialize(self):
    self.results['x'].append(self.x)
    self.results['y'].append(self.y)
    self.results['z'].append(self.z)

  def update(self):
    xt, yt, zt = self.x, self.y, self.z
    s, r, b = self.s, self.r, self.b

    self.x = xt + self.dt * (s * (yt - xt))
    self.y = yt + self.dt * (r * xt - yt - xt * zt)
    self.z = zt + self.dt * (xt * yt - b * zt)
    self.t = self.t + self.dt

    self.timesteps.append(self.t)

  def observe(self):
    self.results['x'].append(self.x)
    self.results['y'].append(self.y)
    self.results['z'].append(self.z)

s = ThreeVariables(
  constants={'s': 10.0, 'r': 30.0, 'b': 3.0},
  vars={'x': 1.0, 'y': 1.0, 'z': 1.0}
)
