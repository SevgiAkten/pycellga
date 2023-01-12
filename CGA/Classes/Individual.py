class Individual:
    def __init__(self, chromosome, fitness_value, position, neighbors):
        self.chromosome = chromosome
        self.fitness_value = fitness_value
        self.position = position
        self.neighbors = neighbors
