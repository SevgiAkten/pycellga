from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
from common import GeneType

class Rothellipsoid(AbstractProblem):
    """
    Rotated Hyper-Ellipsoid function implementation for optimization problems.

    This function is widely used for testing optimization algorithms.
    It is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) for the problem.
    gen_type : GeneType
        The type of genes used in the problem, set to REAL.
    xl : float
        Lower bound for the variables, set to -100.
    xu : float
        Upper bound for the variables, set to 100.

    Methods
    -------
    f(x: list) -> float
        Compute the Rotated Hyper-Ellipsoid function value for a given list of variables.
    evaluate(x, out, *args, **kwargs)
        Computes the fitness value for pymoo compatibility.
    """

    def __init__(self, n_var: int = 3):
        """
        Initialize the Rothellipsoid problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) for the problem, by default 3.
        """
        gen_type = GeneType.REAL
        xl = -100.0
        xu = 100.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x):
        """
        Compute the Rotated Hyper-Ellipsoid function value for a given solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        fitness = sum((i + 1) * pw(x[i], 2) for i in range(len(x)))
        return round(fitness, 3)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate the function for pymoo compatibility.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the computed fitness value.

        Notes
        -----
        Stores the computed fitness value in `out["F"]`.
        """
        out["F"] = self.f(x)
