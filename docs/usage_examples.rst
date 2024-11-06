Usage Examples
==============

In this section, we'll explain the `cga` method in the optimizer and provide an example of how to use it. The package includes various ready-to-use crossover and mutation operators, along with real-valued, binary, and permutation functions that you can run directly. Examples for other methods are available in the `example` folder, while an example for `cga` is provided below.

cga (Cellular Genetic Algorithm)
--------------------------------

**cga** is a type of genetic algorithm where the population is structured as a grid (or other topologies), and each individual interacts only with its neighbors. This structure helps maintain diversity in the population and can prevent premature convergence. To specialize the CGA for real-valued optimization problems, ICGA (Improved CGA) with machine-coded representation can be used, applying byte operators. The encoding and decoding of numbers follow the IEEE 754 standard for floating-point arithmetic, yielding better results for continuous functions.

Example Problem
---------------

Suppose we have a problem that we want to minimize using a Cellular Genetic Algorithm (CGA). The problem is defined as a simple sum of squares function, where the goal is to find a chromosome (vector) that minimizes the function.

The sum of squares function computes the sum of the squares of each element in the chromosome. This function reaches its global minimum when all elements of the chromosome are equal to 0. The corresponding function value at this point is 0.

ExampleProblem Class
--------------------

Here’s how we can define this problem in Python using the `ExampleProblem` class:

.. code-block:: python

    from mpmath import power as pw
    import pycellga 

    class ExampleProblem:
        
        def __init__(self):
            pass
        
        def f(self, x):
            return sum(pw(xi, 2) for xi in x)

Usage
-----

.. code-block:: python

    result = pycellga.optimizer.cga(
        n_cols = 5,
        n_rows = 5,
        n_gen = 100,
        ch_size = 5,
        gen_type = pycellga.optimizer.GeneType.REAL,
        p_crossover = 0.9,
        p_mutation = 0.2,
        problem = ExampleProblem(),  # Replace with a real problem instance as needed
        selection = pycellga.optimizer.TournamentSelection,
        recombination = pycellga.optimizer.ByteOnePointCrossover,
        mutation = pycellga.optimizer.ByteMutationRandom,
        mins = [-32.768] * 5,  # Minimum values for each gene
        maxs = [32.768] * 5,    # Maximum values for each gene
        seed_par = 100 # Ensures the random number generation is repeatable
    )
    print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

    # The result is 
    # Best solution: 0.0 
    # Best solution chromosome: [0.0, 0.0, 0.0, 0.0, 0.0]

We have provided a basic example above. If you're interested in exploring more examples:

- `Click here to see the other examples <https://github.com/SevgiAkten/pycellga/tree/main/pycellga/example>`_ available directly in the repository.
