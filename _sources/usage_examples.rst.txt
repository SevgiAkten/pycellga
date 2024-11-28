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


Customization Scenarios
------------------------

`pycellga` allows users to customize the methods and operators used in their optimization problems. Below are some examples to help you design your own scenarios.

Selecting Gene Types
---------------------

You can change the `gen_type` parameter based on the type of problem:

- `pycellga.optimizer.GeneType.REAL` for real-valued problems.
- `pycellga.optimizer.GeneType.BINARY` for binary problems.
- `pycellga.optimizer.GeneType.PERMUTATION` for permutation-based problems.


Problem Selection
------------------

`pycellga` includes several built-in problems for quick usage, categorized into continuous (real-valued), binary, and permutation problems. These problems allow users to directly specify the `problem` parameter for quick implementation.

Continuous Problems
--------------------

For continuous optimization problems, the following functions are available:

- `pycellga.optimizer.Ackley()`
- `pycellga.optimizer.Bentcigar()`
- `pycellga.optimizer.Bohachevsky()`
- `pycellga.optimizer.Chichinadze()`
- `pycellga.optimizer.Dropwave()`
- `pycellga.optimizer.Fms()`
- `pycellga.optimizer.Griewank()`
- `pycellga.optimizer.Holzman()`
- `pycellga.optimizer.Levy()`
- `pycellga.optimizer.Matyas()`
- `pycellga.optimizer.Pow()`
- `pycellga.optimizer.Powell()`
- `pycellga.optimizer.Rastrigin()`
- `pycellga.optimizer.Rosenbrock()`
- `pycellga.optimizer.Rothellipsoid()`
- `pycellga.optimizer.Schaffer()`
- `pycellga.optimizer.Schaffer2()`
- `pycellga.optimizer.Schwefel()`
- `pycellga.optimizer.Sphere()`
- `pycellga.optimizer.StyblinskiTang()`
- `pycellga.optimizer.Sumofdifferentpowers()`
- `pycellga.optimizer.Threehumps()`
- `pycellga.optimizer.Zakharov()`
- `pycellga.optimizer.Zettle()`

Binary Problems
----------------

For binary optimization problems, use the following built-in options:

- `pycellga.optimizer.CountSat()`
- `pycellga.optimizer.Ecc()`
- `pycellga.optimizer.Maxcut20_01()`
- `pycellga.optimizer.Maxcut20_09()`
- `pycellga.optimizer.Maxcut100()`
- `pycellga.optimizer.Mmdp()`
- `pycellga.optimizer.OneMax()`
- `pycellga.optimizer.Peak()`

Permutation Problems
--------------------

For permutation-based optimization problems, the following option is available:

- `pycellga.optimizer.Tsp()`

These built-in problems provide a diverse set of test cases, allowing users to explore `pycellga`'s capabilities across a wide range of optimization challenges. Users can also define custom problems to suit their specific needs.


Selection Operators
--------------------
Choose from a variety of selection methods:

- `pycellga.optimizer.TournamentSelection`
- `pycellga.optimizer.RouletteWheelSelection`

Recombination Operators
------------------------

The package provides multiple crossover operators:

- `pycellga.optimizer.OnePointCrossover`
- `pycellga.optimizer.PMXCrossover`
- `pycellga.optimizer.TwoPointCrossover`
- `pycellga.optimizer.UniformCrossover`
- `pycellga.optimizer.ByteUniformCrossover`
- `pycellga.optimizer.ByteOnePointCrossover`
- `pycellga.optimizer.FlatCrossover`
- `pycellga.optimizer.ArithmeticCrossover`
- `pycellga.optimizer.BlxalphaCrossover`
- `pycellga.optimizer.LinearCrossover`
- `pycellga.optimizer.UnfairAvarageCrossover`

Mutation Operators
-------------------

You can customize mutation with these options:

- `pycellga.optimizer.BitFlipMutation`
- `pycellga.optimizer.ByteMutation`
- `pycellga.optimizer.ByteMutationRandom`
- `pycellga.optimizer.InsertionMutation`
- `pycellga.optimizer.ShuffleMutation`
- `pycellga.optimizer.SwapMutation`
- `pycellga.optimizer.TwoOptMutation`
- `pycellga.optimizer.FloatUniformMutation`
- `pycellga.optimizer.MutationOperator`


Example Scenarios
------------------

Scenario 1: Binary Optimization with Tournament Selection
------------------------------------------------------------

Optimize a binary problem using tournament selection, one-point crossover, and bit-flip mutation.

.. code-block:: python

    result = pycellga.optimizer.cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        gen_type=pycellga.optimizer.GeneType.BINARY,
        p_crossover=0.8,
        p_mutation=0.1,
        problem=pycellga.optimizer.OneMax(),  # Built-in binary optimization problem
        selection=pycellga.optimizer.TournamentSelection,
        recombination=pycellga.optimizer.OnePointCrossover,
        mutation=pycellga.optimizer.BitFlipMutation,
        mins=[0] * 10,
        maxs=[1] * 10,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


Scenario 2: Real-Valued Optimization with Byte One Point Crossover
--------------------------------------------------------------------

Solve a real-valued optimization problem using Byte One Point Crossover and Byte Mutation.

.. code-block:: python

    result = pycellga.optimizer.cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        gen_type=pycellga.optimizer.GeneType.REAL,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=pycellga.optimizer.Ackley(10),  # Built-in real-valued optimization problem
        selection=pycellga.optimizer.RouletteWheelSelection,
        recombination=pycellga.optimizer.ByteOnePointCrossover,
        mutation=pycellga.optimizer.ByteMutation,
        mins=[-32.768] * 10,
        maxs=[32.768] * 10,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

Scenario 3: Permutation Optimization for Traveling Salesman Problem
----------------------------------------------------------------------

Optimize a TSP using permutation encoding, PMX crossover, and swap mutation.

.. code-block:: python

    result = pycellga.optimizer.cga(
        n_cols=5,
        n_rows=5,
        n_gen=300,
        ch_size=14,  # Number of cities
        gen_type=pycellga.optimizer.GeneType.PERMUTATION,
        p_crossover=0.85,
        p_mutation=0.15,
        problem=pycellga.optimizer.Tsp(),  # Built-in TSP optimization problem
        selection=pycellga.optimizer.TournamentSelection,
        recombination=pycellga.optimizer.PMXCrossover,
        mutation=pycellga.optimizer.SwapMutation,
        mins=[1] * 14,
        maxs=[14] * 14,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


These scenarios demonstrate how to adapt pycellga to different optimization problems using its flexible configuration options.

