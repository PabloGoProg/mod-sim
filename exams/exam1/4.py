from re import L
import numpy as np
from matplotlib import pyplot as plt

def calculate_tolerated_resistance(r, t):
  return np.random.uniform(
    r - (r * t),
    r + (r * t)
  )

v = 12
r1, r2, r3 = 3, 1, 5
itrs = 1000
tolerance = 0.05

currents = []
for _ in range(1000):
  resistances = [r1, r2, r3]
  resistances = [calculate_tolerated_resistance(r, tolerance) for r in resistances]

  total_resistance = sum(resistances)
  currents.append(12 / total_resistance)

plt.hist(currents)
plt.grid()
plt.show()
