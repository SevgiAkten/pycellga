from problems.abstract_problem import AbstractProblem
from common import GeneType
from typing import List

class Ecc(AbstractProblem):
    """
    Error Correcting Codes Design Problem (ECC) function implementation for optimization problems.

    The ECC function is used for testing optimization algorithms, particularly those involving 
    error-correcting codes.

    Attributes
    ----------
    n_var : int
        Number of binary variables, typically 144.
    gen_type : GeneType
        The type of genes used in the problem, set to BINARY.
    xl : int
        Lower bounds for binary variables, fixed to 0.
    xu : int
        Upper bounds for binary variables, fixed to 1.

    Methods
    -------
    f(x: List[int]) -> float
        Calculates the ECC function value for a given list of binary variables.
    evaluate(x: List[int], out: dict, *args, **kwargs) -> None
        Pymoo-compatible evaluation method for batch processing.
    """

    def __init__(self, n_var: int = 144):
        """
        Initialize the ECC problem.

        Parameters
        ----------
        n_var : int, optional
            Number of binary variables for the problem, by default 144.
        """
        gen_type = GeneType.BINARY
        xl = 0  # Lower bound for binary variables
        xu = 1  # Upper bound for binary variables

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[int]) -> float:
        """
        Calculate the ECC function value for a given list of binary variables.

        Parameters
        ----------
        x : list
            A list of binary variables.

        Returns
        -------
        float
            The ECC function value, rounded to four decimal places.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        individual_length = 12  # Length of individual code segments
        half_code = self.n_var // individual_length  # Number of code segments
        partial_fitness = 0.0  # Accumulated partial fitness value

        for i in range(half_code):
            for j in range(i + 1, half_code):  # Avoid double-counting pairs
                hamming = sum(
                    x[i * individual_length + k] != x[j * individual_length + k]
                    for k in range(individual_length)
                )

                if 0 < hamming < individual_length:
                    partial_fitness += (
                        1.0 / (hamming * hamming)
                        + 1.0 / ((individual_length - hamming) * (individual_length - hamming))
                    )

        # Calculate final fitness value
        fitness = 1.0 / (2 * partial_fitness) if partial_fitness != 0 else 0.0
        return round(fitness, 4)

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
