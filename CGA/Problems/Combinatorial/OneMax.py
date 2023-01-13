class OneMax:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    def evalOneMax(self):
        return sum(self.chromosome)
