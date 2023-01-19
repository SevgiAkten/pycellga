import numpy as np


class TournamentSelection:
    def __init__(self, Pop_list):
        self.Pop_list = Pop_list

    def getParents(self):
        K = 2  # How many people will be chosen at random from neighbors
        parents = []
        index = np.random.randint(0, len(self.Pop_list))
        p1 = self.Pop_list[index]
        parents.append(p1)
        Neighbors_positions = p1.neighbors_positions
        Neighbors = []

        for i in range(len(self.Pop_list)):
            if self.Pop_list[i].position in Neighbors_positions:
                Neighbors.append(self.Pop_list[i])

        tournament_selection_pool = []

        while len(tournament_selection_pool) < K:

            index = np.random.randint(0, len(Neighbors))

            if Neighbors[index] not in tournament_selection_pool:
                tournament_selection_pool.append(Neighbors[index])
            else:
                pass

        tournament_selection_pool_ordered = sorted(
            tournament_selection_pool, key=lambda x: x.fitness_value, reverse=True
        )
        p2 = tournament_selection_pool_ordered[0]
        parents.append(p2)

        return parents
