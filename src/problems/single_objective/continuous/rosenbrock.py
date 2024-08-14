from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
class Rosenbrock(AbstractProblem):
    """
    Rosenbrock function implementation for optimization problems.

    The Rosenbrock function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Rosenbrock function value for a given list of variables.

    Notes
    -----
    -5 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(1,...,1) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Rosenbrock function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Rosenbrock function value.
        """
        return round(sum([(100 * (pw((x[i + 1] - pw(x[i], 2)), 2))) + pw((1 - x[i]), 2) for i in range(len(x) - 1)]), 3)
