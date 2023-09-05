from problems.abstract_problem import AbstractProblem
import tsplib95
from math import sqrt
import pandas as pd
from geopy.distance import geodesic

#### berlin52.tsp ########################################
# EDGE_WEIGHT_TYPE: EUC_2D,   use euclidean_dist function
# Length of chromosomes = 52
# Known Best Route = [1, 49, 32, 45, 19, 41, 8, 9, 10, 43, 33, 51, 11, 52, 14, 13, 47, 26, 27, 28, 12, 25, 4, 6, 15, 5, 24, 48, 38, 37, 40, 39, 36, 35, 34, 44, 46, 16, 29, 50, 20, 23, 30, 2, 7, 42, 21, 17, 3, 18, 31, 22]
# Minumum Fitness Value = 7544.3659 some resources its 7442
#########################################################

#### burma14.tsp ########################################
# EDGE_WEIGHT_TYPE: GEO,   use gographical_dist function
# Length of chromosomes = 14
# Known Best Route = []
# Minumum Fitness Value = 3323
#########################################################

#### ulysses16.tsp ######################################
# EDGE_WEIGHT_TYPE: GEO,   use gographical_dist function
# Length of chromosomes = 16
# Known Best Route = [1, 14, 13, 12, 7, 6, 15, 5, 11, 9, 10, 16, 3, 2, 4, 8]
# Minumum Fitness Value = 6859
##########################################################


class Tsp(AbstractProblem):
    def f(self, x: list) -> float:

        with open("burma14.tsp.txt") as fl:
            problem = tsplib95.read(fl)

        nodes = list(problem.node_coords.values())
        node_x = []
        node_y = []

        for i in nodes:
            node_x.append(i[0])
            node_y.append(i[1])

        temp = []
        for i in nodes:
            temp_row = []
            for j in nodes:
                temp_row.append(self.gographical_dist(i, j))
            temp.append(temp_row)

        node_name = []
        for i in range(1, 15):
            node_name.append(i)

        Dist = pd.DataFrame(temp, columns=node_name, index=node_name)

        # objective
        fitness = 0.0

        for i in range(len(x)):
            start_node = x[i]

            if i+1 == len(x):
                end_node = x[0]
            else:
                end_node = x[i+1]
            fitness += Dist[start_node][end_node]

        return round(fitness, 1)

    def euclidean_dist(self, a: list, b: list) -> float:
        dist = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        return round(dist, 1)

    def gographical_dist(self, a: list, b: list) -> float:
        dist = 0.0
        for i in range(len(a)):
            x_city = ([a[0], a[1]])
            y_city = ([b[0], b[1]])
            dist = geodesic(x_city, y_city).km
        return round(dist, 1)
