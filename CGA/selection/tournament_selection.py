import numpy as np


class TournamentSelection:
    def __init__(self, pop_list, c):
        self.pop_list = pop_list
        self.c = c

    def get_parents(self):
        K = 2  # How many people will be chosen at random from neighbors
        parents = []
        p1 = self.pop_list[self.c - 1]

        parents.append(p1)
        neighbors_positions = p1.neighbors_positions
        neighbors = []

        for i in range(len(self.pop_list)):
            if self.pop_list[i].position in neighbors_positions:
                neighbors.append(self.pop_list[i])

        tournament_selection_pool = []

        while len(tournament_selection_pool) < K:

            index = np.random.randint(0, len(neighbors))

            if neighbors[index] not in tournament_selection_pool:
                tournament_selection_pool.append(neighbors[index])
            else:
                pass

        tournament_selection_pool_ordered = sorted(
            tournament_selection_pool, key=lambda x: x.fitness_value, reverse=True
        )
        p2 = tournament_selection_pool_ordered[0]
        parents.append(p2)

        return parents