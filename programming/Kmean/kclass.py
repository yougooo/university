import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import math
from random import choice

class KMean(object):
    def __init__(self):
        self.centers = []
        self.clasters = {}
        self.maxiter = 300

    def make_clasters(self, num_clasters):
        self.clasters = {val: [] for val in xrange(num_clasters)}

    def fit(self, data, num_clasters):
        self.data = data
        self.num_clasters = num_clasters
        self.centers = [list(choice(data)) for i in xrange(num_clasters) ]
        self.claster_block()


    def dist(self, point1, point2):
        return math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1],2))

    def min_dist(self, point):
        temp = map(lambda x: self.dist(x, point), self.centers)
        return temp.index(min(temp))

    def data_to_claster(self):
        map(lambda x: self.clasters[self.min_dist(x)].append(list(x)), self.data)

    def new_centers(self):
        self.centers = map(lambda x: [np.array(x)[:, :1].mean(),np.array(x)[:, 1:].mean()], self.clasters.values())

    def claster_block(self):
        self.clasters.clear()
        self.make_clasters(self.num_clasters)
        self.data_to_claster()

    def k_mean(self):
        it = 0
        while 1:
            old_centers = self.centers
            self.new_centers()
            self.claster_block()
            it = it + 1
            if old_centers == self.centers:
                break
            if it > self.maxiter:
                break
        return self.clasters

    def visual(self):
        color = ['b','g','r','c','m','y','b','w']
        plt.figure(figsize=(20,10))
        for i in range(self.num_clasters):
            plt.scatter(np.array(self.clasters.values()[i])[:, :1],
                        np.array(self.clasters.values()[i])[:, 1:],
                        color=color[i], s=50)
        plt.show()

