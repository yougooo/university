from random import random

class Animal(object):

    def __init__(self, steps):
        self.limit = 1000.0
        self.steps = steps
        self.fox_progress = []
        self.rabbit_progress = []

    def time_line(self, animal):
        return map(lambda x: self.run(animal), range(self.steps))

    def run(self, obj):
        obj.current_rabbit_pop()
        obj.current_fox_pop()
        obj.fox_progress.append(obj.pop_fox)
        obj.rabbit_progress.append(obj.pop_rabbit)

class Rabbit(Animal):

    def __init__(self, pop_rabbit, steps):
        Animal.__init__(self, steps)
        self.pop_rabbit = pop_rabbit

    def rabbit_probability(self, val):
        if val > self.pop_rabbit/self.limit:
            self.pop_rabbit += 1

    def current_rabbit_pop(self):
        data = [random() for i in range(self.pop_rabbit)]
        map(lambda x: self.rabbit_probability(x), data)


class Fox(Rabbit):

    def __init__(self, pop_fox, pop_rabbit, steps):
        Rabbit.__init__(self, pop_rabbit, steps)
        self.pop_fox = pop_fox

    def fox_probability(self, val):
        if val < self.pop_rabbit/self.limit and self.pop_rabbit > 10:
            self.pop_rabbit -= 1
            if random() < 1/3.0:
                self.pop_fox += 1
        else:
            if random() > 0.1 and self.pop_fox > 10:
                self.pop_fox -= 1

    def current_fox_pop(self):
        data = [random() for i in range(self.pop_fox)]
        map(lambda x: self.fox_probability(x), data)
