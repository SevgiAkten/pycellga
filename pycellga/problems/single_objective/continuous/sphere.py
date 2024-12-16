from problems.abstract_problem import AbstractProblem
from common import GeneType

class Sphere(AbstractProblem):
    """
    Sphere function implementation for optimization problems.

    The Sphere function is a simple and commonly used benchmark for optimization algorithms.
    It is defined on a hypercube where each variable typically lies within [-5.12, 5.12].

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bounds for the variables (fixed to -5.12).
    xu : float
        Upper bounds for the variables (fixed to 5.12).

    Methods
    -------
    f(x: list) -> float
        Compute the Sphere function value for a single solution.

    Notes
    -----
    -5.12 ≤ xi ≤ 5.12 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, n_var: int = 10):
        """
        Initialize the Sphere function with the specified number of variables.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) in the problem, by default 10.
        """
        gen_type = GeneType.REAL
        xl = -5.12
        xu = 5.12

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: list) -> float:
        """
        Compute the Sphere function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")

        fitness = sum(xi**2 for xi in x)
        return round(fitness, 3)
