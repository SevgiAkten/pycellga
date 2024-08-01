from problems.abstract_problem import AbstractProblem
import math

class Griewank(AbstractProblem):
    """
    Griewank function implementation for optimization problems.

    The Griewank function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-600, 600], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(X: list) -> float
        Calculates the Griewank function value for a given list of variables.

    Notes
    -----
    -600 ≤ xi ≤ 600 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, X: list) -> float:
        """
        Calculate the Griewank function value for a given list of variables.

        Parameters
        ----------
        X : list
            A list of float variables.

        Returns
        -------
        float
            The Griewank function value.
        """
        sum = 0
        for x in X:
            sum += x * x

        fitness = 1
        for i in range(len(X)):
            fitness *= math.cos(X[i] / math.sqrt(i + 1))

        return round((1 + sum / 4000 - fitness), 3)
