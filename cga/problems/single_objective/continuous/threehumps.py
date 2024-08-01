from problems.abstract_problem import AbstractProblem
from numpy import power as pw

class Threehumps(AbstractProblem):
    """
    Three Hump Camel function implementation for optimization problems.

    The Three Hump Camel function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 5], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Three Hump Camel function value for a given list of variables.

    Notes
    -----
    -5 ≤ xi ≤ 5 for i = 1,…,n
    Global minimum at f(0,..,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Three Hump Camel function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Three Hump Camel function value.
        """
        fitness = 0.0
        for i in range(len(x) - 1):
            fitness += (2 * pw(x[i], 2) - 1.05 * pw(x[i], 4) + (pw(x[i], 6) / 6) + 
                        (x[i] * x[i + 1]) + pw(x[i + 1], 2))
        return round(fitness, 6)
