from problems.abstract_problem import AbstractProblem
from mpmath import power as pw


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
        n = len(x)
        d = n // 4
        
        for i in range(d):
            a = pw(x[4*i] + 10 * x[4*i + 1], 2)
            b = pw(x[4*i + 2] - x[4*i + 3], 2)
            c = pw(x[4*i + 1] - 2 * x[4*i + 2], 4)
            e = pw(x[4*i] - x[4*i + 3], 4)
            fitness += a + 5 * b + c + 10 * e

        return round(fitness, 1)
