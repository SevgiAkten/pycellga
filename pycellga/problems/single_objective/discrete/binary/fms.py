from problems.abstract_problem import AbstractProblem
from numpy import pi, sin, random

class Fms(AbstractProblem):
    """
    Frequency Modulation Sound (FMS) function implementation for optimization problems.

    The FMS function is used for testing optimization algorithms, particularly those involving frequency modulation sound.

    Attributes
    ----------
    design_variables : int
        The number of variables for the problem.
    bounds : list of tuple
        The bounds for each variable.
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Calculates the FMS function value for a given list of variables.

    Notes
    -----
    Length of chromosomes = 192
    Maximum Fitness Value = 0.01
    Maximum Fitness Value Error = 10^-2
    """

    def __init__(self, design_variables=192, bounds=[(0, 1)] * 192, objectives=1):
        super().__init__(design_variables, bounds, objectives)

    def f(self, x: list) -> float:
        """
        Calculate the FMS function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of binary variables.

        Returns
        -------
        float
            The FMS function value.
        """
        theta = (2.0 * pi) / 100.0
        random.seed(100)

        # Initialize integer values for parameters
        a1_int, w1_int, a2_int, w2_int, a3_int, w3_int = 0, 0, 0, 0, 0, 0

        # Convert segments of x to integer parameters
        for i in range(32):
            a1_int = (a1_int << 1) | x[i]
            w1_int = (w1_int << 1) | x[i + 32]
            a2_int = (a2_int << 1) | x[i + 64]
            w2_int = (w2_int << 1) | x[i + 96]
            a3_int = (a3_int << 1) | x[i + 128]
            w3_int = (w3_int << 1) | x[i + 160]

        # Map integer values to continuous values for each parameter
        a1 = -6.4 + (12.75 * (a1_int / 4294967295.0))
        w1 = -6.4 + (12.75 * (w1_int / 4294967295.0))
        a2 = -6.4 + (12.75 * (a2_int / 4294967295.0))
        w2 = -6.4 + (12.75 * (w2_int / 4294967295.0))
        a3 = -6.4 + (12.75 * (a3_int / 4294967295.0))
        w3 = -6.4 + (12.75 * (w3_int / 4294967295.0))

        # Generate target signal based on predefined parameters
        target = [sin((5.0 * theta * i) - (1.5 * sin((4.8 * theta * i) + (2.0 * sin(4.9 * theta * i)))))
                  for i in range(101)]

        # Generate signal y based on the parameters derived from x
        y = [a1 * sin((w1 * theta * j) - (a2 * sin((w2 * theta * j) + (a3 * sin(w3 * theta * j)))))
             for j in range(101)]

        # Calculate fitness as the mean squared error between target and y
        fitness = sum((target[k] - y[k]) ** 2 for k in range(101))
        return round(fitness, 3)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate function for compatibility with pymoo's optimizer.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
