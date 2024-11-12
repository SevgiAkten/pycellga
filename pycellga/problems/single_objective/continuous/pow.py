from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
from typing import List, Tuple

class Pow(AbstractProblem):
    """
    Pow function implementation for optimization problems.

    The Pow function is typically used for testing optimization algorithms.
    It is evaluated on the hypercube x_i ∈ [-5.0, 15.0] with the goal of reaching 
    the global minimum at f(5, 7, 9, 3, 2) = 0.

    Attributes
    ----------
    design_variables : List[str]
        The names of the design variables.
    bounds : List[Tuple[float, float]]
        The bounds for each variable, typically [(-5.0, 15.0) for each dimension].
    objectives : List[str]
        Objectives for optimization, e.g., "minimize".

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the Pow function value for compatibility with Pymoo's optimizer.
    f(x: list) -> float
        Alias for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self, design_variables=5):
        # Define design variable names
        design_variable_names = [f"x{i+1}" for i in range(design_variables)]
        bounds = [(-5.0, 15.0) for _ in range(design_variables)]
        objectives = ["minimize"]

        # Initialize the AbstractProblem
        super().__init__(design_variable_names, bounds, objectives)
        self.design_variables = design_variables

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Pow function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables representing the point in the solution space.
        out : dict
            Dictionary to store the output fitness values.
        """
        if len(x) != self.design_variables:
            raise ValueError(f"Input must have exactly {self.design_variables} variables.")

        fitness = (pw(x[0] - 5, 2) +
                   pw(x[1] - 7, 2) +
                   pw(x[2] - 9, 2) +
                   pw(x[3] - 3, 2) +
                   pw(x[4] - 2, 2))

        out["F"] = round(fitness, 2)

    def f(self, x: List[float]) -> float:
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Pow function value.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
