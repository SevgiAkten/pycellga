from numpy import sin, sqrt, abs

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

class Schwefel(AbstractProblem):
    """
    Schwefel function implementation for optimization problems.

    The Schwefel function is commonly used for testing optimization algorithms.
    It is evaluated on the range [-500, 500] for each variable and has a global minimum
    at f(420.9687,...,420.9687) = 0.

    Attributes
    ----------
    n_var : int
        The number of variables (dimensions) for the problem.
    gen_type : GeneType
        The type of genes used in the problem, fixed to REAL.
    xl : float
        The lower bounds for the variables, fixed to -500.
    xu : float
        The upper bounds for the variables, fixed to 500.

    Methods
    -------
    f(x: list) -> float
        Compute the Schwefel function value for a single solution.

    Notes
    -----
    -500 ≤ xi ≤ 500 for i = 1,…,n
    Global minimum at f(420.9687,...,420.9687) = 0
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Schwefel function with the specified number of variables.

        Parameters
        ----------
        n_var : int, optional
            The number of variables (dimensions) for the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -500.0
        xu = 500.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: list) -> float:
        """
        Compute the Schwefel function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        d = len(x)
        fitness = sum(xi * sin(sqrt(abs(xi))) for xi in x)
        return round((418.9829 * d) - fitness, 3)
