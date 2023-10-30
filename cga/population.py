from individual import *
from grid import *
from neighborhoods.linear_5 import Linear5
from neighborhoods.linear_9 import Linear9
from neighborhoods.compact_9 import Compact9
from neighborhoods.compact_13 import Compact13
from neighborhoods.compact_21 import Compact21
from neighborhoods.compact_25 import Compact25
import byte_operators

from problems.abstract_problem import AbstractProblem
from typing import List


class Population:
    def __init__(self, ch_size: int = 0, n_rows: int = 0, n_cols: int = 0, gen_type: str = "", problem: AbstractProblem = None, vector: list = []):
        self.ch_size = ch_size
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.gen_type = gen_type
        self.problem = problem
        self.vector = vector

    def initial_population(self) -> List[Individual]:

        pop_size = self.n_rows * self.n_cols
        pop_list = []

        grid = Grid(self.n_rows, self.n_cols).make_2d_grid()

        for i in range(pop_size):
            ind = Individual(gen_type=self.gen_type, ch_size=self.ch_size)

            # for cga
            ind.chromosome = ind.randomize()
            ind.fitness_value = self.problem.f(ind.chromosome)

            # for mcccga
            # ind.chromosome = ind.generate_candidate(self.vector)
            # ind_byte_ch = byte_operators.bits_to_floats(ind.chromosome)
            # ind.fitness_value = self.problem.f(ind_byte_ch)

            ind.position = grid[i]
            ind.neighbors_positions = Linear9(
                position=ind.position, n_rows=self.n_rows, n_cols=self.n_cols
            ).calculate_neighbors_positions()
            ind.neighbors = None
            pop_list.append(ind)

        return pop_list
