import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import optimizer
from individual import GeneType

class ExampleProblem:
    """
    Example problem class to be minimized.

    This class implements a simple binary optimization problem, where the goal is to maximize the number of 1s.
    """
    
    def __init__(self):
        pass
    
    def f(self, x):
        """
        Compute the objective function value.

        This method implements a simple sum of binary values.

        Parameters
        ----------
        x : list or numpy.ndarray
            The input chromosome represented as a list or array of binary values (0s and 1s).

        Returns
        -------
        int
            The computed value of the function given the input x.
        """
        return sum(x)

def run_ccga_example():
    """
    Run the Compact Cellular Genetic Algorithm (ccga) using the optimizer module.

    The ccga is configured with a 5x5 grid, 100 generations, and a chromosome size of 10.
    The problem being solved is an instance of the ExampleProblem class, 
    with binary genes, constrained by specified mins and maxs.
    
    Returns
    -------
    tuple
        A tuple containing the best solution chromosome and its corresponding value.
    """
    # Create an instance of the problem
    problem_instance = ExampleProblem()

    result = optimizer.ccga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        gen_type=GeneType.BINARY,
        problem=problem_instance,  # Pass the ExampleProblem instance
        selection=optimizer.TournamentSelection,
        mins=[0] * 10,  # Minimum values for each gene (binary)
        maxs=[1] * 10   # Maximum values for each gene (binary)
    )

    # Print the results
    print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

if __name__ == "__main__":
    run_ccga_example()
