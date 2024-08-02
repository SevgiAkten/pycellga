from cga.problems.abstract_problem import AbstractProblem
class Ecc(AbstractProblem):
    """
    Error Correcting Codes Design Problem (ECC) function implementation for optimization problems.

    The ECC function is used for testing optimization algorithms, particularly those involving error-correcting codes.

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
        individual_length = 12
        half_code = 12
        partial_fitness = 0.0
        hamming = 0
        fitness = 0.0

        for i in range(half_code):
            partial_fitness += 1.0 / (individual_length * individual_length)
            for j in range(half_code):
                if j != i:
                    hamming = 1
                    for k in range(individual_length):
                        if x[(i * individual_length + k) ^ x[(j * individual_length + k)]]:
                            hamming += 1

                    partial_fitness += (1.0 / (hamming * hamming) + 
                                        1.0 / ((individual_length - hamming) * (individual_length - hamming)))

        fitness = 1.0 / (2 * partial_fitness)

        return round(fitness, 4)
