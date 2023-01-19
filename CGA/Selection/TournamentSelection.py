import numpy as np


class TournamentSelection:
    def __init__(self, Pop_list):
        self.Pop_list = Pop_list

    def getParents(self):
        K = 5  # How many people will be chosen at random first in tournament selection
        parents = []

        while len(parents) < 2:
            tournament_selection_pool = []

            while len(tournament_selection_pool) < K:
                index = np.random.randint(0, len(self.Pop_list))
                tournament_selection_pool.append(self.Pop_list[index])
                tournament_selection_pool_ordered = sorted(
                    tournament_selection_pool,
                    key=lambda x: x.fitness_value,
                    reverse=True,
                )
            if tournament_selection_pool_ordered[0] not in parents:
                parents.append(tournament_selection_pool_ordered[0])

        return parents
