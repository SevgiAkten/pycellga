from problems.abstract_problem import AbstractProblem
from numpy import random
from typing import List
from common import GeneType


class Peak(AbstractProblem):
    """
    Represents the Peak problem.

    The Peak problem evaluates the fitness of a chromosome based on its 
    distance to a set of target peaks.

    Attributes
    ----------
    gen_type : GeneType
        Type of genes used in the problem (binary in this case).
    n_var : int
        The number of design variables (chromosome length, default is 100).
    xl : float
        The lower bounds for the design variables (0 for binary genes).
    xu : float
        The upper bounds for the design variables (1 for binary genes).

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    """

    def __init__(self, n_var: int = 100):
        """
        Initialize the Peak problem with a default number of variables (100) 
        and binary gene bounds.

        Parameters
        ----------
        n_var : int, optional
            Number of design variables (default is 100).
        """
        xl = 0
        xu = 1
        gen_type=GeneType.BINARY
        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

        # Seed the random number generator for reproducibility
        random.seed(100)
        self.p_target = [
            [random.randint(2) for _ in range(n_var)] for _ in range(100)
        ]  # 100 target peaks

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
        problem_length = len(x)
        min_distance = float("inf")

        for peak in self.p_target:
            distance = sum(1 for xi, pi in zip(x, peak) if xi != pi)
            if distance < min_distance:
                min_distance = distance

        # Normalize the fitness value
        fitness = 1 - (min_distance / problem_length)  # 1 - normalized distance
        return round(fitness, 3)
