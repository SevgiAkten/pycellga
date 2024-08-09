# pycellga: A Python Package for Improved Cellular Genetic Algorithms

`pycellga` is a Python package that implements cellular genetic algorithms (CGAs) for optimizing complex problems. CGAs combine the principles of cellular automata and traditional genetic algorithms, utilizing a spatially structured population organized in a grid-like topology. This structure allows each individual to interact only with its neighboring individuals, promoting diversity and maintaining a balance between exploration and exploitation during the optimization process. `pycellga` has machine coded operators with byte implementations. Beside it has Alpha-male CGA, Machine Coded Compact CGA and Improved CGA with Machine Coded Operaors for real-valued optimization problems.

## Features

- **Cellular Genetic Algorithm (`cga`)**: Efficient implementation of CGAs with various built-in functions for diverse applications.
- **Improved CGA with Machine-Coded Operators**: Enhanced performance in real-valued optimization problems through the use of `machine-coded` `byte operators`.
- **Synchronous Cellular Genetic Algorithm (`sync_cga`)**: Simultaneous update of all individuals (cells) in each iteration for synchronized evolution.
- **Alpha Male Cellular Genetic Algorithm (`alpha_cga`)**: Population divided into social groups, with each group consisting of females selecting the same alpha male.
- **Compact Cellular Genetic Algorithm (`ccga`)**: Integrates the principles of Cellular Genetic Algorithms with those of Compact Genetic Algorithms for memory efficiency.
- **Machine-Coded Compact Cellular Genetic Algorithm (`mcccga`)**: Applies machine-coded compact GA to a cellular structure for optimizing real-valued problems.
- **Customizable**: Offers various customization options to adapt to different optimization problems.


## Installation

You can install `pycellga` via pip:

```bash
pip install pycellga
```

## Documentation

Comprehensive documentation is available on the official documentation site.

## Usage Examples

In this section, we'll explain what each method in the optimizer does and provide examples of how to use them. The package includes various ready-to-use crossover and mutation operators, along with Real-valued, Binary, and Permutation functions that you can run directly —examples are available in the `main.py` file. Please configure the `gen_type` attribute as `Real-valued`, `Binary`, or `Permutation` according to the type of problem you want to solve.

### 1. **cga (Cellular Genetic Algorithm)**

**cga** is a type of genetic algorithm where the population is structured as a grid (or other topologies) and each individual interacts only with its neighbors. This structure helps maintain diversity in the population and can prevent premature convergence. To convert it from classcical cga into a specialized algorithm, ICGA (Improved CGA) with machine-coded representation for real-valued problems, you should use byte operators.The formulation for encoding and decoding numbers was created by an algorithm specified in the IEEE 754 – IEEE Standards for Floating-Point Arithmetic. This approach yields better results for continuous functions.

**Usage:**

```python
result = optimizer.cga(
    n_cols = 5,
    n_rows = 5,
    n_gen = 100,
    ch_size = 5,
    gen_type = "Real-valued",
    p_crossover = 0.9,
    p_mutation = 0.2,
    problem = optimizer.Ackley(),
    selection = optimizer.TournamentSelection,
    recombination = optimizer.ByteOnePointCrossover,
    mutation = optimizer.ByteMutationRandom
)
print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

# The result is 
# Best solution: 0.0 
# Best solution chromosome: [0.0, 0.0, 0.0, 0.0, 0.0]

# Note that the result could be different because the algorithm includes randomness.
```

### 2. **sync_cga (Synchronous Cellular Genetic Algorithm)**

In the **sync_cga** all individuals (cells) are updated simultaneously in each iteration (generation). This means that the algorithm evaluates the fitness of all individuals, selects parents, and applies genetic operators (crossover and mutation) in parallel, updating the entire population at once before moving to the next generation.

**Usage:**

```python
result = optimizer.sync_cga(
    n_cols = 5,
    n_rows = 5,
    n_gen = 100,
    ch_size = 5,
    gen_type = "Real-valued",
    p_crossover = 0.9,
    p_mutation = 0.2,
    problem = optimizer.Ackley(),
    selection = optimizer.TournamentSelection,
    recombination = optimizer.BlxalphaCrossover,
    mutation = optimizer.FloatUniformMutation
)
print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

# The result is 
# Best solution: 0.0 
# Best solution chromosome: [0.0001, 0.00012, 0.00022, 5e-05, -5e-05]

# Note that the result could be different because the algorithm includes randomness.
```

### 3. **alpha_cga (Alpha Male Cellular Genetic Algorithm)**

**alpha_cga** is an extension of the Cellular Genetic Algorithm that involves dividing the population into social groups, where each group consists of females selecting the same alpha male. Within each group, one individual is labeled as the alpha male, and the rest are productive females. 

**Usage:**

```python
result = optimizer.alpha_cga(
    n_cols = 5,
    n_rows = 5,
    n_gen = 100,
    ch_size = 10,
    gen_type = "Real-valued",
    p_crossover = 0.9,
    p_mutation = 0.2,
    problem = optimizer.Ackley(),
    selection = optimizer.TournamentSelection,
    recombination = optimizer.BlxalphaCrossover,
    mutation = optimizer.FloatUniformMutation
)
print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

# The result is 
# Best solution: 0.0 
# Best solution chromosome: [0.0, 0.0, 0.0, 8e-05, -6e-05, 0.00015, 0.0, -0.00014, -0.0, 0.0]

# Note that the result could be different because the algorithm includes randomness.
```

### 4. **ccga (Compact Cellular Genetic Algorithm)**

**ccga** combines the principles of Cellular Genetic Algorithms with those of Compact Genetic Algorithms. This approach leverages the structured population model of Cellular GAs and the memory efficiency of Compact GAs.

**Usage:**

```python
result = optimizer.ccga(
    n_cols = 5,
    n_rows = 5,
    n_gen = 100,
    ch_size = 10,
    gen_type = "Binary",
    problem = optimizer.OneMax(),
    selection = optimizer.TournamentSelection
)

print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

# The result is 
# Best solution: 8 
# Best solution chromosome: [0, 1, 0, 1, 1, 1, 1, 1, 1, 1]

# Note that the result could be different because the algorithm includes randomness.
```

### 5. **mcccga (Machine-Coded Compact Cellular Genetic Algorithm)**

**mcccga** is the adaptation of the machine-coded compact GA for real-valued optimization problems has been applied to a cellular structure. Real-valued variables are converted into a binary format using the IEEE-754 standard. Encoding and decoding processes are performed bidirectionally using the same standard when necessary. Also the initial vector is generated within a narrowed range according to the variable's definition domain.

**Usage:**

```python
result = optimizer.mcccga(
    n_cols = 5,
    n_rows = 5,
    n_gen = 100,
    ch_size = 5,
    gen_type = "Real-valued",
    problem = optimizer.Ackley(),
    selection = optimizer.TournamentSelection,
    min_value = -32.768,
    max_value = 32.768
)
print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

# The result is 
# Best solution: 11.334 
# Best solution chromosome: [2.201, 18.259, -11.774, 0.0, 20.0]

# Note that the result could be different because the algorithm includes randomness.
```

## Contributing

Contributions are welcome! Please read the contributing guidelines first.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Developed by Sevgi Akten Karakaya and Mehmet Hakan Satman.
Inspired by traditional genetic algorithms and cellular automata principles with machine coded operators.
For more information, please visit the project repository.