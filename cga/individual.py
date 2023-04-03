from numpy import random
import random as rd


class Individual:
    chromosome = []
    fitness_value = 0
    position = (0, 0)
    neighbors_positions = None
    neighbors = None

    def __init__(self, gen_type="Binary", ch_size=0):
        self.gen_type = gen_type
        self.ch_size = ch_size
        self.chromosome = rd.sample(range(1, 53), self.ch_size)

    def randomize(self):
        if self.gen_type == "Binary":
            self.chromosome = [random.randint(2) for i in range(self.ch_size)]
            return self.chromosome
        elif self.gen_type == "Permutation":
            self.chromosome = list(rd.sample(range(1, 53), self.ch_size))
        elif self.gen_type == "Real-valued":
            self.chromosome = list(rd(range(1, 53), 10))  # it will change
        else:
            raise NotImplementedError(self.gen_type + " not implemented yet.")
        return self.chromosome

    def getneighbors_positions(self):
        return self.neighbors_positions

    def setneighbors_positions(self, positions):
        self.neighbors_positions = positions

    def getneighbors(self):
        return self.neighbors

    def setneighbors(self, neighbors):
        #  Copies the argument, not getting the argument itself
        self.neighbors = list(neighbors)
