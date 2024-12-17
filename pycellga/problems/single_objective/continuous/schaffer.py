import numpy as np

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

class Schaffer(AbstractProblem):
    """
    Modified Schaffer function #1 for optimization problems.

    This class implements the Schaffer's function, a common benchmark problem for optimization algorithms.
    The function is defined over a multidimensional input and is used to test the performance of optimization methods.

    Attributes
    ----------
    gen_type : GeneType
        The type of gene, set to REAL.
    n_var : int
        The number of design variables.
    xl : float
        The lower bound for the design variables, set to -100.
    xu : float
        The upper bound for the design variables, set to 100.

    Methods
    -------
    f(x: list) -> float
        Computes the Schaffer's function value for a given list of variables.
    evaluate(x, out, *args, **kwargs)
        Wrapper for pymoo compatibility to calculate the fitness value.
    """

    def __init__(self, n_var=2):
        """
        Initialize the Schaffer's problem.

        Parameters
        ----------
        n_var : int, optional
            The number of design variables, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -100.0
        xu = 100.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x):
        """
        Compute the Schaffer's function value for a given solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The calculated fitness value.
        """
        fitness = 0.0
        for i in range(len(x) - 1):
            xi = x[i]
            xi1 = x[i + 1]
            term1 = np.sin(xi**2 + xi1**2)**2
            term2 = 1 + 0.001 * (xi**2 + xi1**2)
            fitness += 0.5 + (term1 - 0.5)**2 / term2**2
        return round(fitness, 3)
