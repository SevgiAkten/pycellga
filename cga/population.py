from cga.individual import *
from cga.grid import *
from cga.neighborhoods.linear_5 import Linear5
from cga.neighborhoods.linear_9 import Linear9
from cga.neighborhoods.compact_9 import Compact9
from cga.neighborhoods.compact_13 import Compact13
from cga.neighborhoods.compact_21 import Compact21
from cga.neighborhoods.compact_25 import Compact25
from cga.byte_operators import *

from cga.problems.abstract_problem import AbstractProblem
from typing import List


class Population:
    """
    A class to represent a population in an evolutionary algorithm.

    Attributes
    ----------
    ch_size : int
        The size of the chromosome.
    n_rows : int
        The number of rows in the grid.
    n_cols : int
        The number of columns in the grid.
    gen_type : str
        The type of genome representation ("Binary", "Permutation", "Real-valued").
    problem : AbstractProblem
        The problem instance used to evaluate fitness.
    vector : list
        A list used to generate candidates for the population (relevant for MCCCGA).
    """
    def __init__(self, ch_size: int = 0, n_rows: int = 0, n_cols: int = 0, gen_type: str = "", problem: AbstractProblem = None, vector: list = []):
        """
        Initialize the Population with the specified parameters.

        Parameters
        ----------
        ch_size : int, optional
            The size of the chromosome (default is 0).
        n_rows : int, optional
            The number of rows in the grid (default is 0).
        n_cols : int, optional
            The number of columns in the grid (default is 0).
        gen_type : str, optional
            The type of genome representation (default is an empty string).
        problem : AbstractProblem, optional
            The problem instance used to evaluate fitness (default is None).
        vector : list, optional
            A list used to generate candidates (default is an empty list).
        """
        self.ch_size = ch_size
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.gen_type = gen_type
        self.problem = problem
        self.vector = vector

    def initial_population(self) -> List[Individual]:
        """
        Generate the initial population of individuals.

        Returns
        -------
        List[Individual]
            A list of initialized `Individual` objects with their respective chromosomes, fitness values, positions, and neighbors.
        """
        pop_size = self.n_rows * self.n_cols
        pop_list = []

        grid = Grid(self.n_rows, self.n_cols).make_2d_grid()

        for i in range(pop_size):
            ind = Individual(gen_type=self.gen_type, ch_size=self.ch_size)

            # Initialize chromosome and evaluate fitness for CGA
            ind.chromosome = ind.randomize()
            ind.fitness_value = self.problem.f(ind.chromosome)

            # Initialize chromosome and evaluate fitness for MCCGA
            # ind.chromosome = ind.generate_candidate(self.vector)
            # ind_byte_ch = bits_to_floats(ind.chromosome)
            # ind.fitness_value = self.problem.f(ind_byte_ch)

            ind.position = grid[i]
            ind.neighbors_positions = Linear9(
                position=ind.position, n_rows=self.n_rows, n_cols=self.n_cols
            ).calculate_neighbors_positions()
            ind.neighbors = None
            pop_list.append(ind)

        return pop_list
