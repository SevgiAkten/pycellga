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

In this section, we'll explain what each method in the optimizer does and provide examples of how to use them. The package includes various ready-to-use crossover and mutation operators, along with Real-valued, Binary, and Permutation functions that you can run directly. Examples for other methods are available in the `example` folder, while the example for cga is provided below.

### **cga (Cellular Genetic Algorithm)**

**cga** is a type of genetic algorithm where the population is structured as a grid (or other topologies), and each individual interacts only with its neighbors. This structure helps maintain diversity in the population and can prevent premature convergence. To specialize the CGA for real-valued optimization problems, ICGA (Improved CGA) with machine-coded representation can be used, applying byte operators. The encoding and decoding of numbers follow the IEEE 754 standard for floating-point arithmetic, yielding better results for continuous functions.

## Example Problem

Suppose we have a problem that we want to minimize using a Cellular Genetic Algorithm (CGA). The problem is defined as a simple sum of squares function, where the goal is to find a chromosome (vector) that minimizes the function.

The sum of squares function computes the sum of the squares of each element in the chromosome. This function reaches its global minimum when all elements of the chromosome are equal to 0. The corresponding function value at this point is 0.

### ExampleProblem Class

Here’s how we can define this problem in Python using the `ExampleProblem` class:

```python
from numpy import power as pw

class ExampleProblem:
    
    def __init__(self):
        pass
    
    def f(self, x):
        
        return sum(pw(xi, 2) for xi in x)
```
**Usage:**

```python
result = optimizer.cga(
    n_cols = 5,
    n_rows = 5,
    n_gen = 100,
    ch_size = 5,
    gen_type = GeneType.REAL,
    p_crossover = 0.9,
    p_mutation = 0.2,
    problem = ExampleProblem(),  # Replace with a real problem instance as needed
    selection = optimizer.TournamentSelection,
    recombination = optimizer.ByteOnePointCrossover,
    mutation = optimizer.ByteMutationRandom,
    mins = [-32.768] * 5,  # Minimum values for each gene
    maxs = [32.768] * 5    # Maximum values for each gene
)
print("Best solution:", result[1], "\nBest solution chromosome:", result[0])

# The result is 
# Best solution: 0.0 
# Best solution chromosome: [0.0, 0.0, 0.0, 0.0, 0.0]

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