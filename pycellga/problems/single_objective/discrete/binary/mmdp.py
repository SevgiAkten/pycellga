from problems.abstract_problem import AbstractProblem
from typing import List
from common import GeneType


class Mmdp(AbstractProblem):
    """
    Represents the Massively Multimodal Deceptive Problem (MMDP).

    The MMDP is designed to deceive genetic algorithms by having multiple local 
    optima. The problem is characterized by a chromosome length of 240 and a 
    maximum fitness value of 40.

    Attributes
    ----------
    gen_type : GeneType
        Type of genes used in the problem (binary in this case).
    n_var : int
        The number of design variables (240 for MMDP).
    xl : float
        The lower bound  for the design variables (0 for binary genes).
    xu : float
        The upper bound for the design variables (1 for binary genes).

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    """

    def __init__(self):
        """
        Initializes the MMDP problem with binary genes, 240 design variables, 
        and predefined bounds.
        """
        n_var = 240  
        xl = 0
        xu = 1
        gen_type=GeneType.BINARY

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

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
