from cga.problems.abstract_problem import AbstractProblem
from numpy import power as pw

class Holzman(AbstractProblem):
    """
    Holzman function implementation for optimization problems.

    The Holzman function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-10, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Holzman function value for a given list of variables.

    Notes
    -----
    -10 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Holzman function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Holzman function value.
        """
        fitness = 0.0
        for i in range(len(x)):
            fitness += (i + 1) * pw(x[i], 4)
        return round(fitness, 3)
