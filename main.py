import matplotlib.mathtext as mt
import matplotlib.pyplot as plt
import numpy as np
import fx
d = 0

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

x = np.linspace(-5,5,100)

while d <= 1:
  y = fx.animone
  d += 0.04
  plt.plot(x,y, 'r')
  plt.show(hold=False)
  plt.savefig('animone.' + d + '.png')
  fig.close()
  plt.close()

