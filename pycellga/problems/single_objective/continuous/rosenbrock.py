from problems.abstract_problem import AbstractProblem
from mpmath import power as pw

class Rosenbrock(AbstractProblem):
    """
    Rosenbrock function implementation for optimization problems.

    The Rosenbrock function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    design_variables : int
        Number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable, typically [(-5, 10), (-5, 10), ...].
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Evaluates the Rosenbrock function value for a given list of variables.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.

    Notes
    -----
    -5 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(1,...,1) = 0
    """

    def __init__(self, design_variables=2):
        self.design_variables = design_variables
        bounds = [(-5, 10) for _ in range(design_variables)]
        super().__init__(design_variables=[f"x{i+1}" for i in range(design_variables)], bounds=bounds, objectives=["minimize"])

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Rosenbrock function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        fitness = sum([(100 * pw((x[i + 1] - pw(x[i], 2)), 2)) + pw((1 - x[i]), 2) for i in range(len(x) - 1)])
        out["F"] = round(fitness, 3)

    def f(self, x: list) -> float:
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Rosenbrock function value.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
