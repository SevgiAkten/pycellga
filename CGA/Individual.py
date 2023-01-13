from numpy import random


class Individual:
    def __init__(self, gen_type, ch_size):
        self.gen_type = gen_type
        self.ch_size = ch_size

    chromosome = []
    fitness_value = 0
    position = (0, 0)
    neighbors = None

    def setChromosome(self):
        if self.gen_type == "Binary":
            ch = random.randint(2, size=self.ch_size)
        return ch
