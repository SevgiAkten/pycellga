from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

from typing import List

class OneMax(AbstractProblem):
    """
    Represents the OneMax problem.

    The OneMax problem is a simple genetic algorithm benchmark problem 
    where the fitness of a chromosome is the sum of its bits.

    Attributes
    ----------
    gen_type : GeneType
        Type of genes used in the problem (binary in this case).
    n_var : int
        The number of design variables (default is 100).
    xl : float
        The lower bound for the design variables (0 for binary genes).
    xu : float
        The upper bound for the design variables (1 for binary genes).

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    """

    def __init__(self, n_var: int = 100):
        """
        Initialize the OneMax problem with a default number of variables (100) 
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

    def f(self, x: List[int]) -> float:
        """
        Evaluates the fitness of a given chromosome for the OneMax problem.

        The fitness function is the sum of all bits in the chromosome.

        Parameters
        ----------
        x : List[int]
            A list representing the chromosome, where each element is a binary 
            value (0 or 1).

        Returns
        -------
        float
            The fitness value of the chromosome, which is the sum of its bits.
        """
        return float(-sum(x))
