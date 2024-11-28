from problems.abstract_problem import AbstractProblem

class Ecc(AbstractProblem):
    """
    Error Correcting Codes Design Problem (ECC) function implementation for optimization problems.

    The ECC function is used for testing optimization algorithms, particularly those involving 
    error-correcting codes.

    Attributes
    ----------
    design_variables : int
        Number of binary variables, typically 144.
    bounds : list of tuple
        Bounds for each variable, typically [(0, 1)] * 144 for binary inputs.
    objectives : int
        Number of objectives, set to 1 for single-objective optimization.
    """

    def __init__(self, design_variables=144):
        bounds = [(0, 1) for _ in range(design_variables)]  # Binary bounds for each variable
        super().__init__(design_variables=design_variables, bounds=bounds, objectives=[1])

    def f(self, x: list) -> float:
        """
        Calculate the ECC function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of binary variables.

        Returns
        -------
        float
            The ECC function value, rounded to four decimal places.
        """
        individual_length = 12  # Length of individual code segments
        half_code = 12  # Number of code segments to compare
        partial_fitness = 0.0  # Accumulated partial fitness value

        for i in range(half_code):
            for j in range(i + 1, half_code):  # Avoid double-counting pairs
                hamming = sum(x[i * individual_length + k] != x[j * individual_length + k] for k in range(individual_length))

                if 0 < hamming < individual_length:
                    partial_fitness += (1.0 / (hamming * hamming) + 
                                        1.0 / ((individual_length - hamming) * 
                                               (individual_length - hamming)))

        # Calculate final fitness value
        fitness = 1.0 / (2 * partial_fitness) if partial_fitness != 0 else 0.0
        return round(fitness, 4)
