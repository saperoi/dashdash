import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
  a = []
  for i in x:
    p = (-1)**math.ceil(i-d)
    a.append(p)
  return a

def run():
  x = [-5, -4.75, -4.5, -4.25, -4, -3.75, -3.5, -3.25, -3, -2.75, -2.5, -2.25, -2, -1.75, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]
  global d
  d = 0
  while d <= 1.01:
    path = str(d) + '.png'
    plt.figure()
    plt.plot(x,f(x), 'k')
    plt.savefig(path)
    plt.close()
    print(str(d) + " completed")
    d += 0.04

# reg = v * (-1)**math.ceil((x-d)/a) + s

# animi = x**((-1)**math.ceil(x-d))

# animii = (-1)**math.ceil(x**((-1)**math.ceil(x-d)-d))

run()
