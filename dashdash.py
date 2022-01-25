import matplotlib.pyplot as plt
import math

# functions
def fx_flop(x):
  return (-1)**math.ceil(x-d)
def fx_fullflop(x):
  return v*(-1)**math.ceil((x-d)/a) + s

#goniometric
def fx_sin(x):
  return (-1)**(x/math.pi - 0.5)
def fx_cos(x):
  return (-1)**(x/math.pi)
def fx_tan(x):
  return ((-1)**(x/math.pi - 0.5))/(-1)**(x/math.pi - 0.5)
def fx_cot(x):
  return (-1)**(x/math.pi - 0.5)/((-1)**(x/math.pi - 0.5))
def fx_sec(x):
  return 1/(-1)**(x/math.pi)
def fx_csc(x):
  return 1/(-1)**(x/math.pi - 0.5)

def graph():
  x = x_gen()
  d = 0
  while d <= 2.01:
    path = str(d) + '.png'
    plt.figure(figsize=[19.2, 14.4])
    plt.plot(x, [fx_flop(i) for i in x], 'k')
    plt.savefig('animi/' + path)
    plt.close()
    print(str(d) + " completed")
    d += 0.04
    d = round(d, 2)

def x_gen():
  j = []
  i = round(-2.5*math.pi, 2)
  while -2.5*math.pi <= i <= 2.5*math.pi:
    j.append(i)
    i += 0.01
    i = round(i, 2)
  return j


global v
v = 1
global d
d = 0
global a
a = 1
global s
s = 0

graph()