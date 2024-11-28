from numpy import cos, pi
from problems.abstract_problem import AbstractProblem

class Rastrigin(AbstractProblem):
    """
    Rastrigin function implementation for optimization problems.

    The Rastrigin function is widely used for testing optimization algorithms.
    It is typically evaluated on the hypercube x_i ∈ [-5.12, 5.12], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : int
        The number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-5.12, 5.12), (-5.12, 5.12), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Calculates the Rastrigin function value for a given list of variables.

    Notes
    -----
    -5.12 ≤ xi ≤ 5.12 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, design_variables=2):
        """
        Initialize the Rastrigin problem with the specified number of variables.

        Parameters
        ----------
        design_variables : int, optional
            The number of design variables, by default 2.
        """
        self.design_variables = design_variables
        self.bounds = [(-5.12, 5.12) for _ in range(design_variables)]
        self.objectives = 1

    def f(self, x: list) -> float:
        """
        Calculate the Rastrigin function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Rastrigin function value.
        """
        if len(x) != self.design_variables:
            raise ValueError(f"Input must have exactly {self.design_variables} variables.")

        A = 10.0
        fitness = (A * self.design_variables) + sum([(xi ** 2) - (A * cos(2 * pi * xi)) for xi in x])
        return round(fitness, 3)
