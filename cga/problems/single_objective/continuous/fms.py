from cga.problems.abstract_problem import AbstractProblem
from numpy import pi, sin, random

class Fms(AbstractProblem):
    """
    Fms function implementation for optimization problems.

    The Fms function is used for testing optimization algorithms, specifically those dealing with frequency modulation sound.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the Fms function value for a given list of variables.

    Notes
    -----
    -6.4 ≤ xi ≤ 6.35
    Length of chromosomes = 6
    Maximum Fitness Value = 0.01
    Maximum Fitness Value Error = 10^-2
    """

    def f(self, x: list) -> float:
        """
        Calculate the Fms function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Fms function value.
        """
        theta = (2.0 * pi) / 100.0
        random.seed(100)

        a1 = x[0]
        w1 = x[1]
        a2 = x[2]
        w2 = x[3]
        a3 = x[4]
        w3 = x[5]

        def yzero(t):
            return 1.0 * sin((5.0 * theta * t) - (1.5 * sin((4.8 * theta * t) + (2.0 * sin(4.9 * theta * t)))))

        distance = 0.0
        partialfitness = 0.0
        fitness = 0.0

        for k in range(101):
            distance = (
                a1 * sin((w1 * theta * k) - (a2 * sin((w2 * theta * k) + (a3 * sin(w3 * theta * k))))))
            distance -= yzero(k)
            partialfitness += (distance * distance)
        
        fitness = partialfitness
        return round(fitness, 3)
