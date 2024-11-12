from problems.abstract_problem import AbstractProblem
import tsplib95
from math import sqrt
from geopy.distance import geodesic
import os
from typing import List, Tuple

class Tsp(AbstractProblem):
    """
    Represents the Traveling Salesman Problem (TSP).

    This class solves the TSP using geographical distances (GEO) for node coordinates.

    Attributes
    ----------
    design_variables : list
        Names of the design variables (nodes in this case).
    bounds : list of tuples
        Bounds for each design variable as (min, max).
    objectives : list
        Objectives for optimization, e.g., "minimize" or "maximize".
    constraints : list
        Constraints for the optimization problem.

    Notes
    -----
    - Uses geographical distance function (GEO) for evaluating routes.
    - Example problem: burma14.tsp, with a known minimum distance.
    """

    def __init__(self):
        """
        Initialize the TSP problem with default attributes.

        Uses the 'burma14' TSP dataset as an example with 14 nodes.
        """
        design_variables = ["node" + str(i) for i in range(1, 15)]
        bounds = [(1, 14) for _ in range(14)]  # Nodes range from 1 to 14
        objectives = ["minimize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)

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
        # Load TSP data file
        file_path = os.path.join(os.path.dirname(__file__), 'burma14.tsp.txt')
        with open(file_path) as fl:
            problem = tsplib95.read(fl)

        nodes = list(problem.node_coords.values())

        # Compute distances between all pairs of nodes
        temp = []
        for i in nodes:
            temp_row = []
            for j in nodes:
                temp_row.append(self.gographical_dist(i, j))
            temp.append(temp_row)

        # Dictionary of distances between nodes
        node_name = list(range(1, 15))
        Dist = {row_name: {col_name: temp[i][j] for j, col_name in enumerate(node_name)} 
                for i, row_name in enumerate(node_name)}

        # Calculate total route distance
        fitness = 0.0
        for i in range(len(x)):
            start_node = x[i]
            end_node = x[(i + 1) % len(x)]
            fitness += Dist[start_node][end_node]

        return round(fitness, 1)

    def euclidean_dist(self, a: List[float], b: List[float]) -> float:
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

    def gographical_dist(self, a: List[float], b: List[float]) -> float:
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
