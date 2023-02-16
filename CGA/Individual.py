from numpy import random


class Individual:
    def __init__(self, gen_type="Binary", ch_size=0):
        self.gen_type = gen_type
        self.ch_size = ch_size

    chromosome = []
    fitness_value = 0
    position = (0, 0)
    neighbors_positions = None
    neighbors = None

    def setChromosome(self):
        if self.gen_type == "Binary":
            ch = []
            for i in range(self.ch_size):
                digit = random.randint(2)
                ch.append(digit)
        return ch
