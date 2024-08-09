from problems.abstract_problem import AbstractProblem
import numpy as np

class Rothellipsoid(AbstractProblem):
    """
    Rotated Hyper-Ellipsoid function implementation for optimization problems.

    The Rotated Hyper-Ellipsoid function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Rotated Hyper-Ellipsoid function value for a given list of variables.

    Notes
    -----
    -100 ≤ xi ≤ 100 for i = 1,…,n
    Global minimum at f(0,....,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Rotated Hyper-Ellipsoid function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Rotated Hyper-Ellipsoid function value.
        """
        fitness = 0.0
        n = len(x)

        for i in range(n):
            fitness += (i + 2) * np.power(x[i], 2)

        return round(fitness, 3)
