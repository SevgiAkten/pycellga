from problems.abstract_problem import AbstractProblem
from mpmath import power as pw

class Matyas(AbstractProblem):
    """
    Matyas function implementation for optimization problems.

    The Matyas function is commonly used to evaluate the performance of optimization algorithms.
    It is a simple, continuous, convex function that has a global minimum at the origin.
    
    Attributes
    ----------
    design_variables : list of str
        The names of the design variables, typically ["x1", "x2"] for 2 variables.
    bounds : list of tuple
        The bounds for each variable, typically [(-10, 10), (-10, 10)].
    objectives : list of str
        The objectives for optimization, set to ["minimize"].

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Computes the Matyas function value for a given list of variables.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self):
        design_variables = ["x1", "x2"]
        bounds = [(-10, 10), (-10, 10)]
        objectives = ["minimize"]

        super().__init__(design_variables=design_variables, bounds=bounds, objectives=objectives)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Matyas function value for a given list of variables.

        Parameters
        ----------
        x : list of float
            A list of float variables representing a point in the solution space.
        out : dict
            Dictionary to store the output fitness value with key "F".
        """
        if len(x) != 2:
            raise ValueError("Matyas function is defined for exactly 2 variables.")

        x1, x2 = x
        fitness = 0.26 * (pw(x1, 2) + pw(x2, 2)) - 0.48 * x1 * x2
        out["F"] = round(fitness, 2)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
