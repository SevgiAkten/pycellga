from cga.problems.abstract_problem import AbstractProblem

class Sphere(AbstractProblem):
    """
    Sphere function implementation for optimization problems.

    The Sphere function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5.12, 5.12], for all i = 1, 2, ..., n.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Sphere function value for a given list of variables.

    Notes
    -----
    -5.12 ≤ xi ≤ 5.12 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def f(self, x: list) -> float:
        """
        Calculate the Sphere function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Sphere function value.
        """
        return round(sum([i * i for i in x]), 3)
