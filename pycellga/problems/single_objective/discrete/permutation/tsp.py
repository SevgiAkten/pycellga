from problems.abstract_problem import AbstractProblem
import tsplib95
from math import sqrt
from geopy.distance import geodesic
import os
from typing import List
from common import GeneType


class Tsp(AbstractProblem):
    """
    Represents the Traveling Salesman Problem (TSP).

    This class solves the TSP using geographical distances (GEO) for node coordinates.

    Attributes
    ----------
    gen_type : GeneType
        The type of genes used in the problem (permutation in this case).
    n_var : int
        The number of nodes in the TSP problem.
    xl : int
        The minimum value for each variable (1 in this case, node index starts at 1).
    xu : int
        The maximum value for each variable (number of nodes).
    """

    def __init__(self, n_var: int = 14):
        """
        Initialize the TSP problem with default attributes.

        Parameters
        ----------
        n_var : int, optional
            Number of nodes in the TSP problem (default is 14).
        """
        xl = [1] 
        xu = [14]
        gen_type=GeneType.PERMUTATION

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

        # Load TSP data file
        file_path = os.path.join(os.path.dirname(__file__), "burma14.tsp.txt")
        with open(file_path) as fl:
            self.problem = tsplib95.read(fl)
            self.node_coords = list(self.problem.node_coords.values())

        # Precompute distances
        self.distances = self._compute_distances()

    def _compute_distances(self):
        """
        Precomputes the geographical distances between all node pairs.

        Returns
        -------
        dict
            A dictionary with distances between all node pairs.
        """
        distances = {}
        for i, coord_a in enumerate(self.node_coords):
            distances[i + 1] = {}
            for j, coord_b in enumerate(self.node_coords):
                distances[i + 1][j + 1] = self.geographical_dist(coord_a, coord_b)
        return distances

    def f(self, x: List[int]) -> float:
        """
        Evaluates the fitness of a given chromosome (route) for the TSP.

        Parameters
        ----------
        x : list
            A list representing the route (chromosome), where each element is a node index.

        Returns
        -------
        float
            The total distance of the route, rounded to one decimal place.
        """
        fitness = 0.0
        for i in range(len(x)):
            start_node = x[i]
            end_node = x[(i + 1) % len(x)]
            fitness += self.distances[start_node][end_node]
        return round(fitness, 1)

    def geographical_dist(self, a: List[float], b: List[float]) -> float:
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
        dist = geodesic(a, b).km
        return round(dist, 1)
