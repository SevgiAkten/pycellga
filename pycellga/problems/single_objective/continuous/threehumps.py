from mpmath import power as pw
from problems.abstract_problem import AbstractProblem

class Threehumps(AbstractProblem):
    """
    Three Hump Camel function implementation for optimization problems.

    The Three Hump Camel function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 5], for all i = 1, 2, ..., n.

    Attributes
    ----------
    bounds : list of tuple
        Bounds for each variable, set to [(-5, 5), (-5, 5)] for this function.
    design_variables : int
        Number of variables for this problem, which is 2.
    objectives : int
        Number of objectives, which is 1 for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Calculates the Three Hump Camel function value for a given list of variables.
    """

    def __init__(self):
        super().__init__(design_variables=2, bounds=[(-5, 5), (-5, 5)], objectives=["minimize"])

    def f(self, x: list) -> float:
        """
        Calculate the Three Hump Camel function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Three Hump Camel function value.
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
