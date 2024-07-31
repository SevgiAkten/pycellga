from typing import List
from individual import Individual
import numpy as np

"""
    The Tournament Selection operator is a technique used in genetic algorithms to choose 
    individuals from a population based on a competitive selection process. In this method, a 
    subset of individuals is randomly selected from the population to compete in a 'tournament'. 
    The individual with the highest fitness within this subset is chosen as the winner and is 
    selected for reproduction. Tournament Selection allows for flexible control over selection 
    pressure by adjusting the tournament size, which determines how many individuals participate 
    in each competition. This approach balances exploration and exploitation by giving a chance 
    to less fit individuals while favoring those with higher fitness, thereby promoting both diversity 
    and quality in the evolving population.
"""
class TournamentSelection:
    def __init__(self, pop_list: List[Individual] = {}, c: int = 0, K: int = 2):
        self.pop_list = pop_list
        self.c = c
        self.K = K  # How many people will be chosen at random from neighbors

    def get_parents(self) -> List[Individual]:
        parents = []
        p1 = self.pop_list[self.c - 1]

        parents.append(p1)
        neighbors_positions = p1.neighbors_positions
        neighbors = []

        for i in range(len(self.pop_list)):
            if self.pop_list[i].position in neighbors_positions:
                neighbors.append(self.pop_list[i])

        tournament_selection_pool = []

        while len(tournament_selection_pool) < self.K:

            # ### classical cellular genetic algorithm
            index = np.random.randint(0, len(neighbors))

            if neighbors[index] not in tournament_selection_pool:
                tournament_selection_pool.append(neighbors[index])

            # ### restrict consanguineous marriage
            # index = np.random.randint(0, len(self.pop_list))
            # selected = self.pop_list[index]

            # if selected is not p1:
            #     if selected not in neighbors:
            #         tournament_selection_pool.append(selected)

        tournament_selection_pool_ordered = sorted(
            tournament_selection_pool, key=lambda x: x.fitness_value, reverse=True
        )
        p2 = tournament_selection_pool_ordered[0]
        parents.append(p2)

        return parents
