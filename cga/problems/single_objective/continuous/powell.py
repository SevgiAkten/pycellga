from problems.abstract_problem import AbstractProblem
import numpy as np
class Powell(AbstractProblem):
    """
    Powell function implementation for optimization problems.

    The Powell function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-4, 5], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Powell function value for a given list of variables.

    Notes
    -----
    -4 ≤ xi ≤ 5 for i = 1,…,n
    Global minimum at f(0,....,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Powell function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Powell function value.
        """
        fitness = 0.0
        a = 0.0
        b = 0.0
        c = 0.0
        e = 0.0
        
        d = round(len(x) / 4)

        for i in range(1, d):
            a = np.power((x[4*i - 3] + 10 * x[4*i - 2]), 2)
            b = np.power((x[4*i - 1] - x[4*i]), 2)
            c = np.power((x[4*i - 2] - 2 * x[4*i - 1]), 4)
            e = np.power((x[4*i - 3] - x[4*i]), 4)
            fitness +=  a + 5 * b + c + 10 * e

        return round(fitness, 3)
