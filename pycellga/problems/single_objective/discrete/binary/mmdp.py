from problems.abstract_problem import AbstractProblem
from typing import List, Tuple

class Mmdp(AbstractProblem):
    """
    Represents the Massively Multimodal Deceptive Problem (MMDP).

    The MMDP is designed to deceive genetic algorithms by having multiple local 
    optima. The problem is characterized by a chromosome length of 240 and a 
    maximum fitness value of 40.

    Attributes
    ----------
    design_variables : List[str]
        Names of the design variables (in this case, binary chromosome genes).
    bounds : List[Tuple[float, float]]
        Bounds for each design variable (0 or 1).
    objectives : List[str]
        Objectives for optimization, e.g., "maximize" in this case.
    constraints : List[str]
        Any constraints for the optimization problem.

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    
    Notes
    -----
    # Length of chromosomes = 240
    # Maximum Fitness Value = 40
    """

    def __init__(self):
        """
        Initializes the MMDP problem with predefined design variables, bounds, 
        objectives, and constraints.
        """
        design_variables = ["gene" + str(i) for i in range(240)]
        bounds = [(0, 1) for _ in range(240)]
        objectives = ["maximize"]
        constraints = []

        super().__init__(design_variables, bounds, objectives, constraints)

    def f(self, x: List[int]) -> float:
        """
        Evaluates the fitness of a given chromosome for the MMDP.

        The fitness function is calculated based on the number of ones in each 
        of the 40 subproblems, each of length 6.

        Parameters
        ----------
        x : List[int]
            A list representing the chromosome, where each element is a binary 
            value (0 or 1).

        Returns
        -------
        float
            The normalized fitness value of the chromosome, rounded to three 
            decimal places.
        """
        subproblems_length = 6
        subproblems_number = 40
        fitness = 0.0

        for i in range(subproblems_number):
            total_ones = sum(x[i * subproblems_length + j] for j in range(subproblems_length))

            if total_ones == 0 or total_ones == 6:
                partial_fitness = 1.0
            elif total_ones == 1 or total_ones == 5:
                partial_fitness = 0.0
            elif total_ones == 2 or total_ones == 4:
                partial_fitness = 0.360384
            elif total_ones == 3:
                partial_fitness = 0.640576

            fitness += partial_fitness

        fitness_normalized = fitness / subproblems_number
        return round(fitness_normalized, 3)
