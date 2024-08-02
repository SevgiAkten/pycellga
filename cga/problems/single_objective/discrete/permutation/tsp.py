from cga.problems.abstract_problem import AbstractProblem
import tsplib95
from math import sqrt
import pandas as pd
from geopy.distance import geodesic
import os

class Tsp(AbstractProblem):
    """
    Represents the Traveling Salesman Problem (TSP).

    This class solves the TSP using geographical distances (GEO) for node coordinates.

    Notes
    ----------
    #### burma14.tsp ########################################
    # EDGE_WEIGHT_TYPE: GEO,   use gographical_dist function
    # Length of chromosomes = 14
    # Known Best Route = []
    # Minumum Fitness Value = 3323
    #########################################################
    """

    def f(self, x: list) -> float:
        """
        Evaluates the fitness of a given chromosome (route) for the TSP.

        This method calculates the total distance of the given route using geographical distances.

        Parameters
        ----------
        x : list
            A list representing the route (chromosome), where each element is a node index.

        Returns
        -------
        float
            The total distance of the route, rounded to one decimal place.
        """
   

        file_path = os.path.join(os.path.dirname(__file__), 'burma14.tsp.txt')
        with open(file_path) as fl:
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
        """
        Computes the Euclidean distance between two nodes.

        Parameters
        ----------
        a : list
            Coordinates of the first node.
        b : list
            Coordinates of the second node.

        Returns
        -------
        float
            The Euclidean distance between the two nodes, rounded to one decimal place.
        """
        dist = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        return round(dist, 1)

    def gographical_dist(self, a: list, b: list) -> float:
        """
        Computes the geographical distance between two nodes using the geodesic distance.

        Parameters
        ----------
        a : list
            Coordinates of the first node.
        b : list
            Coordinates of the second node.

        Returns
        -------
        float
            The geographical distance between the two nodes, rounded to one decimal place.
        """
        dist = 0.0
        for i in range(len(a)):
            x_city = ([a[0], a[1]])
            y_city = ([b[0], b[1]])
            dist = geodesic(x_city, y_city).km
        return round(dist, 1)
