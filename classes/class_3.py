from base import Base
from matplotlib import pyplot as plt
import random

class Class3ex1(Base):

  def __init__(self, initial_value=0, constants=[1]):
    super().__init__()
    self.initial_value = initial_value
    self.constants = constants

    self.current = self.initial_value
    self.result = []

    self.initialize()
    for _ in range(100):
      self.update()
      self.visualize()

    plt.show()

  def initialize(self):
    self.result = [[self.current] for _ in range(len(self.constants[0]))]
    print(self.result)

  def visualize(self):
    plt.plot(self.result)

  def update(self):
    print(self.result)
    for i in range(len(self.constants[0])):
      self.result[i].append(self.constants[0][i] * self.result[i][-1] + self.constants[1][i])

# class3ex1 = Class3ex1(1.0, [
#   [random.randrange(-100, 100) / 100 for _ in range(10)] for _ in range(2)
# ])

# Fibonaccio Sequence

class FiboService(Base):

  def __init__(self):
    super().__init__()
    self.result = []
    self.current = 1

    self.initialize()

    for _ in range(5):
      print(self.result)
      self.update()
      self.visualize()

    plt.grid()
    plt.show()

  def initialize(self):
    self.result = [self.current] * 2

  def visualize(self):
    self.result.append(self.current)
    plt.plot(self.result)

  def update(self):
    self.current = sum(self.result[-2:])

# fibo_service = FiboService()

# Two variables

av = [-0.1, 0.1]
b = -2.0
c = 1.3
dv = [-0.1, 0.1]

# Define the initial conditions
def initialize():
    global x, y, xresult, yresult
    x = 1.0
    y = 1.0
    xresult = [x]
    yresult = [y]

# Photograp of the model in each iteration
def observe():
    global x, y, xresult, yresult
    xresult.append(x)
    yresult.append(y)

# Model that defines the system
def update():
    global x, y
    xtemp = x
    x = a * x + b * y
    y = c * xtemp + d * y

for a in av:
    for d in dv:
        initialize()
        for t in range(1000):
            update()
            observe()
        plt.plot(xresult, yresult, label='a = ' + str(a) + ', d = ' + str(d))

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
