from cga.problems.abstract_problem import AbstractProblem
from numpy import power as pw

class Pow(AbstractProblem):
    """
    Pow function implementation for optimization problems.

    The Pow function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5.0, 15.0].

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Pow function value for a given list of variables.

    Notes
    -----
    -5.0 ≤ xi ≤ 15.0
    Global minimum at f(5, 7, 9, 3, 2) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Pow function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Pow function value.
        """
        fitness = 0.0
        # Use only the first five dimensions for fitness calculation
        for i in range(min(len(x), 5) - 4):
            fitness += (pw(x[i] - 5, 2) +
                        pw(x[i + 1] - 7, 2) +
                        pw(x[i + 2] - 9, 2) +
                        pw(x[i + 3] - 3, 2) +
                        pw(x[i + 4] - 2, 2))

        return round(fitness, 2)
