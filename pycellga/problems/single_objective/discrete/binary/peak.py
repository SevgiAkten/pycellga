from problems.abstract_problem import AbstractProblem
from numpy import random
from typing import List, Tuple

class Peak(AbstractProblem):
    """
    Represents the Peak problem.

    The Peak problem evaluates the fitness of a chromosome based on its 
    distance to a set of target peaks.

    Attributes
    ----------
    design_variables : List[str]
        Names of the design variables.
    bounds : List[Tuple[float, float]]
        Bounds for each design variable as (min, max).
    objectives : List[str]
        Objectives for optimization, e.g., "minimize" or "maximize".
    constraints : List[str]
        Any constraints for the optimization problem.

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    
    Notes
    -----
    # Length of chromosomes = 100
    # Maximum Fitness Value = 1.0
    """

    def __init__(self):
        """
        Initializes the Peak problem with default values.
        """
        design_variables = ["x" + str(i) for i in range(100)]
        bounds = [(0, 1) for _ in range(100)]  # Each gene is binary (0 or 1)
        objectives = ["maximize"]  # Aim to maximize fitness value
        constraints = []  # No additional constraints

        super().__init__(design_variables, bounds, objectives, constraints)

    def f(self, x: List[int]) -> float:
        """
        Evaluates the fitness of a given chromosome for the Peak problem.

        The fitness function calculates the distance between the given 
        chromosome and a set of randomly generated target peaks.

        Parameters
        ----------
        x : list
            A list representing the chromosome, where each element is a binary 
            value (0 or 1).

        Returns
        -------
        float
            The fitness value of the chromosome, normalized to a range of 0.0 to 1.0.
        """
        
        # Seed the random number generator for reproducibility
        random.seed(100)

        problem_length = len(x)
        number_of_peaks = 100
        
        # Generate target peaks
        p_target = [[random.randint(2) for _ in range(problem_length)] for _ in range(number_of_peaks)]

        # Calculate the distance to the nearest peak
        min_distance = float('inf')
        for peak in p_target:
            distance = sum(1 for xi, pi in zip(x, peak) if xi != pi)
            if distance < min_distance:
                min_distance = distance

        # Normalize the fitness value
        fitness = min_distance / problem_length

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
