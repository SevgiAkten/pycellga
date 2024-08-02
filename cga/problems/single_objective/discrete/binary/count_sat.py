from cga.problems.abstract_problem import AbstractProblem
class CountSat(AbstractProblem):
    """
    CountSat function implementation for optimization problems.

    The CountSat function is used for testing optimization algorithms, particularly those involving satisfiability problems.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the CountSat function value for a given list of variables.

    Notes
    -----
    Length of chromosomes = 20
    Maximum Fitness Value = 6860
    Maximum Fitness Value (normalized) = 1
    """

    def f(self, x: list) -> float:
        """
        Calculate the CountSat function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of binary variables.

        Returns
        -------
        float
            The normalized CountSat function value.
        """
        variables = len(x)  # --> n is the length of x
        total_ones = 0
        fitness = 0
        fitness_normalized = 0.0
        
        # Count the number of ones in the list
        for i in x:
            if i == 1:
                total_ones += 1

        # Calculate the fitness value based on the CountSat formula
        fitness = (total_ones + 
                   (variables * (variables - 1) * (variables - 2)) - 
                   ((variables - 2) * total_ones * (total_ones - 1)) + 
                   (total_ones * (total_ones - 1) * (total_ones - 2)))

        # Normalize the fitness value
        fitness_normalized = fitness / 6860
        return round(fitness_normalized, 3)
