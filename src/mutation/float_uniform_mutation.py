import random
from individual import *
from problems.abstract_problem import AbstractProblem
from mutation.mutation_operator import MutationOperator

class FloatUniformMutation(MutationOperator):
    """
    FloatUniformMutation performs a uniform mutation on an individual's chromosome in a Genetic Algorithm.

    Parameters
    ----------
    mutation_cand : Individual, optional
        The candidate individual to be mutated (default is None).
    problem : AbstractProblem, optional
        The problem instance that provides the fitness function (default is None).
    """

    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        """
        Initialize the FloatUniformMutation object.

        Parameters
        ----------
        mutation_cand : Individual, optional
            The candidate individual to be mutated (default is None).
        problem : AbstractProblem, optional
            The problem instance that provides the fitness function (default is None).
        """
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:
        """
        Perform a uniform mutation on the candidate individual.

        Each gene in the candidate's chromosome is mutated by adding or subtracting a random float uniformly
        sampled from [0, 1]. The mutation is rounded to 5 decimal places.

        Returns
        -------
        Individual
            A new individual with the mutated chromosome.
        """
        # Convert the chromosome to a list to allow mutation
        m_ch = list(self.mutation_cand.chromosome)

        # Mutate each gene in the chromosome
        for i in range(len(m_ch)):
            rnd = random.uniform(0, 1)
            if rnd < 0.5:
                m_ch[i] = round(m_ch[i] - rnd, 5)
            else:
                m_ch[i] = round(m_ch[i] + rnd, 5)

        # Create a new Individual with the mutated chromosome
        mutated_ch_new = list(m_ch)
        mutated = Individual()
        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
