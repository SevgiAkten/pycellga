from numpy import cos, pi
from cga.problems.abstract_problem import AbstractProblem
class Rastrigin(AbstractProblem):
    """
    Rastrigin function implementation for optimization problems.

    The Rastrigin function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5.12, 5.12], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Rastrigin function value for a given list of variables.

    Notes
    -----
    -5.12 ≤ xi ≤ 5.12 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Rastrigin function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Rastrigin function value.
        """
        A = 10.0
        return round((A * len(x)) + sum([(i * i) - (A * cos(2 * pi * i)) for i in x]), 3)
