from problems.abstract_problem import AbstractProblem
from common import GeneType
from typing import List

class CountSat(AbstractProblem):
    """
    CountSat function implementation for optimization problems.

    The CountSat function is used for testing optimization algorithms, particularly those involving satisfiability problems.

    Attributes
    ----------
    n_var : int
        The number of variables (chromosome length) for the problem.
    gen_type : GeneType
        The type of genes used in the problem, set to BINARY.
    xl : int
        Lower bounds for binary variables, fixed to 0.
    xu : int
        Upper bounds for binary variables, fixed to 1.

    Methods
    -------
    f(x: List[int]) -> float
        Calculates the CountSat function value for a given list of binary variables.
    evaluate(x: List[int], out: dict, *args, **kwargs) -> None
        Pymoo-compatible evaluation method for batch processing.
    """

    def __init__(self, n_var: int = 20):
        """
        Initialize the CountSat problem.

        Parameters
        ----------
        n_var : int, optional
            Number of binary variables (chromosome length) for the problem, by default 20.
        """
        gen_type = GeneType.BINARY
        xl = 0  # Lower bound for binary variables
        xu = 1  # Upper bound for binary variables

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[int]) -> float:
        """
        Calculate the CountSat function value for a given list of binary variables.

        Parameters
        ----------
        x : list
            A list of binary variables.

        Returns
        -------
        float
            The normalized CountSat function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        total_ones = sum(1 for i in x if i == 1)
        variables = len(x)

        # Calculate the fitness based on the CountSat formula
        fitness = (
            total_ones
            + (variables * (variables - 1) * (variables - 2))
            - ((variables - 2) * total_ones * (total_ones - 1))
            + (total_ones * (total_ones - 1) * (total_ones - 2))
        )

        # Normalize the fitness value
        fitness_normalized = fitness / 6860
        return round(fitness_normalized, 3)

    def evaluate(self, x: List[int], out: dict, *args, **kwargs) -> None:
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
