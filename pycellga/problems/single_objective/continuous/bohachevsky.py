from numpy import cos, pi
from mpmath import power as pw
from typing import List, Dict, Any
from problems.abstract_problem import AbstractProblem

class Bohachevsky(AbstractProblem):
    """
    Bohachevsky function implementation for optimization problems.

    The Bohachevsky function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-15, 15], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : List[str]
        List of variable names.
    bounds : List[Tuple[float, float]]
        Bounds for each variable.
    objectives : List[str]
        Objectives for optimization.
    constraints : List[str]
        Any constraints for the problem.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the Bohachevsky function value for given variables.
    f(x)
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -15 ≤ xi ≤ 15 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, dimension: int):
        design_variables = [f"x{i+1}" for i in range(dimension)]
        bounds = [(-15, 15) for _ in range(dimension)]
        objectives = ["minimize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)
        self.dimension = dimension

    def evaluate(self, x: List[float], out: Dict[str, Any], *args, **kwargs):
        """
        Calculate the Bohachevsky function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        fitness = sum([
            pw(x[i], 2) + (2 * pw(x[i + 1], 2)) 
            - (0.3 * cos(3 * pi * x[i])) 
            - (0.4 * cos(4 * pi * x[i + 1])) + 0.7
            for i in range(len(x) - 1)
        ])
        out["F"] = round(fitness, 3)

    def f(self, x: List[float]) -> float:
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
