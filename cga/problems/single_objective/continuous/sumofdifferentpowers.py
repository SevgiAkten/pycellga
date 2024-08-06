import numpy as np
from cga.problems.abstract_problem import AbstractProblem

class Sumofdifferentpowers(AbstractProblem):
    """
    Sum of Different Powers function implementation for optimization problems.
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

        for i in range(len(x)):
            a = np.abs(x[i])
            b = i + 1
            fitness += np.power(a, b)

        return round(fitness, 3)
