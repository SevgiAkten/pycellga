import random
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List
from recombination.recombination_operator import RecombinationOperator

class LinearCrossover(RecombinationOperator):
    """
    LinearCrossover performs a linear crossover on a pair of parent individuals
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
        Initialize the LinearCrossover object.

        Parameters
        ----------
        parents : list
            A list containing two parent individuals.
        problem : AbstractProblem
            The problem instance that provides the fitness function.
        """
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        """
        Combine two parent individuals using linear crossover to produce a single offspring.

        Parameters
        ----------
        p1 : Individual
            The first parent individual.
        p2 : Individual
            The second parent individual.
        locationsource : Individual
            The individual from which to copy positional information for the offspring.

        Returns
        -------
        Individual
            The resulting offspring individual.
        """
        chsize = len(p1.chromosome)
        child1_ch = [0 for i in range(chsize)]
        child2_ch = [0 for i in range(chsize)]
        child3_ch = [0 for i in range(chsize)]

        for i in range(chsize):
            p1_allele = p1.chromosome[i]
            p2_allele = p2.chromosome[i]

            child1_ch[i] = round(0.5 * p1_allele + 0.5 * p2_allele, 5)
            child2_ch[i] = round(3 * p1_allele / 2 - 0.5 * p2_allele, 5)
            child3_ch[i] = round(-0.5 * p1_allele + 3 * p2_allele / 2, 5)

        chosed_ch = random.randint(1, 3)
        if chosed_ch == 1:
            chosed_child_ch = child1_ch
        elif chosed_ch == 2:
            chosed_child_ch = child2_ch
        elif chosed_ch == 3:
            chosed_child_ch = child3_ch

        indv = Individual(p1.gen_type, p1.ch_size)
        indv.position = locationsource.position
        indv.neighbors_positions = locationsource.neighbors_positions
        indv.chromosome = list(chosed_child_ch)
        indv.fitness_value = self.problem.f(chosed_child_ch)
        return indv

    def get_recombinations(self) -> List[Individual]:
        """
        Perform the linear crossover on the parent individuals to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2, p1),
            self.combine(p1, p2, p2)
        ]
