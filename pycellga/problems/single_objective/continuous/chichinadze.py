import numpy as np
from typing import List
from problems.abstract_problem import AbstractProblem

class Chichinadze(AbstractProblem):
    """
    Chichinadze function implementation for optimization problems.

    The Chichinadze function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x, y ∈ [-30, 30].

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
        Calculates the Chichinadze function value for given variables.
    f(x)
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -30 ≤ x, y ≤ 30
    Global minimum at f(5.90133, 0.5) = −43.3159
    """

    def __init__(self):
        design_variables = ["x", "y"]
        bounds = [(-30, 30), (-30, 30)]
        objectives = ["minimize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Chichinadze function value for a given list of variables.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        x_val, y_val = x[0], x[1]
        term1 = x_val**2 - 12 * x_val + 11
        term2 = 10 * np.cos(np.pi * x_val / 2)
        term3 = 8 * np.sin(5 * np.pi * x_val)
        term4 = (1.0 / np.sqrt(5)) * np.exp(-((y_val - 0.5)**2) / 2)
        fitness = term1 + term2 + term3 - term4

        out["F"] = round(fitness, 4)

    def f(self, x: List[float]) -> float:
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
