from problems.abstract_problem import AbstractProblem
from typing import List, Tuple

class OneMax(AbstractProblem):
    """
    Represents the OneMax problem.

    The OneMax problem is a simple genetic algorithm benchmark problem 
    where the fitness of a chromosome is the sum of its bits.

    Attributes
    ----------
    design_variables : int
        Number of design variables (chromosome length).
    bounds : List[Tuple[float, float]]
        Bounds for each design variable as (min, max).
    objectives : List[str]
        Objectives for optimization, e.g., "maximize".
    constraints : List[str]
        Any constraints for the optimization problem.

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    """

    def __init__(self, 
                 design_variables: int = 100,
                 bounds: List[Tuple[float, float]] = [(0, 1)] * 100,
                 objectives: List[str] = ["maximize"],
                 constraints: List[str] = []):
        """
        Initialize the OneMax problem with default design variables, bounds, 
        objectives, and optional constraints.

        Parameters
        ----------
        design_variables : int, optional
            Number of design variables (default is 100).
        bounds : List[Tuple[float, float]], optional
            Bounds for each design variable in (min, max) format (default is [(0, 1)] * 100).
        objectives : List[str], optional
            Objectives for optimization, e.g., "maximize" (default is ["maximize"]).
        constraints : List[str], optional
            Constraints for the problem (default is an empty list).
        """
        super().__init__(design_variables=design_variables, bounds=bounds, objectives=objectives, constraints=constraints)

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
