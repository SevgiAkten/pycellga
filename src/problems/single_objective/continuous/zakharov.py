from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
class Zakharov(AbstractProblem):
    """
    Zakharov function implementation for optimization problems.

    The Zakharov function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Zakharov function value for a given list of variables.

    Notes
    -----
    -5 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(0,..,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Zakharov function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Zakharov function value.
        """
        fitness1 = 0.0
        fitness2 = 0.0
        fitness3 = 0.0
        fitness = 0.0
        
        for i in range(len(x)):
            fitness1 += pw(x[i], 2)

        for i in range(len(x)):
            fitness2 += 0.5 * (i + 1) * x[i]
        fitness2 = pw(fitness2, 2)

        for i in range(len(x)):
            fitness3 += 0.5 * (i + 1) * x[i]
        fitness3 = pw(fitness3, 4)

        fitness = fitness1 + fitness2 + fitness3

        return round(fitness, 3)
