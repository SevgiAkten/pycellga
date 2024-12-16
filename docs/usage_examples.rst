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
    from typing import List

    from pycellga.optimizer import cga
    from pycellga.recombination import ByteOnePointCrossover
    from pycellga.mutation import ByteMutationRandom
    from pycellga.selection import TournamentSelection
    from pycellga.problems import AbstractProblem
    from pycellga.common import GeneType

    class ExampleProblem(AbstractProblem):

        def __init__(self, n_var):

            super().__init__(
                gen_type=GeneType.REAL,
                n_var=n_var,
                xl=-100, 
                xu=100
            )

        def f(self, x: List[float]) -> float:
            return round(sum(pw(xi, 2) for xi in x),3)


**Usage**

.. code-block:: python

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=5,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=ExampleProblem(n_var=5),
        selection=TournamentSelection,
        recombination=ByteOnePointCrossover,
        mutation=ByteMutationRandom,
        seed_par=100
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
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

    from numpy import power as pw
    from typing import List

    from pycellga.optimizer import alpha_cga
    from pycellga.recombination import BlxalphaCrossover
    from pycellga.mutation import FloatUniformMutation
    from pycellga.selection import TournamentSelection
    from pycellga.problems import AbstractProblem
    from pycellga.common import GeneType


    class ExampleProblem(AbstractProblem):

        def __init__(self, n_var):

            super().__init__(
                gen_type=GeneType.REAL,
                n_var=n_var,
                xl=-100, 
                xu=100
            )

        def f(self, x: List[float]) -> float:

            return round(sum(pw(xi, 2) for xi in x),3)


    result = alpha_cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=ExampleProblem(n_var=10),
        selection=TournamentSelection,
        recombination=BlxalphaCrossover,
        mutation=FloatUniformMutation,
        seed_par=100
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


**Example 2: Compact Cellular Genetic Algorithm (ccga)**

The Compact Cellular Genetic Algorithm optimizes a binary problem where the goal is to maximize the number of `1`s.

.. code-block:: python

    
    from pycellga.optimizer import ccga
    from pycellga.selection import TournamentSelection
    from pycellga.problems import AbstractProblem
    from pycellga.common import GeneType

    class ExampleProblem(AbstractProblem):

        def __init__(self, n_var):

            super().__init__(
                gen_type=GeneType.BINARY,
                n_var=n_var,
                xl=0, 
                xu=1
            )
    
        def f(self, x):
            return sum(x)

    result = ccga(
        n_cols=5,
        n_rows=5,
        n_gen=200,
        ch_size=10,
        problem=ExampleProblem(n_var=10),
        selection=TournamentSelection
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


**Example 3: Machine-Coded Compact Cellular Genetic Algorithm (mcccga)**

The Machine-Coded Compact Cellular Genetic Algorithm solves real-valued optimization problems with machine-coded representation.

.. code-block:: python

    import numpy as np

    from pycellga.optimizer import mcccga
    from pycellga.selection import TournamentSelection
    from pycellga.problems import AbstractProblem
    from pycellga.common import GeneType

    class RealProblem(AbstractProblem):
    
        def __init__(self, n_var):

            super().__init__(
                gen_type=GeneType.REAL,
                n_var=n_var,
                xl=-3.768, 
                xu=3.768
            )
        
        def f(self, x):
            return sum(np.power(xi, 2) for xi in x)

    result = mcccga(
        n_cols=5,
        n_rows=5,
        n_gen=500,
        ch_size=5,
        problem=RealProblem(n_var=5),
        selection=TournamentSelection
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


**Example 4: Synchronous Cellular Genetic Algorithm (sync_cga)**

The Synchronous Cellular Genetic Algorithm optimizes a real-valued problem in a 5x5 grid using the crossover and mutation operators.

.. code-block:: python

    from numpy import power as pw
    from typing import List

    from pycellga.optimizer import sync_cga
    from pycellga.recombination import BlxalphaCrossover
    from pycellga.mutation import FloatUniformMutation
    from pycellga.selection import TournamentSelection
    from pycellga.problems import AbstractProblem
    from pycellga.common import GeneType


    class ExampleProblem(AbstractProblem):

        def __init__(self, n_var):

            super().__init__(
                gen_type=GeneType.REAL,
                n_var=n_var,
                xl=-100, 
                xu=100
            )

        def f(self, x: List[float]) -> float:
            return round(sum(pw(xi, 2) for xi in x),3)


    result = sync_cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=5,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=ExampleProblem(n_var=5),  
        selection=TournamentSelection,
        recombination=BlxalphaCrossover,
        mutation=FloatUniformMutation,
        seed_par=100
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


Customization Scenarios
------------------------

`pycellga` allows users to customize the methods and operators used in their optimization problems. Below are some examples to help you design your own scenarios.

**Selecting Gene Types**

You can use the `gen_type` parameter of the problem based on the defined problem:

.. code-block:: python

    from pycellga.common import GeneType


- `GeneType.REAL` for real-valued problems.
- `GeneType.BINARY` for binary problems.
- `GeneType.PERMUTATION` for permutation-based problems.


**Problem Selection**

`pycellga` includes several built-in problems for quick usage, categorized into continuous (real-valued), binary, and permutation problems. These problems allow users to directly specify the `problem` parameter for quick implementation.

**Continuous Problems**

For continuous optimization problems, the following functions are available:

.. code-block:: python

    from pycellga.problems.single_objective.continuous.ackley import Ackley
    from pycellga.problems.single_objective.continuous.bentcigar import Bentcigar
    from pycellga.problems.single_objective.continuous.bohachevsky import Bohachevsky
    from pycellga.problems.single_objective.continuous.chichinadze import Chichinadze
    from pycellga.problems.single_objective.continuous.dropwave import Dropwave
    from pycellga.problems.single_objective.continuous.fms import Fms
    from pycellga.problems.single_objective.continuous.griewank import Griewank
    from pycellga.problems.single_objective.continuous.holzman import Holzman
    from pycellga.problems.single_objective.continuous.levy import Levy
    from pycellga.problems.single_objective.continuous.matyas import Matyas
    from pycellga.problems.single_objective.continuous.pow import Pow
    from pycellga.problems.single_objective.continuous.powell import Powell
    from pycellga.problems.single_objective.continuous.rastrigin import Rastrigin
    from pycellga.problems.single_objective.continuous.rosenbrock import Rosenbrock
    from pycellga.problems.single_objective.continuous.rothellipsoid import Rothellipsoid
    from pycellga.problems.single_objective.continuous.schaffer import Schaffer
    from pycellga.problems.single_objective.continuous.schaffer2 import Schaffer2
    from pycellga.problems.single_objective.continuous.schwefel import Schwefel
    from pycellga.problems.single_objective.continuous.sphere import Sphere
    from pycellga.problems.single_objective.continuous.styblinskiTang import StyblinskiTang
    from pycellga.problems.single_objective.continuous.sumofdifferentpowers import Sumofdifferentpowers
    from pycellga.problems.single_objective.continuous.threehumps import Threehumps
    from pycellga.problems.single_objective.continuous.zakharov import Zakharov
    from pycellga.problems.single_objective.continuous.zettle import Zettle


**Binary Problems**

For binary optimization problems, use the following built-in options:


.. code-block:: python  

    from pycellga.problems.single_objective.discrete.binary.count_sat import CountSat
    from pycellga.problems.single_objective.discrete.binary.ecc import Ecc
    from pycellga.problems.single_objective.discrete.binary.maxcut20_01 import Maxcut20_01
    from pycellga.problems.single_objective.discrete.binary.maxcut20_09 import Maxcut20_09
    from pycellga.problems.single_objective.discrete.binary.maxcut100 import Maxcut100
    from pycellga.problems.single_objective.discrete.binary.mmdp import Mmdp
    from pycellga.problems.single_objective.discrete.binary.one_max import OneMax
    from pycellga.problems.single_objective.discrete.binary.peak import Peak


**Permutation Problems**

For permutation-based optimization problems, the following option is available:

.. code-block:: python 

    from problems.single_objective.discrete.permutation.tsp import Tsp


These built-in problems provide a diverse set of test cases, allowing users to explore `pycellga`'s capabilities across a wide range of optimization challenges. Users can also define custom problems to suit their specific needs.


**Selection Operators**

Choose from selection methods:

.. code-block:: python 

    from selection.tournament_selection import TournamentSelection
    from selection.roulette_wheel_selection import RouletteWheelSelection


**Recombination Operators**

The package provides multiple crossover operators:

.. code-block:: python 

    from pycellga.recombination.one_point_crossover import OnePointCrossover
    from pycellga.recombination.pmx_crossover import PMXCrossover
    from pycellga.recombination.two_point_crossover import TwoPointCrossover
    from pycellga.recombination.uniform_crossover import UniformCrossover
    from pycellga.recombination.byte_uniform_crossover import ByteUniformCrossover
    from pycellga.recombination.byte_one_point_crossover import ByteOnePointCrossover
    from pycellga.recombination.flat_crossover import FlatCrossover
    from pycellga.recombination.arithmetic_crossover import ArithmeticCrossover 
    from pycellga.recombination.blxalpha_crossover import BlxalphaCrossover 
    from pycellga.recombination.linear_crossover import LinearCrossover
    from pycellga.recombination.unfair_avarage_crossover import UnfairAvarageCrossover


**Mutation Operators**

You can customize mutation with these options:

.. code-block:: python 
    
    from pycellga.mutation.bit_flip_mutation import BitFlipMutation
    from pycellga.mutation.byte_mutation import ByteMutation 
    from pycellga.mutation.byte_mutation_random import ByteMutationRandom 
    from pycellga.mutation.insertion_mutation import InsertionMutation
    from pycellga.mutation.shuffle_mutation import ShuffleMutation
    from pycellga.mutation.swap_mutation import SwapMutation
    from pycellga.mutation.two_opt_mutation import TwoOptMutation
    from pycellga.mutation.float_uniform_mutation import FloatUniformMutation 


**Example Scenarios**

**Scenario 1: Binary Optimization with Tournament Selection**

Optimize a binary problem using tournament selection, one-point crossover, and bit-flip mutation.

.. code-block:: python

    from pycellga.optimizer import cga
    from problems.single_objective.discrete.binary.one_max import OneMax 
    from pycellga.selection import TournamentSelection
    from pycellga.recombination import OnePointCrossover
    from pycellga.mutation import BitFlipMutation

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        p_crossover=0.8,
        p_mutation=0.1,
        problem=OneMax(n_var=10),  # Built-in binary optimization problem
        selection=TournamentSelection,
        recombination=OnePointCrossover,
        mutation=BitFlipMutation
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


**Scenario 2: Real-Valued Optimization with Byte One Point Crossover**

Solve a real-valued optimization problem using Byte One Point Crossover and Byte Mutation.

.. code-block:: python

    from pycellga.optimizer import cga
    from problems.single_objective.continuous.ackley import Ackley
    from pycellga.selection import RouletteWheelSelection
    from pycellga.recombination import ByteOnePointCrossover
    from pycellga.mutation import ByteMutation

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=10,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=Ackley(n_var=10),  # Built-in real-valued optimization problem
        selection=RouletteWheelSelection,
        recombination=ByteOnePointCrossover,
        mutation=ByteMutation,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

**Scenario 3: Permutation Optimization for Traveling Salesman Problem**

Optimize a TSP using permutation encoding, PMX crossover, and swap mutation.

.. code-block:: python

    from pycellga.optimizer import cga
    from problems.single_objective.discrete.permutation.tsp import Tsp
    from pycellga.selection import TournamentSelection
    from pycellga.recombination import PMXCrossover
    from pycellga.mutation import SwapMutation

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=300,
        ch_size=14,  # Number of cities
        p_crossover=0.85,
        p_mutation=0.15,
        problem=Tsp(n_var=14),  # Built-in TSP optimization problem
        selection=TournamentSelection,
        recombination=PMXCrossover,
        mutation=SwapMutation,
        seed_par=100
    )
    print("Best solution:", result.chromosome)
    print("Best fitness value:", result.fitness_value)


These scenarios demonstrate how to adapt pycellga to different optimization problems using its flexible configuration options.

