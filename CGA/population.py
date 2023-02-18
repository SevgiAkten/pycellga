from individual import *
from grid import *
from neighborhoods.linear_5 import *
from problems.abstract_problem import AbstractProblem

class Population:
    def __init__(self, ch_size: int, n_rows: int, n_cols: int, gen_type: str, problem: AbstractProblem):
        self.ch_size = ch_size
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.gen_type = gen_type
        self.problem = problem

    def initial_population(self) -> list:

        pop_size = self.n_rows * self.n_cols
        pop_list = []

        grid = Grid(self.n_rows, self.n_cols).make_2d_grid()

        for i in range(pop_size):
            ind = Individual(gen_type = self.gen_type, ch_size = self.ch_size)
            ind.chromosome = ind.randomize()
            ind.position = grid[i]
            ind.fitness_value = self.problem.f(ind.chromosome)
            ind.neighbors_positions = Linear5(
                position = ind.position, n_rows = self.n_rows, n_cols = self.n_cols
            ).calculate_neighbors_positions()
            ind.neighbors = None
            pop_list.append(ind)

        return pop_list