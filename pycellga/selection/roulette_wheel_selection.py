from typing import List
from individual import Individual
from selection.selection_operator import SelectionOperator
import random

class RouletteWheelSelection(SelectionOperator):
    """
    RouletteWheelSelection performs a roulette wheel selection on a population of individuals
    to select parent individuals for crossover.

    Parameters
    ----------
    pop_list : list of Individual
        The population of individuals to select from.
    c : int
        The index of the individual to start selection from.
    """

    def __init__(self, pop_list: List[Individual] = [], c: int = 0):
        """
        Initialize the RouletteWheelSelection object.

        Parameters
        ----------
        pop_list : list of Individual
            The population of individuals to select from.
        c : int
            The index of the individual to start selection from.
        """
        self.pop_list = pop_list
        self.c = c

    def get_parents(self) -> List[Individual]:
        """
        Perform the roulette wheel selection to get parent individuals.

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

        # Calculate the sum of neighbors' fitness values
        neighbors_fitness_sum = 0
        neighbors_fitnesses = []
        for neighbor in neighbors:
            neighbors_fitness_sum += neighbor.fitness_value
            neighbors_fitnesses.append(neighbor.fitness_value)

        # Perform roulette wheel selection
        random_number = random.uniform(0, 1)
        previous_probability = 0
        for neighbor in neighbors:
            previous_probability += (neighbor.fitness_value / neighbors_fitness_sum)

            if p1 != neighbor:
                if random_number < previous_probability:
                    parents.append(neighbor)
                    break

        return parents
