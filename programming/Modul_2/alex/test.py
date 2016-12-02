import matplotlib.pyplot as plt
import numpy as np
import math as m
import random


x = np.array([-3.0544199624634256, -3.2010454375797162, 6.9008194827323273, 10.555785826747972, 1.7232773965804817, -4.9991869336879242, 1.4986341357154496, 10.477768040999228, 7.0983674509556041, -3.0544199624634238])

data = np.array([(x,3+8*np.sin(x*2+4)) for x in np.linspace(0,2*np.pi,10)])
print data
#print foo(x)
#plt.scatter(x,foo(x))
plt.plot(data)
plt.show()

