from problems.abstract_problem import AbstractProblem
from numpy import pi, sin
from typing import List
from common import GeneType


class Fms(AbstractProblem):
    """
    Fms function implementation for optimization problems.

    The Fms function is used for testing optimization algorithms, specifically those dealing with frequency modulation sound.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem (fixed to 6).
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for the variables (fixed to -6.4).
    xu : float
        Upper bound for the variables (fixed to 6.35).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Fms function value for a single solution.
    """

    def __init__(self):
        """
        Initialize the Fms problem.
        """
        gen_type = GeneType.REAL
        n_var = 6  # Fixed to 6 for [a1, w1, a2, w2, a3, w3]
        xl = -6.4
        xu = 6.35

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Fms function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        theta = (2.0 * pi) / 100.0
        a1, w1, a2, w2, a3, w3 = x

        def yzero(t):
            return sin((5.0 * theta * t) - (1.5 * sin((4.8 * theta * t) + (2.0 * sin(4.9 * theta * t)))))

        partial_fitness = 0.0
        for k in range(101):
            distance = (
                a1 * sin((w1 * theta * k) - (a2 * sin((w2 * theta * k) + (a3 * sin(w3 * theta * k)))))
                - yzero(k)
            )
            partial_fitness += distance ** 2

        return round(partial_fitness, 3)
