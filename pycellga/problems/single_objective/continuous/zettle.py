from problems.abstract_problem import AbstractProblem
from mpmath import power as pw

class Zettle(AbstractProblem):
    """
    Zettle function implementation for optimization problems.

    The Zettle function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 5], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Zettle function value for a given list of variables.

    Notes
    -----
    -5 ≤ xi ≤ 5 for i = 1,…,n
    Global minimum at f(−0.0299, 0) = −0.003791
    """

    def f(self, x: list) -> float:
        """
        Calculate the Zettle function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Zettle function value.
        """
        fitness = 0.0
        for i in range(len(x) - 1):
            fitness += pw((pw(x[i], 2) + pw(x[i + 1], 2)) - 2 * x[i], 2) + 0.25 * x[i]
        return round(fitness, 6)
