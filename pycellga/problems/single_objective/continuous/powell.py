from problems.abstract_problem import AbstractProblem
from mpmath import power as pw

class Powell(AbstractProblem):
    """
    Powell function implementation for optimization problems.

    The Powell function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-4, 5], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : int
        The number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-4, 5), (-4, 5), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    evaluate(x, out, *args, **kwargs) -> None
        Calculates the Powell function value and stores in the output dictionary.

    f(x: list) -> float
        Wrapper for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self, design_variables=4):
        bounds = [(-4, 5) for _ in range(design_variables)]
        super().__init__(design_variables=design_variables, bounds=bounds, objectives=["minimize"])

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate the Powell function at a given point.

        Parameters
        ----------
        x : list or numpy array
            Input variables.
        out : dict
            Output dictionary to store the function value.
        """
        fitness = 0.0
        d = len(x) // 4
        
        for i in range(d):
            a = pw(x[4 * i] + 10 * x[4 * i + 1], 2)
            b = pw(x[4 * i + 2] - x[4 * i + 3], 2)
            c = pw(x[4 * i + 1] - 2 * x[4 * i + 2], 4)
            e = pw(x[4 * i] - x[4 * i + 3], 4)
            fitness += a + 5 * b + c + 10 * e

        out["F"] = round(fitness, 1)

    def f(self, x):
        """
        Wrapper for the evaluate method to maintain compatibility.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The computed Powell function value.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
