from problems.abstract_problem import AbstractProblem
import math
from mpmath import power as pw
from typing import List

class Levy(AbstractProblem):
    """
    Levy function implementation for optimization problems.

    The Levy function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-10, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : List[str]
        The names of the design variables.
    bounds : List[Tuple[float, float]]
        The bounds for each variable, typically [(-10, 10), (-10, 10), ...].
    objectives : List[str]
        Objectives for optimization, usually "minimize" for single-objective functions.
    constraints : List[str]
        Any constraints for the optimization problem.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the Levy function value for a given list of variables and stores in `out`.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -10 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(1,1,...,1) = 0
    """

    def __init__(self, dimension: int = 2):
        design_variables = [f"x{i+1}" for i in range(dimension)]
        bounds = [(-10, 10) for _ in range(dimension)]
        objectives = ["minimize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)
        self.dimension = dimension

    def evaluate(self, x: List[float], out, *args, **kwargs):
        """
        Evaluate the Levy function at a given point.

        Parameters
        ----------
        x : list
            A list of float variables.
        out : dict
            Dictionary to store the output fitness value.
        """
        if len(x) != self.dimension:
            raise ValueError(f"Input must have exactly {self.dimension} variables.")

        fitness = 0.0
        for i in range(self.dimension - 1):
            term1 = pw(math.sin(3 * x[i] * math.pi), 2)
            term2 = (pw((x[i] - 1), 2)) * (1 + pw(math.sin(3 * x[i + 1] * math.pi), 2))
            term3 = (pw((x[i + 1] - 1), 2)) * (1 + pw(math.sin(2 * x[i + 1] * math.pi), 2))
            fitness += term1 + term2 + term3

        out["F"] = round(fitness, 3)

    def f(self, x: List[float]) -> float:
        """
        Alias for evaluate to maintain compatibility with the rest of the codebase.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The calculated Levy function value.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
