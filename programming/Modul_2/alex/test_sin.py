import numpy as np
import matplotlib.pyplot as plt
import random
import math as m

sin1 = [8*np.sin(x)+random.gauss(0.2,.4) for x in np.linspace(2*np.pi,np.pi/3,10)]
sin2 = np.arange(0,2*np.pi,np.pi/3)

plt.plot(sin2, sin1, 'ro')
plt.plot(np.arange(0, 2*np.pi, 0.01), [8*np.sin(i) for i in np.arange(0,2*np.pi, 0.01)], 'b-', c='green')
plt.show()


