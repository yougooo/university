import numpy as np
import matplotlib.pyplot as plt
import math as m

# y = 2*x + 4

x = np.array([4,8])
y = np.array([12,20])

def best(data,k,b):
  return x[0] * k[data] + b[data], x[1] * k[data] + b[data]

def foo(x,y,k,b):
  return y - (x * k + b)

def monte_carlo(x,y,n):
  k = (np.random.uniform(m.radians(75),m.radians(150)) for i in range(n))
  b = (np.random.uniform(0,5) for i in range(n))
  #print type(k),type(b)
  return filter(lambda t: sum(foo(x,y,t[0],t[1])**2) < 0.001, zip(k,b))

def mean_carlo(arr):
  if len(arr) == 0:
    return 'Bad range'
  arr = np.array(arr)
  return arr[:,0].sum()/len(arr),arr[:,1].sum()/len(arr)


def foo_sin(A, B, C, D):
  print A,B,C,D
  return sin_y - (A + B * np.sin(sin_x * C + D))

def run_sin(n, points):
    #3+8*np.sin(x*2+4)
    # generate data:
    # np.array([(x, 3 + 8 * np.sin(x * 2 + 4)) for x in np.linspace(0, 2 * np.pi, 10)])
  sin_x = np.array(points)[:, 0]
  sin_y = np.array(points)[:, 1]
  A = (np.random.uniform(-4, 4) for i in range(n))
  B = (np.random.uniform(-10, 10) for i in range(n))
  C = (np.random.uniform(-3, 3) for i in range(n))
  D = (np.random.uniform(-6, 6) for i in range(n))
  coeff_sin = filter(lambda val: sum(foo_sin(A.next(), B.next(), C.next(), D.next())**2) < 0.01, range(n))
  return coeff_sin


points = [[0.0, -3.0544199624634256], [0.69813170079773179, -3.2010454375797162], [1.3962634015954636, 6.9008194827323273], [2.0943951023931953, 10.555785826747972], [2.7925268031909272, 1.7232773965804817], [3.4906585039886591, -4.9991869336879242], [4.1887902047863905, 1.4986341357154496], [4.8869219055841224, 10.477768040999228], [5.5850536063818543, 7.0983674509556041], [6.2831853071795862, -3.0544199624634238]]
sin_x = np.array(points)[:, 0]
sin_y = np.array(points)[:, 1]

print run_sin(500000,points)
#data = monte_carlo(x,y,5000)
#print data
#print mean_carlo(data)
