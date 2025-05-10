from base import Base
import numpy as np
from matplotlib import pylab as pl

# 1 ---------------------------

'''
Considera el siguiente sistema dinámico continuo en el tiempo:
𝑑𝑥
𝑑𝑡 = 𝑟𝑥 − 𝑥
3
donde 𝑟 es un parámetro de control.
a) Determine los puntos de equilibrio.
b) Realice un análisis de estabilidad lineal alrededor de los puntos de equilibrio.
c) Encuentra el valor crítico de 𝑟 en el que ocurre una bifurcación y clasifica el tipo
de bifurcación.
Usa Python para simular el sistema para diferentes valores de 𝑟 y grafica la evolución
temporal de 𝑥(𝑡)
'''
