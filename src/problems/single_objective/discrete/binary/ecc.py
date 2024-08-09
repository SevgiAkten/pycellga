from problems.abstract_problem import AbstractProblem

class Ecc(AbstractProblem):
    """
    Error Correcting Codes Design Problem (ECC) function implementation for optimization problems.

    The ECC function is used for testing optimization algorithms, particularly those involving 
    error-correcting codes.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Calculates the ECC function value for a given list of variables.

    Notes
    -----
    Length of chromosomes = 144
    Maximum Fitness Value = 0.0674
    """

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
            The ECC function value.
        """
        individual_length = 12  # Length of individual code segments
        half_code = 12  # Number of code segments to compare
        partial_fitness = 0.0  # Accumulated partial fitness value
        fitness = 0.0  # Final fitness value

        for i in range(half_code):
            partial_fitness += 1.0 / (individual_length * individual_length)
            for j in range(half_code):
                if j != i:
                    hamming = 1  # Initialize Hamming distance
                    for k in range(individual_length):
                        # Compute Hamming distance between segments
                        if x[(i * individual_length + k) ^ x[(j * individual_length + k)]]:
                            hamming += 1

                    # Update partial fitness with contributions from current pair of segments
                    partial_fitness += (1.0 / (hamming * hamming) + 
                                        1.0 / ((individual_length - hamming) * 
                                               (individual_length - hamming)))

        # Calculate final fitness value
        fitness = 1.0 / (2 * partial_fitness)

        return round(fitness, 4)
