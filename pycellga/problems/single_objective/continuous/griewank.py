from problems.abstract_problem import AbstractProblem
import math
from typing import List

class Griewank(AbstractProblem):
    """
    Griewank function implementation for optimization problems.

    The Griewank function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-600, 600], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : List[str]
        Names of the design variables.
    bounds : List[Tuple[float, float]]
        Bounds for each design variable.
    objectives : List[str]
        Objectives for optimization, typically ["minimize"].
    constraints : List[str]
        Any constraints for the optimization problem.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Evaluates the Griewank function value for a given list of variables.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -600 ≤ xi ≤ 600 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, dimensions=10):
        """
        Initialize the Griewank function with the specified number of dimensions.

        Parameters
        ----------
        dimensions : int, optional
            The number of dimensions (design variables) for the Griewank function, by default 10.
        """
        design_variables = [f"x{i+1}" for i in range(dimensions)]
        bounds = [(-600, 600)] * dimensions
        objectives = ["minimize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)
        self.dimensions = dimensions

    def evaluate(self, x: List[float], out, *args, **kwargs):
        """
        Calculate the Griewank function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.
        out : dict
            Dictionary to store the output fitness value.
        """
        sum_sq = sum(xi ** 2 for xi in x)
        prod_cos = math.prod(math.cos(xi / math.sqrt(i + 1)) for i, xi in enumerate(x))
        fitness = 1 + sum_sq / 4000 - prod_cos
        out["F"] = round(fitness, 3)

    def f(self, x: List[float]) -> float:
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Griewank function value.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
