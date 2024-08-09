import optimizer

# --------------------------------Cellular Genetic Algorithm (cga)------------------------------------------ #

result = optimizer.cga(
    n_cols = 5,
    n_rows = 5,
    n_gen = 100,
    ch_size = 5,
    gen_type = "Real",
    p_crossover = 0.9,
    p_mutation = 0.2,
    problem = optimizer.Ackley(),
    selection = optimizer.TournamentSelection,
    recombination = optimizer.ByteOnePointCrossover,
    mutation = optimizer.ByteMutationRandom)

"""
Optimize using the Cellular Genetic Algorithm (cga).

Parameters
----------
n_cols : int
    Number of columns in the cellular grid.
n_rows : int
    Number of rows in the cellular grid.
n_gen : int
    Number of generations to run the algorithm.
ch_size : int
    Chromosome size.
gen_type : str
    Type of the genetic representation, e.g., 'Real-valued'.
p_crossover : float
    Probability of crossover.
p_mutation : float
    Probability of mutation.
problem : problem class
    Instance of the optimization problem, e.g., Ackley.
selection : selection function
    Selection method, e.g., TournamentSelection.
recombination : recombination function
    Crossover method, e.g., ByteOnePointCrossover.
mutation : mutation function
    Mutation method, e.g., ByteMutationRandom.

Returns
-------
tuple
    Best solution found and its corresponding chromosome.
"""

# --------------------------------Synchronous Cellular Genetic Algorithm (sync_cga)------------------------------------------ #

# result = optimizer.sync_cga(
#     n_cols = 5,
#     n_rows = 5,
#     n_gen = 100,
#     ch_size = 5,
#     gen_type = "Real",
#     p_crossover = 0.9,
#     p_mutation = 0.2,
#     problem = optimizer.Ackley(),
#     selection = optimizer.TournamentSelection,
#     recombination = optimizer.BlxalphaCrossover,
#     mutation = optimizer.FloatUniformMutation)

"""
Optimize using the Synchronous Cellular Genetic Algorithm (sync_cga).

Parameters
----------
n_cols : int
    Number of columns in the cellular grid.
n_rows : int
    Number of rows in the cellular grid.
n_gen : int
    Number of generations to run the algorithm.
ch_size : int
    Chromosome size.
gen_type : str
    Type of the genetic representation, e.g., 'Real-valued'.
p_crossover : float
    Probability of crossover.
p_mutation : float
    Probability of mutation.
problem : problem class
    Instance of the optimization problem, e.g., Ackley.
selection : selection function
    Selection method, e.g., TournamentSelection.
recombination : recombination function
    Crossover method, e.g., BlxalphaCrossover.
mutation : mutation function
    Mutation method, e.g., FloatUniformMutation.

Returns
-------
tuple
    Best solution found and its corresponding chromosome.
"""

# --------------------------------Alpha Male Cellular Genetic Algorithm (alpha_cga)------------------------------------------ #

# result = optimizer.alpha_cga(
#     n_cols = 5,
#     n_rows = 5,
#     n_gen = 100,
#     ch_size = 10,
#     gen_type = "Real",
#     p_crossover = 0.9,
#     p_mutation = 0.2,
#     problem = optimizer.Ackley(),
#     selection = optimizer.TournamentSelection,
#     recombination = optimizer.BlxalphaCrossover,
#     mutation = optimizer.FloatUniformMutation)

"""
Optimize using the Alpha Male Cellular Genetic Algorithm (alpha_cga).

Parameters
----------
n_cols : int
    Number of columns in the cellular grid.
n_rows : int
    Number of rows in the cellular grid.
n_gen : int
    Number of generations to run the algorithm.
ch_size : int
    Chromosome size.
gen_type : str
    Type of the genetic representation, e.g., 'Real-valued'.
p_crossover : float
    Probability of crossover.
p_mutation : float
    Probability of mutation.
problem : problem class
    Instance of the optimization problem, e.g., Ackley.
selection : selection function
    Selection method, e.g., TournamentSelection.
recombination : recombination function
    Crossover method, e.g., BlxalphaCrossover.
mutation : mutation function
    Mutation method, e.g., FloatUniformMutation.

Returns
-------
tuple
    Best solution found and its corresponding chromosome.
"""
# --------------------------------Compact Cellular Genetic Algorithm (ccga)------------------------------------------ #

# result = optimizer.ccga(
#     n_cols = 5,
#     n_rows = 5,
#     n_gen = 100,
#     ch_size = 10,
#     gen_type = "Binary",
#     problem = optimizer.OneMax(),
#     selection = optimizer.TournamentSelection)

"""
Optimize using the Compact Cellular Genetic Algorithm (ccga).

Parameters
----------
n_cols : int
    Number of columns in the cellular grid.
n_rows : int
    Number of rows in the cellular grid.
n_gen : int
    Number of generations to run the algorithm.
ch_size : int
    Chromosome size.
gen_type : str
    Type of the genetic representation, e.g., 'Binary'.
problem : problem class
    Instance of the optimization problem, e.g., OneMax.
selection : selection function
    Selection method, e.g., TournamentSelection.

Returns
-------
tuple
    Best solution found and its corresponding chromosome.
"""

# --------------------------------Machine-Coded Compact Cellular Genetic Algorithm (mcccga)------------------------------------------ #

# result = optimizer.mcccga(
#     n_cols = 5,
#     n_rows = 5,
#     n_gen = 100,
#     ch_size = 5,
#     gen_type = "Real",
#     problem = optimizer.Ackley(),
#     selection = optimizer.TournamentSelection,
#     min_value = -32.768,
#     max_value = 32.768)

"""
Optimize using the Machine-Coded Compact Cellular Genetic Algorithm (mcccga).

Parameters
----------
n_cols : int
    Number of columns in the cellular grid.
n_rows : int
    Number of rows in the cellular grid.
n_gen : int
    Number of generations to run the algorithm.
ch_size : int
    Chromosome size.
gen_type : str
    Type of the genetic representation, e.g., 'Real-valued'.
problem : problem class
    Instance of the optimization problem, e.g., Ackley.
selection : selection function
    Selection method, e.g., TournamentSelection.
min_value : float
    Minimum value of the real-valued variables.
max_value : float
    Maximum value of the real-valued variables.

Returns
-------
tuple
    Best solution found and its corresponding chromosome.
"""



print("Best solution:", result[1], "\nBest solution chromosome:", result[0])
