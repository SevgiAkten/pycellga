from cga.problems.abstract_problem import AbstractProblem

class Mmdp(AbstractProblem):
    """
    Represents the Massively Multimodal Deceptive Problem (MMDP).

    The MMDP is designed to deceive genetic algorithms by having multiple local 
    optima. The problem is characterized by a chromosome length of 240 and a 
    maximum fitness value of 40.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    
    Notes
    -----
    # Length of chromosomes = 240
    # Maximum Fitness Value = 40
    """

    def f(self, x: list) -> float:
        """
        Evaluates the fitness of a given chromosome for the MMDP.

        The fitness function is calculated based on the number of ones in each 
        of the 40 subproblems, each of length 6.

        Parameters
        ----------
        x : list
            A list representing the chromosome, where each element is a binary 
            value (0 or 1).

        Returns
        -------
        float
            The normalized fitness value of the chromosome, rounded to three 
            decimal places.
        """

        subproblems_length = 6
        subproblems_number = 40
        total_ones = 0
        partial_fitness = 0.0
        fitness = 0.0

        for i in range(subproblems_number):
            total_ones = 0
            for j in range(subproblems_length):
                if x[i * subproblems_length + j] == 1:
                    total_ones += 1

            if total_ones == 0 or total_ones == 6:
                partial_fitness = 1.0
            elif total_ones == 1 or total_ones == 5:
                partial_fitness = 0.0
            elif total_ones == 2 or total_ones == 4:
                partial_fitness = 0.360384
            elif total_ones == 3:
                partial_fitness = 0.640576

            fitness += partial_fitness

        fitness_normalized = fitness / 40

        return round(fitness_normalized, 3)
