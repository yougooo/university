import numpy as np
import matplotlib.pyplot as plt
import math as m
import seaborn as sns; sns.set()

# 3+8*np.sin(x*2+4)

points = np.array([[0.0, -3.0544199624634256], [0.69813170079773179, -3.2010454375797162], [1.3962634015954636, 6.9008194827323273], [2.0943951023931953, 10.555785826747972], [2.7925268031909272, 1.7232773965804817], [3.4906585039886591, -4.9991869336879242], [4.1887902047863905, 1.4986341357154496], [4.8869219055841224, 10.477768040999228], [5.5850536063818543, 7.0983674509556041], [6.2831853071795862, -3.0544199624634238]])
x = points[:, 0]
y = points[:, 1]

plt.scatter(points[:, 0], points[:, 1])
plt.plot(points[:, 0], points[:, 1])
plt.show()

#def run_sin(n,x,y):
n = 10

a = (np.random.uniform(m.radians(75), m.radians(150)) for i in range(n))
b = (np.random.uniform(0, 5) for i in range(n))
c = (np.random.uniform(1,10) for i in range(n))
d = (np.random.uniform() for i in range(n))

def foo_sin(a,b,c,d,x,y):
    return y - a *


def run_sin(n, x, y):


print points[:, 0], points[:, 1]
