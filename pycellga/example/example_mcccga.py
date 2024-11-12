import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import optimizer
import numpy as np
from individual import GeneType

class RealProblem:
    """
    Example problem class to be minimized.

    This class implements a simple sum of squares function with a global minimum value of 0,
    achieved when all elements of the chromosome are equal to 0.
    """
    
    def __init__(self):
        pass
    
    def f(self, x):
        """
        Compute the objective function value.

        This method implements the sum of squares function.

        Parameters
        ----------
        x : list or numpy.ndarray
            The input chromosome represented as a list or array of real values.

        Returns
        -------
        float
            The computed value of the function given the input x.
        """
        return sum(np.power(xi, 2) for xi in x)

def run_mcccga_example():
    """
    Run the Machine-Coded Compact Cellular Genetic Algorithm (mcccga)
    using the optimizer module.

    The mcccga is configured with a 5x5 grid, 100 generations, and a chromosome size of 10.
    The problem being solved is an instance of the RealProblem class,
    with real genes, constrained by specified mins and maxs.

    Returns
    -------
    Result
        A Result instance containing the best solution's chromosome, its fitness value, 
        and the generation in which it was found.
    """
    # Create an instance of the problem
    problem_instance = RealProblem()

    result = optimizer.mcccga(
        n_cols=5,
        n_rows=5,
        n_gen=500,
        ch_size=5,
        gen_type=GeneType.REAL,
        problem=problem_instance,  # Pass the RealProblem instance
        selection=optimizer.TournamentSelection,
        mins=[-3.768] * 5,
        maxs=[3.768] * 5
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)
    print("Generation found:", result.generation_found)

if __name__ == "__main__":
    run_mcccga_example()
