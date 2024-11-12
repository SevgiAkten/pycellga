from problems.abstract_problem import AbstractProblem
from mpmath import power as pw

class Rothellipsoid(AbstractProblem):
    """
    Rotated Hyper-Ellipsoid function implementation for optimization problems.

    This function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : int
        Number of variables (dimensions) for the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-100, 100), (-100, 100), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Alias for evaluate, calculates the Rotated Hyper-Ellipsoid function value for a given list of variables.
    evaluate(x, out, *args, **kwargs)
        Pymoo-compatible function for calculating the fitness values and storing them in the `out` dictionary.
    """

    def __init__(self, design_variables=3):
        # Initialize the parameters as required by AbstractProblem
        super().__init__(
            design_variables=[f"x{i+1}" for i in range(design_variables)],
            bounds=[(-100, 100)] * design_variables,
            objectives=["minimize"]
        )

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Rotated Hyper-Ellipsoid function value for pymoo compatibility.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        fitness = 0.0
        for i in range(len(x)):
            fitness += (i + 1) * pw(x[i], 2)
        out["F"] = round(fitness, 3)

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
            The Rotated Hyper-Ellipsoid function value.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
