from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

from numpy import pi, sin, random
from typing import List

class Fms(AbstractProblem):
    """
    Frequency Modulation Sound (FMS) function implementation for optimization problems.

    The FMS function is used for testing optimization algorithms, particularly those involving frequency modulation sound.

    Attributes
    ----------
    n_var : int
        The number of binary variables for the problem, typically 192.
    gen_type : GeneType
        The type of genes used in the problem, set to BINARY.
    xl : int
        Lower bounds for binary variables, fixed to 0.
    xu : int
        Upper bounds for binary variables, fixed to 1.

    Methods
    -------
    f(x: List[int]) -> float
        Calculates the FMS function value for a given list of binary variables.
    evaluate(x: List[int], out: dict, *args, **kwargs) -> None
        Pymoo-compatible evaluation method for batch processing.
    """

    def __init__(self, n_var: int = 192):
        """
        Initialize the FMS problem.

        Parameters
        ----------
        n_var : int, optional
            Number of binary variables for the problem, by default 192.
        """
        gen_type = GeneType.BINARY
        xl = 0  # Lower bound for binary variables
        xu = 1  # Upper bound for binary variables

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[int]) -> float:
        """
        Calculate the FMS function value for a given list of binary variables.

        Parameters
        ----------
        x : list
            A list of binary variables.

        Returns
        -------
        float
            The FMS function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")

        theta = (2.0 * pi) / 100.0
        random.seed(100)

        # Decode binary variables into continuous parameters
        def decode_segment(segment):
            value = 0
            for bit in segment:
                value = (value << 1) | bit
            return -6.4 + (12.75 * (value / 4294967295.0))

        a1 = decode_segment(x[:32])
        w1 = decode_segment(x[32:64])
        a2 = decode_segment(x[64:96])
        w2 = decode_segment(x[96:128])
        a3 = decode_segment(x[128:160])
        w3 = decode_segment(x[160:192])

        # Generate target signal
        target = [sin((5.0 * theta * i) - (1.5 * sin((4.8 * theta * i) + (2.0 * sin(4.9 * theta * i))))) for i in range(101)]

        # Generate predicted signal
        y = [a1 * sin((w1 * theta * j) - (a2 * sin((w2 * theta * j) + (a3 * sin(w3 * theta * j))))) for j in range(101)]

        # Compute mean squared error
        fitness = sum((target[k] - y[k]) ** 2 for k in range(101))
        return round(fitness, 3)

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
