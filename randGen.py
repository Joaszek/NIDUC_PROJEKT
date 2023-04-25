# We need to import time from our pc for first seed
import time


# LCG method for generating numbers
class RandGen:
    # initializing numbers for our generator
    def __init__(self, seed):
        self.seed = seed
        self.a = 15.34
        self.c = 1013904223.07
        self.m = 2 ** 32

    # method for generating numbers
    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return int(self.seed % 2)

    def random_zero_to_one(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / 2 ** 32


generator = RandGen(time.time())
