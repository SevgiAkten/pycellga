from typing import List
from individual import Individual
from selection.selection_operator import SelectionOperator
import numpy as np


class TournamentSelection(SelectionOperator):
    """
    TournamentSelection performs a tournament selection on a population of individuals
    to select parent individuals for crossover.

    Parameters
    ----------
    pop_list : list of Individual
        The population of individuals to select from.
    c : int
        The index of the individual to start selection from.
    K : int
        The number of individuals to be chosen at random from neighbors.
    """

    def __init__(self, pop_list: List[Individual] = [], c: int = 0, K: int = 2):
        """
        Initialize the TournamentSelection object.

        Parameters
        ----------
        pop_list : list of Individual
            The population of individuals to select from.
        c : int
            The index of the individual to start selection from.
        K : int
            The number of individuals to be chosen at random from neighbors.
        """
        self.pop_list = pop_list
        self.c = c
        self.K = K

    def get_parents(self) -> List[Individual]:
        """
        Perform the tournament selection to get parent individuals.

        Returns
        -------
        list of Individual
            A list containing the selected parent individuals.
        """
        parents = []
        p1 = self.pop_list[self.c - 1]
        parents.append(p1)
        neighbors_positions = p1.neighbors_positions
        neighbors = []

        # Find neighbors in the population
        for i in range(len(self.pop_list)):
            if self.pop_list[i].position in neighbors_positions:
                neighbors.append(self.pop_list[i])

        tournament_selection_pool = []

        # Select K individuals randomly from neighbors for the tournament
        while len(tournament_selection_pool) < self.K:
            index = np.random.randint(0, len(neighbors))
            if neighbors[index] not in tournament_selection_pool:
                tournament_selection_pool.append(neighbors[index])

        # Sort the tournament selection pool by fitness value in descending order
        tournament_selection_pool_ordered = sorted(
            tournament_selection_pool, key=lambda x: x.fitness_value, reverse=True
        )

        # Select the individual with the highest fitness value as the second parent
        p2 = tournament_selection_pool_ordered[0]
        parents.append(p2)

        return parents
