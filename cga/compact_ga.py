from numpy import random
from problems.single_objective.discrete.binary.one_max import OneMax
from individual import *


class Compact_GA:
    def __init__(self, n_gen: int, ch_size: int, pop_size: int):

        self.n_gen = n_gen
        self.ch_size = ch_size
        self.pop_size = pop_size

    def generate_candidate(self, vector: list) -> list:
        ind = []

        for p in vector:
            ind.append(
                1) if random.rand() < p else ind.append(0)

        return ind

    def generate_vector(self, ch_size: int) -> list:
        vector = [0.5 for p in range(ch_size)]
        return vector

    def compete(self, p1: Individual, p2: Individual):
        if p1.fitness_value > p2.fitness_value:
            return p1, p2
        else:
            return p2, p1

    def update_vector(self, vector, winner: Individual, loser: Individual, pop_size):
        for i in range(len(vector)):
            if winner.chromosome[i] != loser.chromosome[i]:
                if winner.chromosome[i] == 1:
                    vector[i] += 1.0 / float(pop_size)
                else:
                    vector[i] -= 1.0 / float(pop_size)

    def run(self) -> Individual:
        vector = self.generate_vector(self.ch_size)
        best = Individual()

        for i in range(self.n_gen):
            p1 = Individual()
            p2 = Individual()
            p1.chromosome = self.generate_candidate(vector)
            p2.chromosome = self.generate_candidate(vector)

            # fitness calculation
            theproblem = OneMax()
            p1.fitness_value = theproblem.f(p1.chromosome)
            p2.fitness_value = theproblem.f(p2.chromosome)

            winner, loser = self.compete(p1, p2)

            if best:
                if winner.fitness_value > best.fitness_value:
                    best = winner
            else:
                best = winner

            self.update_vector(vector, winner, loser, self.pop_size)
            best.ch_size = len(best.chromosome)

            print("""generation: {} best value: {} best fitness: {}""".format(
                i + 1, best.chromosome, float(best.fitness_value)))

        return best


a = Compact_GA(pop_size=10, ch_size=5, n_gen=3).run()
