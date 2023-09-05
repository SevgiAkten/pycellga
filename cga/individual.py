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
        # self.chromosome = rd.sample(range(1, 53), self.ch_size)

    def randomize(self):
        if self.gen_type == "Binary":
            # # CountSat, Fms, Mmdp, OneMax, Ecc, Maxcut20_01, Maxcut20_09, Maxcut100
            self.chromosome = [random.randint(2) for i in range(self.ch_size)]

            # Peak
            # self.chromosome = [[random.randint(2) for g in range(self.ch_size)] for h in range(self.ch_size)]

        elif self.gen_type == "Permutation":
            # # Tsp
            self.chromosome = list(rd.sample(range(1, 15), self.ch_size))
        elif self.gen_type == "Real-valued":
            # # Ackley
            # self.chromosome = [round(rd.uniform(-32.768, 32.768), 3) for i in range(self.ch_size)]
            # # Bohachevsky
            # self.chromosome = [random.randint(-15, 16) for i in range(self.ch_size)]
            # # Fms
            self.chromosome = [round(rd.uniform(-6.4, 6.35), 2)
                               for i in range(self.ch_size)]
            # # Rastrigin
            # self.chromosome = [round(rd.uniform(-5.12, 5.12), 2) for i in range(self.ch_size)]

            # # Rosenbrock
            # self.chromosome = [random.randint(-5, 11) for i in range(self.ch_size)]

            # # Schwefel
            # self.chromosome = [round(rd.uniform(-500.0, 500.0), 4) for i in range(self.ch_size)]

            # # Sphere
            # self.chromosome = [round(rd.uniform(-5.12, 5.12), 2) for i in range(self.ch_size)]
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
