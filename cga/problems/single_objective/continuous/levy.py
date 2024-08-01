from problems.abstract_problem import AbstractProblem
import math
from numpy import power as pw

class Levy(AbstractProblem):
    """
    Levy function implementation for optimization problems.

    The Levy function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-10, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Levy function value for a given list of variables.

    Notes
    -----
    -10 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(1,1) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Levy function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Levy function value.
        """
        fitness = 0.0
        for i in range(len(x) - 1):
            fitness += (
                pw((math.sin(3 * x[i] * math.pi)), 2) +
                (pw((x[i] - 1), 2)) * (1 + pw((math.sin(3 * x[i + 1] * math.pi)), 2)) +
                (pw((x[i + 1] - 1), 2)) * (1 + pw((math.sin(2 * x[i + 1] * math.pi)), 2))
            )
        return round(fitness, 3)
