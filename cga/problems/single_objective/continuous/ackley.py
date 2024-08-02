from numpy import pi, e, cos, sqrt, exp
from cga.problems.abstract_problem import AbstractProblem
class Ackley(AbstractProblem):
    """
    Ackley function implementation for optimization problems.

    The Ackley function is widely used for testing optimization algorithms.
    It has a nearly flat outer region and a large hole at the center.
    The function is usually evaluated on the hypercube x_i ∈ [-32.768, 32.768], for all i = 1, 2, ..., d.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Ackley function value for a given list of variables.

    Notes
    -----
    -32.768 ≤ xi ≤ 32.768
    Global minimum at f(0, 0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Ackley function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Ackley function value.
        """
        sum1 = 0.0
        sum2 = 0.0
        fitness = 0.0

        for i in range(len(x)):
            gene = x[i]
            sum1 += gene * gene
            sum2 += cos(2 * pi * gene)
        
        fitness += -20.0 * exp(-0.2 * sqrt(sum1 / len(x))) - exp(sum2 / len(x)) + 20.0 + e

        return round(fitness, 3)
