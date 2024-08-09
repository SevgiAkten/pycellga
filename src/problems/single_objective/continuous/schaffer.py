import numpy as np
from numpy import power as pw
from problems.abstract_problem import AbstractProblem


class Schaffer(AbstractProblem):
    """
    Schaffer's Function.

    This class implements the Schaffer's function, which is a common benchmark problem for optimization algorithms.
    The function is defined over a multidimensional input and is used to test the performance of optimization methods.

    Methods
    -------
    f(X: list) -> float
        Calculates the value of the Schaffer's function for a given list of input variables.
    """

    def f(self, X: list) -> float:
        """
        Evaluate the Schaffer's function at a given point.

        Parameters
        ----------
        X : list
            A list of input variables (continuous values). The length of X should be at least 2.

        Returns
        -------
        float
            The value of the Schaffer's function evaluated at X, rounded to three decimal places.

        Notes
        -----
        The Schaffer's function is defined as:
        \[
        f(X) = \sum_{i=1}^{n-1} \left[ 0.5 + \frac{(\sin(x_i^2 + x_{i+1}^2)^2 - 0.5)^2}{(1 + 0.001 \cdot (x_i^2 + x_{i+1}^2))^2} \right]
        \]
        where \( n \) is the number of elements in X.

        Examples
        --------
        >>> schaffer = Schaffer()
        >>> schaffer.f([1.0, 2.0])
        0.554
        """
        fitness = 0.0
        for i in range(len(X) - 1):
            xi = X[i]
            xi1 = X[i + 1]
            term1 = np.sin(xi**2 + xi1**2)**2
            term2 = 1 + 0.001 * (xi**2 + xi1**2)
            fitness += 0.5 + (term1 - 0.5)**2 / term2**2
        return round(fitness, 3)
