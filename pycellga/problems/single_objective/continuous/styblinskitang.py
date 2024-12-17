from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

class StyblinskiTang(AbstractProblem):
    """
    Styblinski-Tang function implementation for optimization problems.

    The Styblinski-Tang function is commonly used to test optimization algorithms. 
    It is defined over the range [-5, 5] for each variable and has a global minimum.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bounds for the variables (fixed to -5).
    xu : float
        Upper bounds for the variables (fixed to 5).

    Methods
    -------
    f(x: list) -> float
        Compute the Styblinski-Tang function value for a given solution.

    Notes
    -----
    -5 ≤ xi ≤ 5 for i = 1,…,n
    Global minimum at f(-2.903534, ..., -2.903534) ≈ -39.16599 * n_var
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Styblinski-Tang function with the specified number of variables.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) in the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -5.0
        xu = 5.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: list) -> float:
        """
        Compute the Styblinski-Tang function value for a given solution.

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

        fitness = sum(xi**4 - 16 * xi**2 + 5 * xi for xi in x) / self.n_var
        return round(fitness, 3)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate function for compatibility with pymoo's optimizer.

        This method wraps the `f` method and allows pymoo to handle batch evaluations
        by storing the computed fitness values in the output dictionary.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
