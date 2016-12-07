import numpy as np
import matplotlib.pyplot as plt
import math as m
import seaborn as sns; sns.set()


class MonteCarlo(object):

    def __init__(self, point):
        self.x = np.array(point, dtype=np.float16)[:, 0]
        self.y = np.array(point, dtype=np.float16)[:, 1]

########################### line block ###########################

    def model_line(self, n):
        self.k = np.array(np.random.uniform(m.radians(75), m.radians(150), n), dtype=np.float16)
        self.b = np.array(np.random.uniform(0, 5, n), dtype=np.float16)

    def line_err(self, k, b):
        return sum((self.y - (self.x * k + b)) ** 2)


    def min_error(self):
        return min(map(lambda val: self.line_err(val[0], val[1]), zip(self.k, self.b)))

    def run_line(self):
        mi = self.min_error()
        self.coeff = self.mean(filter(lambda val: self.line_err(val[0], val[1]) <= mi, zip(self.k, self.b)))
        return self.coeff

    def mean(self, arr):
        if len(arr) == 0:
            return 'Bad range'
        arr = np.array(arr)
        return arr[:, 0].sum() / len(arr), arr[:, 1].sum() / len(arr)

    def value_line(self):
        return self.x * self.coeff[0] + self.coeff[1]

########################### sin block ###########################
# fun like: 4 + 5 * np.sin(x * 4 + 5)

    def sin_model(self, n):
        self.a = np.random.uniform(3, 5, n)
        self.p = np.random.uniform(6, 10, n)
        self.c = np.random.uniform(3, 6, n)
        self.d = np.random.uniform(1, 3, n)

    def sin_err(self, a, p, c, d):
        return sum((self.y-(a + p * np.sin(self.x * c + d))) ** 2)

    def sin_min_error(self):
        return min(map(lambda val: self.sin_err(val[0], val[1], val[2], val[3]), zip(self.a, self.p, self.c, self.d)))

    def run_sin(self):
        mi = self.sin_min_error()
        print mi
        self.coeff = filter(lambda val: self.sin_err(val[0], val[1], val[2], val[3]) <= mi, zip(self.a, self.p, self.c, self.d))

        return self.coeff

    def value_sin(self):
        self.coeff = self.coeff[0]
        return self.coeff[0] + self.coeff[1] * np.sin(self.x * self.coeff[2] + self.coeff[3])

########################### plot block ###########################

    def plot_line(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.x, self.value_line(), color='green')
        ax.scatter(self.x, self.y)
        plt.show()

    def plot_sin(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.x, self.value_sin())
        ax.scatter(self.x, self.y)
        plt.show()
        