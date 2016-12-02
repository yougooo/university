import numpy as np
import matplotlib.pyplot as plt
import math as m


class MonteCarlo(object):
    def __init__(self, point):
        self.x = np.array(point)[:, 0]
        self.y = np.array(point)[:, 1]

    def model(self):
        pass

    def foo(self, k, b):
        return self.y - (self.x * k + b)

    def mean(self, arr):
        if len(arr) == 0:
            return 'Bad range'
        arr = np.array(arr)
        return arr[:, 0].sum() / len(arr), arr[:, 1].sum() / len(arr)

    def run_line(self, n):
        k = (np.random.uniform(m.radians(75), m.radians(150)) for i in range(n))
        b = (np.random.uniform(0, 5) for i in range(n))
        self.coeff = self.mean(filter(lambda val: sum(self.foo(val[0], val[1])**2) < 0.001, zip(k, b)))
        return self.coeff

   #def run_sin(self,n):
        

    def value(self):
        return self.x * self.coeff[0] + self.coeff[1]

    def plot_line(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.x, self.y)
        ax.plot(self.x, self.value())
        plt.show()


