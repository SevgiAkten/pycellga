from problems.abstract_problem import AbstractProblem
from numpy import power as pw

class Bentcigar(AbstractProblem):
    """
    Bentcigar function implementation for optimization problems.

    The Bentcigar function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(X: list) -> float
        Calculates the Bentcigar function value for a given list of variables.

    Notes
    -----
    -100 ≤ xi ≤ 100 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, X: list) -> float:
        """
        Calculate the Bentcigar function value for a given list of variables.

        Parameters
        ----------
        X : list
            A list of float variables.

        Returns
        -------
        float
            The Bentcigar function value.
        """
        a = pw(X[0], 2)
        b = pw(10, 6)
        sum = 0.0
        for i in range(1, len(X)):
            sum += pw(X[i], 2)
        
        fitness = a + (b * sum)
        return round(fitness, 3)
