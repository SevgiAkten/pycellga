from problems.abstract_problem import AbstractProblem

class Sphere(AbstractProblem):
    """
    Sphere function implementation for optimization problems.

    The Sphere function is commonly used for testing optimization algorithms.
    It is defined on a hypercube where each variable typically lies within [-5.12, 5.12].
    """

    def __init__(self, design_variables=10):
        """
        Initializes the Sphere function with specified design variables and bounds.
        
        Parameters
        ----------
        design_variables : int, optional
            Number of variables for the function, by default 10.
        """
        super().__init__(design_variables=design_variables, bounds=[(-5.12, 5.12)] * design_variables, objectives=["minimize"])

    def f(self, x: list) -> float:
        """
        Calculate the Sphere function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Sphere function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        fitness = sum([xi**2 for xi in x])
        return round(fitness, 3)

    def evaluate(self, x, out, *args, **kwargs):
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
