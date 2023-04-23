# We need to import time from our pc for first seed
import time


# LCG method for generating numbers
class RandGen:
    # initializing numbers for our generator
    def __init__(self, seed):
        self.seed = seed
        self.a = 15.34
        self.c = 1013904223
        self.m = 2 ** 32

    # method for generating numbers
    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed


generator = RandGen(time.time())
