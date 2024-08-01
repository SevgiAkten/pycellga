from problems.abstract_problem import AbstractProblem
from numpy import *

class Dropwave(AbstractProblem):
    """
    Dropwave function implementation for optimization problems.

    The Dropwave function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5.12, 5.12], for all i = 1, 2.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Dropwave function value for a given list of variables.

    Notes
    -----
    -5.12 ≤ xi ≤ 5.12 for i = 1,2
    Global minimum at f(0,0) = −1
    """

    def f(self, x: list) -> float:
        """
        Calculate the Dropwave function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Dropwave function value.
        """
        x1 = x[0]
        x2 = x[1]

        sqrts_sums = power(x1, 2) + power(x2, 2)
        b = 0.5 * (sqrts_sums) + 2
        fitness = -(1 + cos(12 * sqrt(sqrts_sums))) / b

        return round(fitness, 3)
