import numpy as np
from numpy import power as pw
from problems.abstract_problem import AbstractProblem

class Schaffer2(AbstractProblem):
    """
    Modified Schaffer function #2 implementation for optimization problems.

    The Modified Schaffer function #2 is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : int
        The number of design variables.
    bounds : list of tuple
        The bounds for each variable, typically [(-100, 100), (-100, 100), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Evaluates the Modified Schaffer function #2 value for a given list of variables.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self, design_variables=2):
        super().__init__(design_variables=[f"x{i+1}" for i in range(design_variables)],
                         bounds=[(-100, 100)] * design_variables,
                         objectives=["minimize"])

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate the Modified Schaffer function #2 value for a given list of variables.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        fitness = 0.0
        for i in range(len(x) - 1):
            term1 = np.sin(pw(x[i], 2) - pw(x[i + 1], 2)) ** 2
            term2 = (1 + 0.001 * (pw(x[i], 2) + pw(x[i + 1], 2))) ** 2
            fitness += 0.5 + ((term1 - 0.5) / term2)
        out["F"] = round(fitness, 3)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
