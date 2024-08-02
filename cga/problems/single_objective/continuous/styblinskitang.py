from cga.problems.abstract_problem import AbstractProblem
from numpy import power as pw

class StyblinskiTang(AbstractProblem):
    """
    Styblinski-Tang function implementation for optimization problems.

    The Styblinski-Tang function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 5], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Styblinski-Tang function value for a given list of variables.

    Notes
    -----
    -5 ≤ xi ≤ 5 for i = 1,…,n
    Global minimum at f(−2.903534, −2.903534) = −78.332
    """

    def f(self, x: list) -> float:
        """
        Calculate the Styblinski-Tang function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Styblinski-Tang function value.
        """
        fitness = 0.0
        for i in range(len(x)):
            fitness += (pw(x[i], 4) - 16 * pw(x[i], 2) + 5 * x[i])
        
        fitness = fitness / len(x)
        return round(fitness, 3)
