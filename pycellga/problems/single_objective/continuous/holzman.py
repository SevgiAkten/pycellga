from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
from typing import List

class Holzman(AbstractProblem):
    """
    Holzman function implementation for optimization problems.

    The Holzman function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-10, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : List[str]
        Names of the design variables.
    bounds : List[Tuple[float, float]]
        Bounds for each variable.
    objectives : List[str]
        Objectives for optimization.
    constraints : List[str]
        Any constraints for the problem.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the Holzman function value for given variables.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -10 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, design_variables: int = 2):
        var_names = [f"x{i+1}" for i in range(design_variables)]
        bounds = [(-10, 10) for _ in range(design_variables)]
        objectives = ["minimize"]
        constraints = []

        super().__init__(var_names, bounds, objectives, constraints)
        self.design_variables = design_variables

    def evaluate(self, x: List[float], out, *args, **kwargs):
        """
        Calculate the Holzman function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.
        out : dict
            Dictionary to store the output fitness value.
        """
        fitness = sum((i + 1) * pw(x[i], 4) for i in range(len(x)))
        out["F"] = round(fitness, 3)

    def f(self, x: List[float]) -> float:
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
