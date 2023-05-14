# Description: This file contains the class RandGen which is used for generating random numbers

class RandGen:
    # initializing numbers for our generator
    def __init__(self, seed):
        self.seed = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2 ** 32

    # method for generating numbers
    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return int(self.seed % 2)

    def random_zero_to_one(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / 2 ** 32

    # method for returning 0 or 1 based on generated number
    def generate_zero_or_one(self):
        return int(self.random() % 2)

    # method for generating number in range 0 - 1
    def generate_zero_to_one(self):
        return self.random() / self.m
