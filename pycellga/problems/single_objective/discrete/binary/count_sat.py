from problems.abstract_problem import AbstractProblem

class CountSat(AbstractProblem):
    """
    CountSat function implementation for optimization problems.

    The CountSat function is used for testing optimization algorithms, particularly those involving satisfiability problems.

    Attributes
    ----------
    design_variables : int
        The number of variables (chromosome length) for the problem.
    bounds : list of tuple
        The bounds for each binary variable, typically [(0, 1), (0, 1), ...] for binary inputs.
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.

    Methods
    -------
    f(x: list) -> float
        Calculates the CountSat function value for a given list of binary variables.
    """

    def __init__(self, design_variables=20):
        super().__init__(design_variables=design_variables,
                         bounds=[(0, 1) for _ in range(design_variables)],
                         objectives=["maximize"])

    def f(self, x: list) -> float:
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
        fitness = (total_ones + 
                   (variables * (variables - 1) * (variables - 2)) - 
                   ((variables - 2) * total_ones * (total_ones - 1)) + 
                   (total_ones * (total_ones - 1) * (total_ones - 2)))

        # Normalize the fitness value
        fitness_normalized = fitness / 6860
        return round(fitness_normalized, 3)

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
