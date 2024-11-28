from typing import List
from individual import *
from grid import *
from neighborhoods.linear_9 import Linear9
from byte_operators import *
from problems.abstract_problem import AbstractProblem
from enum import Enum 


class OptimizationMethod(Enum):
    """
    OptimizationMethod is an enumeration class that represents the optimization methods used in an evolutionary algorithm.
    The five optimization methods are CGA, SYNCGA, ALPHA_CGA, CCGA, and MCCCGA.
    "cga", "sync_cga", "alpha_cga", "ccga", "mcccga"
    """
    CGA = 1
    SYNCGA = 2
    ALPHA_CGA = 3
    CCGA = 4
    MCCCGA = 5


class Population:
    """
    A class to represent a population in an evolutionary algorithm.

    Attributes
    ----------
    method_name : OptimizationMethod
        The name of the optimization method. Must be one of OptimizationMethod.CGA, OptimizationMethod.SYNCGA, OptimizationMethod.ALPHA_CGA, OptimizationMethod.CCGA, or OptimizationMethod.MCCCGA.
    ch_size : int
        The size of the chromosome.
    n_rows : int
        The number of rows in the grid.
    n_cols : int
        The number of columns in the grid.
    gen_type : str
        The type of genome representation (GeneType.BINARY, Genetype.PERMUTATION, GeneType.REAL).
    problem : AbstractProblem
        The problem instance used to evaluate fitness.
    vector : list
        A list used to generate candidates for the population (relevant for MCCCGA).
    """
    def __init__(self, 
                 method_name: OptimizationMethod = OptimizationMethod.CGA, 
                 ch_size: int = 0, 
                 n_rows: int = 0, 
                 n_cols: int = 0, 
                 gen_type: str = "", 
                 problem: AbstractProblem = None, 
                 vector: list = [],
                 mins : list[float] = [],
                 maxs : list[float] = []):
        """
        Initialize the Population with the specified parameters.

        Parameters
        ----------
        method_name : OptimizationMethod.
            The name of the optimization method. Must be one of OptimizationMethod.CGA, OptimizationMethod.SYNCGA, OptimizationMethod.ALPHA_CGA, OptimizationMethod.CCGA, or OptimizationMethod.MCCCGA.
            Default is OptimizationMethod.CGA.
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
        mins: list[float]
            The minimum values for each gene in the chromosome (for real value optimization).
        maxs: list[float]
            The maximum values for each gene in the chromosome (for real value optimization).
        """
        self.method_name = method_name
        self.ch_size = ch_size
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.gen_type = gen_type
        self.problem = problem
        self.vector = vector
        self.mins = mins
        self.maxs = maxs

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
            ind = Individual(gen_type = self.gen_type, ch_size = self.ch_size, 
                             mins = self.mins, maxs = self.maxs)
                
            # Initialize chromosome and evaluate fitness for cga, syn_cga and alpha_cga
            if self.method_name in [OptimizationMethod.CGA, OptimizationMethod.SYNCGA, OptimizationMethod.ALPHA_CGA, OptimizationMethod.CCGA]:
                ind.chromosome = ind.randomize()
                ind.fitness_value = self.problem.f(ind.chromosome)

            # Initialize chromosome and evaluate fitness for cga and mcccga
            elif self.method_name in [OptimizationMethod.MCCCGA]:
                ind.chromosome = ind.generate_candidate(self.vector)
                ind_byte_ch = bits_to_floats(ind.chromosome)
                ind.fitness_value = self.problem.f(ind_byte_ch)

            ind.position = grid[i]
            ind.neighbors_positions = Linear9(
                position=ind.position, n_rows=self.n_rows, n_cols=self.n_cols
            ).calculate_neighbors_positions()
            ind.neighbors = None
            pop_list.append(ind)

        return pop_list
