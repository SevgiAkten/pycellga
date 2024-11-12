from numpy import sin, sqrt
from problems.abstract_problem import AbstractProblem

class Schwefel(AbstractProblem):
    """
    Schwefel function implementation for optimization problems.

    This function is commonly used for testing optimization algorithms and is evaluated on the range
    [-500, 500] for each variable.

    Attributes
    ----------
    design_variables : int
        The number of variables in the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-500, 500), (-500, 500), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the Schwefel function value for a given list of variables, compatible with pymoo.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self, design_variables=2):
        bounds = [(-500, 500) for _ in range(design_variables)]
        super().__init__(design_variables=design_variables, bounds=bounds, objectives=1)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Schwefel function value for a given list of variables.

        Parameters
        ----------
        x : numpy.ndarray
            A numpy array of float variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        d = len(x)
        fitness = sum(xi * sin(sqrt(abs(xi))) for xi in x)
        out["F"] = round((418.9829 * d) - fitness, 3)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Schwefel function value.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
