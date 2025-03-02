from matplotlib import pyplot as plt
from matplotlib import pylab as pl

a = 1
b = 1
c = 1
d = 1
Dt = 0.001

def initialize():
  global x, y, xresult, yresult, t, timesteps
  x = 0.1
  y = 0.1
  xresult = [x]
  yresult = [y]
  t = 0.0
  timesteps = [t]


def observe():
  global x, y, xresult, yresult, t, timesteps
  xresult.append(x)
  yresult.append(y)
  timesteps.append(t)


def update():
  global x, y, t
  temp = x
  x = x + Dt * (a * x - b * x * y)
  y = y + Dt * (-c * y + d * temp * y)
  t = t + Dt

initialize()

while t < 50.0:
  update()
  observe()

# plot_1 = plt.plot(timesteps, xresult)
# plot_1 = plt.plot(timesteps, yresult)
# plot_1 = plt.grid()

xm, ym = pl.meshgrid(pl.arange(0, 10, 0.1), pl.arange(0, 10, 0.1))
xdot = xm - xm * ym
ydot = -ym + xm * ym

plot_2 = pl.streamplot(xm, ym, xdot, ydot, density=2)
pl.show()

xrange = pl.linspace(0, 2, 20)
yrange = pl.linspace(0, 2, 20)
xrange, yrange = pl.meshgrid(xrange, yrange)
