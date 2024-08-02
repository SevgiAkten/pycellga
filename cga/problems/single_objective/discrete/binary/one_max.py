from cga.problems.abstract_problem import AbstractProblem

class OneMax(AbstractProblem):
    """
    Represents the OneMax problem.

    The OneMax problem is a simple genetic algorithm benchmark problem 
    where the fitness of a chromosome is the sum of its bits.

    Attributes
    ----------
    None

    Methods
    -------
    f(x: list) -> float
        Evaluates the fitness of a given chromosome.
    """

    def f(self, x) -> float:
        """
        Evaluates the fitness of a given chromosome for the OneMax problem.

        The fitness function is the sum of all bits in the chromosome.

        Parameters
        ----------
        x : list
            A list representing the chromosome, where each element is a binary 
            value (0 or 1).

        Returns
        -------
        float
            The fitness value of the chromosome, which is the sum of its bits.
        """
        return sum(x)
