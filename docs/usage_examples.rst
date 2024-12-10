Usage Examples
==============

In this section, we'll explain the `cga` method in the optimizer and provide an example of how to use it.

**Example Problem**

Suppose we have a problem that we want to minimize using a Cellular Genetic Algorithm (CGA). The problem is defined as a simple sum of squares function, where the goal is to find a chromosome (vector) that minimizes the function.

The sum of squares function computes the sum of the squares of each element in the chromosome. This function reaches its global minimum when all elements of the chromosome are equal to 0. The corresponding function value at this point is 0.

**ExampleProblem Class**


Here’s how we can define this problem in Python using the `ExampleProblem` class:

.. code-block:: python

    from mpmath import power as pw

    from pycellga.optimizer import cga
    from pycellga.individual import GeneType
    from pycellga.selection import TournamentSelection
    from pycellga.recombination import ByteOnePointCrossover
    from pycellga.mutation import ByteMutationRandom

    class ExampleProblem:
        
        def __init__(self):
            pass
        
        def f(self, x):
            return sum(pw(xi, 2) for xi in x)

**Usage**

.. code-block:: python

    result = cga(
        n_cols = 5,
        n_rows = 5,
        n_gen = 100,
        ch_size = 5,
        gen_type = GeneType.REAL,
        p_crossover = 0.9,
        p_mutation = 0.2,
        problem = ExampleProblem(),  # Replace with a real problem instance as needed
        selection = TournamentSelection,
        recombination = ByteOnePointCrossover,
        mutation = ByteMutationRandom,
        mins = [-32.768] * 5,  # Minimum values for each gene
        maxs = [32.768] * 5,    # Maximum values for each gene
        seed_par = 100 # Ensures the random number generation is repeatable
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

    # The result is 
    # Best solution: 0.0 
    # Best solution chromosome: [0.0, 0.0, 0.0, 0.0, 0.0]


Advanced Usage Examples
------------------------

The following examples demonstrate the usage of other methods provided by `pycellga`, including `alpha_cga`, `ccga`, `mcccga`, and `sync_cga`. Each example highlights a unique algorithm solving real-world optimization problems.

**Example 1: Alpha Cellular Genetic Algorithm (alpha_cga)**

The Alpha Cellular Genetic Algorithm optimizes a real-valued problem using Blxalpha Crossover  and Float Uniform Mutation operators.

.. code-block:: python

    from mpmath import power as pw

    from pycellga.optimizer import alpha_cga
    from pycellga.individual import GeneType
    from pycellga.selection import TournamentSelection
    from pycellga.recombination import BlxalphaCrossover
    from pycellga.mutation import FloatUniformMutation

    class ExampleProblem:
        
        def __init__(self):
            pass
        
        def f(self, x):
            return sum(pw(xi, 2) for xi in x)


    result = alpha_cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        gen_type=GeneType.REAL,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=ExampleProblem(),
        selection=TournamentSelection,
        recombination=BlxalphaCrossover,
        mutation=FloatUniformMutation,
        mins=[-15] * 10,
        maxs=[15] * 10,
        seed_par=100
    )
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

---

**Example 2: Compact Cellular Genetic Algorithm (ccga)**

The Compact Cellular Genetic Algorithm optimizes a binary problem where the goal is to maximize the number of `1`s.

.. code-block:: python

    from pycellga.optimizer import ccga
    from pycellga.individual import GeneType
    from pycellga.selection import TournamentSelection

    class ExampleProblem:
        def __init__(self):
            pass

        def f(self, x):
            return sum(x)

    result = ccga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        gen_type=GeneType.BINARY,
        problem=ExampleProblem(),
        selection=TournamentSelection,
        mins=[0] * 10,
        maxs=[1] * 10
    )
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


**Example 3: Machine-Coded Compact Cellular Genetic Algorithm (mcccga)**

The Machine-Coded Compact Cellular Genetic Algorithm solves real-valued optimization problems with machine-coded representation.

.. code-block:: python

    from pycellga.optimizer import mcccga
    from pycellga.individual import GeneType
    from pycellga.selection import TournamentSelection
    

    class RealProblem:
        def __init__(self):
            pass

        def f(self, x):
            return sum(np.power(xi, 2) for xi in x)

    result = mcccga(
        n_cols=5,
        n_rows=5,
        n_gen=500,
        ch_size=5,
        gen_type=GeneType.REAL,
        problem=RealProblem(),
        selection=TournamentSelection,
        mins=[-3.55] * 5,
        maxs=[3.55] * 5
    )
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


**Example 4: Synchronous Cellular Genetic Algorithm (sync_cga)**

The Synchronous Cellular Genetic Algorithm optimizes a real-valued problem in a 5x5 grid using the crossover and mutation operators.

.. code-block:: python

    from pycellga.optimizer import sync_cga
    from pycellga.individual import GeneType
    from pycellga.selection import TournamentSelection
    from pycellga.recombination import BlxalphaCrossover
    from pycellga.mutation import FloatUniformMutation

    class ExampleProblem:
        def __init__(self):
            pass

        def f(self, x):
            return sum(pw(xi, 2) for xi in x)

    result = sync_cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=5,
        gen_type=GeneType.REAL,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=ExampleProblem(),
        selection=TournamentSelection,
        recombination=BlxalphaCrossover,
        mutation=FloatUniformMutation,
        mins=[-32.768] * 5,
        maxs=[32.768] * 5,
        seed_par=100
    )
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


Customization Scenarios
------------------------

`pycellga` allows users to customize the methods and operators used in their optimization problems. Below are some examples to help you design your own scenarios.

**Selecting Gene Types**

You can change the `gen_type` parameter based on the type of problem:

- `pycellga.individual.GeneType.REAL` for real-valued problems.
- `pycellga.individual.GeneType.BINARY` for binary problems.
- `pycellga.individual.GeneType.PERMUTATION` for permutation-based problems.


**Problem Selection**

`pycellga` includes several built-in problems for quick usage, categorized into continuous (real-valued), binary, and permutation problems. These problems allow users to directly specify the `problem` parameter for quick implementation.

**Continuous Problems**

For continuous optimization problems, the following functions are available:

- `pycellga.problems.Ackley`
- `pycellga.problems.Bentcigar`
- `pycellga.problems.Bohachevsky`
- `pycellga.problems.Chichinadze`
- `pycellga.problems.Dropwave`
- `pycellga.problems.Fms`
- `pycellga.problems.Griewank`
- `pycellga.problems.Holzman`
- `pycellga.problems.Levy`
- `pycellga.problems.Matyas`
- `pycellga.problems.Pow`
- `pycellga.problems.Powell`
- `pycellga.problems.Rastrigin`
- `pycellga.problems.Rosenbrock`
- `pycellga.problems.Rothellipsoid`
- `pycellga.problems.Schaffer`
- `pycellga.problems.Schaffer2`
- `pycellga.problems.Schwefel`
- `pycellga.problems.Sphere`
- `pycellga.problems.StyblinskiTang`
- `pycellga.problems.Sumofdifferentpowers`
- `pycellga.problems.Threehumps`
- `pycellga.problems.Zakharov`
- `pycellga.problems.Zettle`

**Binary Problems**

For binary optimization problems, use the following built-in options:

- `pycellga.problems.CountSat`
- `pycellga.problems.Ecc`
- `pycellga.problems.Maxcut20_01`
- `pycellga.problems.Maxcut20_09`
- `pycellga.problems.Maxcut100`
- `pycellga.problems.Mmdp`
- `pycellga.problems.OneMax`
- `pycellga.problems.Peak`

**Permutation Problems**

For permutation-based optimization problems, the following option is available:

- `pycellga.problems.Tsp`

These built-in problems provide a diverse set of test cases, allowing users to explore `pycellga`'s capabilities across a wide range of optimization challenges. Users can also define custom problems to suit their specific needs.


**Selection Operators**

Choose from a variety of selection methods:

- `pycellga.selection.TournamentSelection`
- `pycellga.selection.RouletteWheelSelection`

**Recombination Operators**

The package provides multiple crossover operators:

- `pycellga.recombination.OnePointCrossover`
- `pycellga.recombination.PMXCrossover`
- `pycellga.recombination.TwoPointCrossover`
- `pycellga.recombination.UniformCrossover`
- `pycellga.recombination.ByteUniformCrossover`
- `pycellga.recombination.ByteOnePointCrossover`
- `pycellga.recombination.FlatCrossover`
- `pycellga.recombination.ArithmeticCrossover`
- `pycellga.recombination.BlxalphaCrossover`
- `pycellga.recombination.LinearCrossover`
- `pycellga.recombination.UnfairAvarageCrossover`

**Mutation Operators**

You can customize mutation with these options:

- `pycellga.mutation.BitFlipMutation`
- `pycellga.mutation.ByteMutation`
- `pycellga.mutation.ByteMutationRandom`
- `pycellga.mutation.InsertionMutation`
- `pycellga.mutation.ShuffleMutation`
- `pycellga.mutation.SwapMutation`
- `pycellga.mutation.TwoOptMutation`
- `pycellga.mutation.FloatUniformMutation`
- `pycellga.mutation.MutationOperator`


**Example Scenarios**

**Scenario 1: Binary Optimization with Tournament Selection**

Optimize a binary problem using tournament selection, one-point crossover, and bit-flip mutation.

.. code-block:: python

    from pycellga.optimizer import cga
    from pycellga.individual import GeneType
    from pycellga.problems import OneMax
    from pycellga.selection import TournamentSelection
    from pycellga.recombination import OnePointCrossover
    from pycellga.mutation import BitFlipMutation

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        gen_type=GeneType.BINARY,
        p_crossover=0.8,
        p_mutation=0.1,
        problem=OneMax(),  # Built-in binary optimization problem
        selection=TournamentSelection,
        recombination=OnePointCrossover,
        mutation=BitFlipMutation,
        mins=[0] * 10,
        maxs=[1] * 10,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


**Scenario 2: Real-Valued Optimization with Byte One Point Crossover**

Solve a real-valued optimization problem using Byte One Point Crossover and Byte Mutation.

.. code-block:: python

    from pycellga.optimizer import cga
    from pycellga.individual import GeneType
    from pycellga.problems import Ackley
    from pycellga.selection import RouletteWheelSelection
    from pycellga.recombination import ByteOnePointCrossover
    from pycellga.mutation import ByteMutation

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        gen_type=GeneType.REAL,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=Ackley(10),  # Built-in real-valued optimization problem
        selection=RouletteWheelSelection,
        recombination=ByteOnePointCrossover,
        mutation=ByteMutation,
        mins=[-32.768] * 10,
        maxs=[32.768] * 10,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

**Scenario 3: Permutation Optimization for Traveling Salesman Problem**

Optimize a TSP using permutation encoding, PMX crossover, and swap mutation.

.. code-block:: python

    from pycellga.optimizer import cga
    from pycellga.individual import GeneType
    from pycellga.problems import Tsp
    from pycellga.selection import TournamentSelection
    from pycellga.recombination import PMXCrossover
    from pycellga.mutation import SwapMutation

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=300,
        ch_size=14,  # Number of cities
        gen_type=GeneType.PERMUTATION,
        p_crossover=0.85,
        p_mutation=0.15,
        problem=Tsp(),  # Built-in TSP optimization problem
        selection=TournamentSelection,
        recombination=PMXCrossover,
        mutation=SwapMutation,
        mins=[1] * 14,
        maxs=[14] * 14,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


These scenarios demonstrate how to adapt pycellga to different optimization problems using its flexible configuration options.

