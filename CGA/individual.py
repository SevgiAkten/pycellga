from numpy import random


class Individual:
    chromosome = []
    fitness_value = 0
    position = (0, 0)
    neighbors_positions = None
    neighbors = None

    def __init__(self, gen_type = "Binary", ch_size = 0):
        self.gen_type = gen_type
        self.ch_size = ch_size
        self.chromosome = [0 for i in range(ch_size)]

    def randomize(self):
        if self.gen_type == "Binary":
            self.chromosome = [random.randint(2) for i in range(self.ch_size)]
            return self.chromosome
        else: 
            raise NotImplementedError(self.gen_type + " not implemented yet.")

    def getneighbors_positions(self):
        return self.neighbors_positions
    
    def setneighbors_positions(self, positions):
        self.neighbors_positions = positions

    def getneighbors(self):
        return self.neighbors
    
    def setneighbors(self, neighbors):
        self.neighbors = list(neighbors) # Copies the argument, not getting the argument itself
    
    
    