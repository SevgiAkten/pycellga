import numpy as np
from mpmath import power as pw
from problems.abstract_problem import AbstractProblem

class Sumofdifferentpowers(AbstractProblem):
    """
    Sum of Different Powers function implementation for optimization problems.

    The Sum of Different Powers function is often used for testing optimization algorithms.
    It is usually evaluated within the bounds x_i ∈ [-1, 1] for each variable.

    Attributes
    ----------
    n_var : int
        The number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-1, 1), (-1, 1), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Calculates the Sum of Different Powers function value for a given list of variables.

    Notes
    -----
    -1 ≤ xi ≤ 1 for all i.
    Global minimum at f(0,...,0) = 0.
    """

    def __init__(self, design_variables=2):
        bounds = [(-1, 1) for _ in range(design_variables)]
        objectives = ["minimize"]
        super().__init__(design_variables=design_variables, bounds=bounds, objectives=objectives)

    def f(self, x: list) -> float:
        """
        Calculate the Sum of Different Powers function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Sum of Different Powers function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")

        fitness = sum(pw(np.abs(xi), i + 1) for i, xi in enumerate(x))
        return round(fitness, 3)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate method for compatibility with pymoo's framework.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
