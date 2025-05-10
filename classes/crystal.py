from pylab import *

width = 50
height = 50
initProb = 0.2

def initialize():
    global time, config, nextConfig
    time = 0
    config = zeros([height, width])
    nextConfig = zeros([height, width])
    for x in range(width):
        for y in range(height):
            state = 1 if random() < initProb else 0
            config[y, x] = state

def observe():
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)
    axis('image')
    title(f"time = {time}")
    show()

def can_review(dx, dy, x, y):
    return (dx == 0 and dy == 0) and (y - dy < 0 or x - dx < 0) and (y + dy > 0 or x + dx > 0) and (dx == 0 or dy == 0)

def update():
    global time, config, nextConfig
    time += 1
    for x in range(width):
        for y in range(height):
            state = config[y, x]
            numberOfAlive = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if can_review(dx, dy, x, y):
                        continue
                    numberOfAlive += config[(y + dy), (x + dx)]
            if numberOfAlive > 1:
                state = 1
            else:
                state = 0
            nextConfig[y, x] = state
    config, nextConfig = nextConfig, config

initialize()
for i in range(5):
    observe()
    update()
    pause(0.5)