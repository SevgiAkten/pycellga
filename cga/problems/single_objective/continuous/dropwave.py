from cga.problems.abstract_problem import AbstractProblem
import math
from numpy import *

# -5.12 ≤ xi ≤ 5.12    i = 1,2
# Global minimum at f(0,0) = −1

class Dropwave(AbstractProblem):
    """
    Dropwave function for optimization problems.

    The Dropwave function is a multimodal function commonly used as a performance test problem for optimization algorithms.
    It is defined within the bounds -5.12 ≤ xi ≤ 5.12 for i = 1, 2, and has a global minimum at f(0, 0) = -1.

    Methods
    -------
    f(x: list) -> float
        Computes the value of the Dropwave function at a given point x.
    """

    def f(self, x: list) -> float:
        """
        Evaluate the Dropwave function at a given point.

        Parameters
        ----------
        x : list
            A list of two floats representing the coordinates [x1, x2].

        Returns
        -------
        float
            The value of the Dropwave function rounded to three decimal places.

        Notes
        -----
        The Dropwave function is defined as:
            f(x1, x2) = - (1 + cos(12 * sqrt(x1^2 + x2^2))) / (0.5 * (x1^2 + x2^2) + 2)
        where x1 and x2 are the input variables.

        Examples
        --------
        >>> dropwave = Dropwave()
        >>> dropwave.f([0, 0])
        -1.0
        >>> dropwave.f([1, 1])
        -0.028
        """
        # Extract the coordinates
        x1 = x[0]
        x2 = x[1]

        # Compute the squared sums
        sqrts_sums = power(x1, 2) + power(x2, 2)
        
        # Compute the denominator term
        b = 0.5 * (sqrts_sums) + 2
        
        # Compute the fitness value
        fitness = -(1 + cos(12 * sqrt(sqrts_sums))) / b

        # Return the fitness value rounded to three decimal places
        return round(fitness, 3)
