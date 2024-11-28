from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
from typing import List
import numpy as np

class Bentcigar(AbstractProblem):
    """
    Bentcigar function implementation for optimization problems.

    The Bentcigar function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

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
        Calculates the Bentcigar function value for given variables.
    f(x)
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -100 ≤ xi ≤ 100 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, dimension: int):
        design_variables = [f"x{i+1}" for i in range(dimension)]
        bounds = [(-100, 100) for _ in range(dimension)]
        objectives = ["minimize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)
        self.dimension = dimension

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Bentcigar function value for a given list of variables.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        a = pw(x[0], 2)
        b = pw(10, 6)
        sum_val = sum(pw(xi, 2) for xi in x[1:])
        
        fitness = a + (b * sum_val)
        out["F"] = round(fitness, 3)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
