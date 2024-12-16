from mpmath import power as pw
from problems.abstract_problem import AbstractProblem
from common import GeneType


class Threehumps(AbstractProblem):
    """
    Three Hump Camel function implementation for optimization problems.

    The Three Hump Camel function is commonly used for testing optimization algorithms.
    It is defined for two variables within the bounds [-5, 5].

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) for the problem, fixed to 2.
    gen_type : GeneType
        Type of genes used in the problem (REAL).
    xl : float
        Lower bounds for the variables, fixed to -5.
    xu : float
        Upper bounds for the variables, fixed to 5.

    Methods
    -------
    f(x: list) -> float
        Compute the Three Hump Camel function value for a given solution.
    """

    def __init__(self):
        """
        Initialize the Three Hump Camel problem.
        """
        gen_type = GeneType.REAL
        n_var = 2
        xl = -5.0
        xu = 5.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: list) -> float:
        """
        Compute the Three Hump Camel function value for a given solution.

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
        
        x1, x2 = x
        fitness = 2 * pw(x1, 2) - 1.05 * pw(x1, 4) + (pw(x1, 6) / 6) + x1 * x2 + pw(x2, 2)
        return round(fitness, 6)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate method for compatibility with pymoo's framework.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
