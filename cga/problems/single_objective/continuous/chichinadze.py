from problems.abstract_problem import AbstractProblem
import numpy as np

class Chichinadze(AbstractProblem):
    """
    Chichinadze function implementation for optimization problems.

    The Chichinadze function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x, y ∈ [-30, 30].

    Attributes
    ----------
    None

    Methods
    -------
    f(X: list) -> float
        Calculates the Chichinadze function value for a given list of variables.

    Notes
    -----
    -30 ≤ x, y ≤ 30
    Global minimum at f(5.90133, 0.5) = −43.3159
    """

    def f(self, X: list) -> float:
        """
        Calculate the Chichinadze function value for a given list of variables.

        Parameters
        ----------
        X : list
            A list of float variables.

        Returns
        -------
        float
            The Chichinadze function value.
        """
        x = X[0]
        y = X[1]
        fitness = (np.power(x, 2) - 12 * x + 11 + 
                   (10 * np.cos((np.pi * x) / 2)) +
                   (8 * np.sin(5 * np.pi * x)) - 
                   (1.0 / np.sqrt(5) * np.exp(-(np.power((y - 0.5), 2)) / 2)))
        
        return round(fitness, 4)
