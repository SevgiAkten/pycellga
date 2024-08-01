from numpy import sin, sqrt
from problems.abstract_problem import AbstractProblem

class Schwefel(AbstractProblem):
    """
    Schwefel function implementation for optimization problems.

    The Schwefel function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-500, 500], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Schwefel function value for a given list of variables.

    Notes
    -----
    -500 ≤ xi ≤ 500 for i = 1,…,n
    Global minimum at f(420.9687,…,420.9687) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Schwefel function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Schwefel function value.
        """
        fitness = 0.0
        d = len(x)
        for i in range(d):
            fitness += x[i] * sin(sqrt(abs(x[i])))
        fitness = (418.9829 * d) - fitness

        return round(fitness, 3)
