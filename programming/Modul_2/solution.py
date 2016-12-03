import numpy as np
import matplotlib.pyplot as plt
import math as m
import seaborn as sns; sns.set()


class MonteCarlo(object):
    '''define model model(model_line) first, 
       after that you can work whit object,
       but now its just test class'''
    def __init__(self, point):
        self.x = np.array(point, dtype=np.float16)[:, 0]
        self.y = np.array(point, dtype=np.float16)[:, 1]

    def model_line(self, n):
        '''n: how many generations and iterations will be'''
        self.k = np.array(np.random.uniform(m.radians(75), m.radians(150), n), dtype=np.float16)
        self.b = np.array(np.random.uniform(0, 5, n), dtype=np.float16)

    def line_err(self, k, b):
        return sum((self.y - (self.x * k + b)) ** 2)


    def min_error(self):
        '''find min error for source data(point)'''
        return min(map(lambda val: self.line_err(val[0], val[1]), zip(self.k, self.b)))

    def run_line(self):
        mi = self.min_error()
        self.coeff = self.mean(filter(lambda val: self.line_err(val[0], val[1]) <= mi, zip(self.k, self.b)))
        return self.coeff

    def mean(self, arr):
        if len(arr) == 0:
            return 'Bad range'
        arr = np.array(arr)
        return arr[:, 0].sum()/len(arr), arr[:, 1].sum()/len(arr)

    def value(self):
        return self.x * self.coeff[0] + self.coeff[1]


    def plot_line(self):
        fig = plt.figure(figsize=(20,10))
        ax = fig.add_subplot(111)
        # ax.axis([5, 5, 30, 30])
        #ax.scatter(self.x, self.y)
        ax.plot(self.x, self.value(), color='green',label='RegresionLine')
        ax.scatter(self.x, self.y, label='SourcePoint')
        ax.legend('best')
        plt.show()

