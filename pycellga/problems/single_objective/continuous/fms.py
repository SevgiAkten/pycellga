from problems.abstract_problem import AbstractProblem
from numpy import pi, sin
import numpy as np

class Fms(AbstractProblem):
    """
    Fms function implementation for optimization problems.

    The Fms function is used for testing optimization algorithms, specifically those dealing with frequency modulation sound.

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
        Calculates the Fms function value for given variables.
    f(x)
        Alias for evaluate to maintain compatibility with the rest of the codebase.
    """

    def __init__(self):
        design_variables = ["a1", "w1", "a2", "w2", "a3", "w3"]
        bounds = [(-6.4, 6.35)] * 6  # Same bounds for each variable
        objectives = ["minimize"]
        constraints = []
        
        super().__init__(design_variables, bounds, objectives, constraints)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Calculate the Fms function value for a given list of variables.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        theta = (2.0 * pi) / 100.0
        a1, w1, a2, w2, a3, w3 = x

        def yzero(t):
            return sin((5.0 * theta * t) - (1.5 * sin((4.8 * theta * t) + (2.0 * sin(4.9 * theta * t)))))

        partial_fitness = 0.0
        for k in range(101):
            distance = a1 * sin((w1 * theta * k) - (a2 * sin((w2 * theta * k) + (a3 * sin(w3 * theta * k))))) - yzero(k)
            partial_fitness += distance ** 2

        out["F"] = round(partial_fitness, 3)

    def f(self, x):
        """
        Alias for the evaluate method to maintain compatibility with the rest of the codebase.
        """
        result = {}
        self.evaluate(x, result)
        return result["F"]
