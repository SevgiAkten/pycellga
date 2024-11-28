from problems.abstract_problem import AbstractProblem
from mpmath import power as pw

class Zettle(AbstractProblem):
    """
    Zettle function implementation for optimization problems.

    The Zettle function is widely used for testing optimization algorithms.
    It is usually evaluated on the hypercube x_i ∈ [-5, 5] for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : int
        The number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-5, 5), (-5, 5), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Calculates the Zettle function value for a given list of variables.

    Notes
    -----
    -5 ≤ xi ≤ 5 for i = 1,…,n
    Global minimum at f(-0.0299, 0) = -0.003791
    """

    def __init__(self, design_variables=2):
        super().__init__(design_variables=design_variables, 
                         bounds=[(-5, 5) for _ in range(design_variables)], 
                         objectives=["minimize"])

    def f(self, x: list) -> float:
        """
        Calculate the Zettle function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Zettle function value, rounded to six decimal places.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        fitness = 0.0
        for i in range(len(x) - 1):
            fitness += pw((pw(x[i], 2) + pw(x[i + 1], 2)) - 2 * x[i], 2) + 0.25 * x[i]
        
        return round(fitness, 6)