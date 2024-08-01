from problems.abstract_problem import AbstractProblem
from numpy import power as pw

class Matyas(AbstractProblem):
    """
    Matyas function implementation for optimization problems.

    The Matyas function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-10, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(X: list) -> float
        Calculates the Matyas function value for a given list of variables.

    Notes
    -----
    -10 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, X: list) -> float:
        """
        Calculate the Matyas function value for a given list of variables.

        Parameters
        ----------
        X : list
            A list of float variables.

        Returns
        -------
        float
            The Matyas function value.
        """
        fitness = 0.0
        for i in range(len(X) - 1):
            fitness += 0.26 * (pw(X[i], 2) + pw(X[i + 1], 2)) - 0.48 * X[i] * X[i + 1]
        return round(fitness, 3)
