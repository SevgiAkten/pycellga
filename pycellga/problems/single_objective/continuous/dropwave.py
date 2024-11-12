from problems.abstract_problem import AbstractProblem
from numpy import power, cos, sqrt

class Dropwave(AbstractProblem):
    """
    Dropwave function for optimization problems.

    The Dropwave function is a multimodal function commonly used as a performance test problem for optimization algorithms.
    It is defined within the bounds -5.12 ≤ xi ≤ 5.12 for i = 1, 2, and has a global minimum at f(0, 0) = -1.

    Attributes
    ----------
    design_variables : list
        The names of the variables, in this case ["x1", "x2"].
    bounds : list of tuples
        The lower and upper bounds for each variable, [-5.12, 5.12] for both x1 and x2.
    objectives : list
        List defining the optimization objective, which is to "minimize" for this function.
    num_variables : int
        The number of variables (dimensions) for the function, which is 2 in this case.

    Methods
    -------
    evaluate(x, out, *args, **kwargs)
        Calculates the value of the Dropwave function at a given point x.
    f(x)
        Alias for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self):
        # Dropwave problem-specific parameters
        design_variables = ["x1", "x2"]
        bounds = [(-5.12, 5.12), (-5.12, 5.12)]
        objectives = ["minimize"]

        # Initialize the AbstractProblem with specific parameters
        super().__init__(design_variables, bounds, objectives)
        self.num_variables = 2

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Dropwave function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of two floats representing the coordinates [x1, x2].
        out : dict
            Dictionary to store the output fitness values.

        Notes
        -----
        The Dropwave function is defined as:
            f(x1, x2) = - (1 + cos(12 * sqrt(x1^2 + x2^2))) / (0.5 * (x1^2 + x2^2) + 2)
        where x1 and x2 are the input variables.
        """
        if len(x) != self.num_variables:
            raise ValueError(f"Input must have exactly {self.num_variables} variables.")
        
        x1, x2 = x
        sqrts_sums = power(x1, 2) + power(x2, 2)
        denominator = 0.5 * sqrts_sums + 2
        fitness = -(1 + cos(12 * sqrt(sqrts_sums))) / denominator
        out["F"] = round(fitness, 3)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
