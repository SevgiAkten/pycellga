import numpy as np
from mpmath import power as pw
from problems.abstract_problem import AbstractProblem

class Schaffer(AbstractProblem):
    """
    Schaffer's Function for optimization problems.

    This class implements the Schaffer's function, a common benchmark problem for optimization algorithms.
    The function is defined over a multidimensional input and is used to test the performance of optimization methods.

    Attributes
    ----------
    design_variables : int
        The number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable, typically set to [(-100, 100), (-100, 100), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the Schaffer's function value for compatibility with pymoo.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self, design_variables=2):
        super().__init__(
            design_variables=[f"x{i+1}" for i in range(design_variables)],
            bounds=[(-100, 100) for _ in range(design_variables)],
            objectives=["minimize"]
        )
        self.design_variables_count = design_variables

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate the Schaffer's function for a given point using pymoo compatibility.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness value.
        """
        fitness = 0.0
        for i in range(len(x) - 1):
            xi = x[i]
            xi1 = x[i + 1]
            term1 = np.sin(xi**2 + xi1**2)**2
            term2 = 1 + 0.001 * (xi**2 + xi1**2)
            fitness += 0.5 + (term1 - 0.5)**2 / term2**2
        out["F"] = round(fitness, 3)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
