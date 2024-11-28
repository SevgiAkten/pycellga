from numpy import pi, e, cos, sqrt, exp,power
from problems.abstract_problem import AbstractProblem

class Ackley(AbstractProblem):
    """
    Ackley function implementation for optimization problems.

    The Ackley function is widely used for testing optimization algorithms.
    It has a nearly flat outer region and a large hole at the center.
    The function is usually evaluated on the hypercube x_i ∈ [-32.768, 32.768], for all i = 1, 2, ..., d.

    Attributes
    ----------
    design_variables : List[str]
        List of variable names.
    bounds : List[Tuple[float, float]]
        Bounds for each variable.
    objectives : List[str]
        Objectives for optimization.
    constraints : List[str]
        Any constraints for the problem.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the Ackley function value for given variables.
    f(x)
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -32.768 ≤ xi ≤ 32.768
    Global minimum at f(0, 0) = 0
    """

    def __init__(self, dimension: int):
        design_variables = [f"x{i+1}" for i in range(dimension)]
        bounds = [(-32.768, 32.768) for _ in range(dimension)]
        objectives = ["minimize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)
        self.dimension = dimension

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Ackley function value for a given list of variables.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        sum1 = sum(power(gene,2) for gene in x)
        sum2 = sum(cos(2 * pi * gene) for gene in x)
        
        fitness = -20.0 * exp(-0.2 * sqrt(sum1 / self.dimension)) - exp(sum2 / self.dimension) + 20.0 + e
        out["F"] = round(fitness, 3)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
