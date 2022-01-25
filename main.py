import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

def run():
  x = np.linspace(-5, 5, 100)
  d = 0
  while d <= 1:
    f(x) = np.vectorize(x**((-1)**math.ceil(x-d)))
    path = "./animone/" + d + '.png'
    plt.plot(x,f(x), 'r')
    plt.show(hold=False)
    plt.savefig(path)
    fig.close()
    plt.close()
    d += 0.04

# reg = v * (-1)**math.ceil((x-d)/a) + s

# animi = x**((-1)**math.ceil(x-d))

# animii = (-1)**math.ceil(x**((-1)**math.ceil(x-d)-d))

run()