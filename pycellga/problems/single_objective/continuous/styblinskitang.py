from problems.abstract_problem import AbstractProblem
from mpmath import power as pw

class StyblinskiTang(AbstractProblem):
    """
    Styblinski-Tang function implementation for optimization problems.

    The Styblinski-Tang function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 5], for all i = 1, 2, ..., n.
    """

    def __init__(self, design_variables=2):
        """
        Initializes the Styblinski-Tang function with specified design variables and bounds.
        
        Parameters
        ----------
        design_variables : int, optional
            Number of variables for the function, by default 2.
        """
        super().__init__(design_variables=design_variables, bounds=[(-5, 5)] * design_variables, objectives=["minimize"])

    def f(self, x: list) -> float:
        """
        Calculate the Styblinski-Tang function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Styblinski-Tang function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        fitness = sum(pw(xi, 4) - 16 * pw(xi, 2) + 5 * xi for xi in x)
        fitness /= self.n_var
        return round(fitness, 3)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate function for compatibility with pymoo's optimizer.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
