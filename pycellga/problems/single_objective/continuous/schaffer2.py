import numpy as np
from numpy import power as pw

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

class Schaffer2(AbstractProblem):
    """
    Modified Schaffer function #2 implementation for optimization problems.

    The Modified Schaffer function #2 is widely used for testing optimization algorithms.
    The function is evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    n_var : int
        The number of variables (dimensions) for the problem.
    gen_type : GeneType
        Type of genes used in the problem, fixed to REAL.
    xl : float
        Lower bounds for the variables, fixed to -100.
    xu : float
        Upper bounds for the variables, fixed to 100.

    Methods
    -------
    f(x: list) -> float
        Compute the Modified Schaffer function #2 value for a single solution.
    evaluate(x, out, *args, **kwargs)
        Compute the fitness value(s) for pymoo's optimization framework.
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Modified Schaffer function #2.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) for the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -100.0
        xu = 100.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: list) -> float:
        """
        Compute the Modified Schaffer function #2 value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        fitness = 0.0
        for i in range(len(x) - 1):
            term1 = np.sin(pw(x[i], 2) - pw(x[i + 1], 2)) ** 2
            term2 = (1 + 0.001 * (pw(x[i], 2) + pw(x[i + 1], 2))) ** 2
            fitness += 0.5 + ((term1 - 0.5) / term2)
        return round(fitness, 3)
