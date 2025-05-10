from pylab import *
from matplotlib import cm
import networkx as nx 

def initialize():
    global g, p_i, p_r, s_r
    p_i = 0.1
    p_r = 0.5
    s_r = 0.35
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)

    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < 0.5 else 0 


def observe():
    global g
    cla()
    nx.draw(g, cmap = cm.Wistia, vmin=0, vmax=1, node_color = [g.nodes[i]['state'] for i in g.nodes], pos = g.pos)

def update():
    global g
    a = choice(list(g.nodes))
    if g.nodes[a]['state'] == 0:
        if g.degree(a) > 0:
            b = choice(list(g.neighbors(a)))
            if g.nodes[b]['state'] == 1:
                if random() < s_r:
                    g.remove_edge(a, b)
                else:
                    g.nodes[a]['state'] = 1 if random() < p_i else 0
    else:
        g.nodes[a]['state'] = 0 if random() < p_r else 1

initialize()
for _ in range(500):
    update()
    pause(0.2)
    observe()

