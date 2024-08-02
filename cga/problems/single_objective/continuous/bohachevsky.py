from numpy import cos
from numpy import pi
from numpy import power as pw
from cga.problems.abstract_problem import AbstractProblem

class Bohachevsky(AbstractProblem):
    """
    Bohachevsky function implementation for optimization problems.

    The Bohachevsky function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-15, 15], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Bohachevsky function value for a given list of variables.

    Notes
    -----
    -15 ≤ xi ≤ 15 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Bohachevsky function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Bohachevsky function value.
        """
        return round(sum([(pw(x[i], 2) + (2 * pw(x[i + 1], 2)) - (0.3 * cos(3 * pi * x[i])) - (0.4 * cos(4 * pi * x[i + 1])) + 0.7) for i in range(len(x) - 1)]), 3)
