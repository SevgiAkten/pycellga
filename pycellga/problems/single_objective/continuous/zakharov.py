from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
from typing import List, Any

class Zakharov(AbstractProblem):
    """
    Zakharov function implementation for optimization problems.

    The Zakharov function is commonly used to test optimization algorithms.
    It evaluates inputs over the hypercube x_i ∈ [-5, 10].

    Attributes
    ----------
    design_variables : int
        The number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-5, 10), (-5, 10), ...].
    objectives : list
        Objectives for the problem, set to ["minimize"] for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Calculates the Zakharov function value for a given list of variables.
    """

    def __init__(self, design_variables=2):
        bounds = [(-5, 10) for _ in range(design_variables)]
        objectives = ["minimize"]
        super().__init__(design_variables=design_variables, bounds=bounds, objectives=objectives)

    def f(self, x: List[float]) -> float:
        """
        Calculate the Zakharov function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Zakharov function value.
        """
        fitness1 = sum(pw(xi, 2) for xi in x)
        fitness2 = pw(sum(0.5 * (i + 1) * xi for i, xi in enumerate(x)), 2)
        fitness3 = pw(sum(0.5 * (i + 1) * xi for i, xi in enumerate(x)), 4)
        fitness = fitness1 + fitness2 + fitness3
        return round(fitness, 3)

    def evaluate(self, x: List[float], out: dict, *args: Any, **kwargs: Any) -> None:
        """
        Evaluate function for compatibility with pymoo's optimizer.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
