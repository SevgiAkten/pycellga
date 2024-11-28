import random
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List
from recombination.recombination_operator import RecombinationOperator

class UnfairAvarageCrossover(RecombinationOperator):
    """
    UnfairAvarageCrossover performs an unfair average crossover on a pair of parent individuals
    to produce offspring individuals.

    Parameters
    ----------
    parents : list
        A list containing two parent individuals.
    problem : AbstractProblem
        The problem instance that provides the fitness function.
    """

    def __init__(self, parents: list, problem: AbstractProblem):
        """
        Initialize the UnfairAvarageCrossover object.

        Parameters
        ----------
        parents : list
            A list containing two parent individuals.
        problem : AbstractProblem
            The problem instance that provides the fitness function.
        """
        self.parents = parents
        self.problem = problem

    def get_recombinations(self) -> List[Individual]:
        """
        Perform the unfair average crossover on the parent individuals to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]
        chsize = len(p1.chromosome)
        a = p1.chromosome
        b = p2.chromosome

        alpha = random.uniform(0, 1)
        child_1_ch = [0 for i in range(chsize)]
        child_2_ch = [0 for i in range(chsize)]

        alpha = random.uniform(0, 1)
        j = random.randint(1, chsize)

        for i in range(chsize):
            if i <= j:
                child_1_ch[i] = round((1 + alpha) * a[i] - alpha * b[i], 5)
                child_2_ch[i] = round((1 - alpha) * a[i] + alpha * b[i], 5)
            else:
                child_1_ch[i] = round(-alpha * a[i] + (1 + alpha) * b[i], 5)
                child_2_ch[i] = round(alpha * a[i] + (1 - alpha) * b[i], 5)

        # First child
        child_1 = Individual()
        child_1.chromosome = child_1_ch
        child_1.ch_size = len(child_1_ch)
        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1_ch)
        offsprings.append(child_1)

        # Second child
        child_2 = Individual()
        child_2.chromosome = child_2_ch
        child_2.ch_size = len(child_2_ch)
        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2_ch)
        offsprings.append(child_2)

        return offsprings
