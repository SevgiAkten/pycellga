from cga.problems.abstract_problem import AbstractProblem
import numpy as np

class Sumofdifferentpowers(AbstractProblem):
    """
    Sum of Different Powers function implementation for optimization problems.

    The Sum of Different Powers function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-10, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Sum of Different Powers function value for a given list of variables.

    Notes
    -----
    -10 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(0,....,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Sum of Different Powers function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Sum of Different Powers function value.
        """
        fitness = 0.0

        for i in range(1, len(x)):
            a = np.abs(x[i - 1])
            b = i + 1
            fitness += np.power(a, b)

        return round(fitness, 3)