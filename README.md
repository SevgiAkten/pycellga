[![Doc](https://img.shields.io/badge/docs-dev-blue.svg)](https://sevgiakten.github.io/pycellga/)
[![License](https://img.shields.io/github/license/SevgiAkten/pycellga)](https://github.com/SevgiAkten/pycellga/blob/main/LICENSE)
![Repo Size](https://img.shields.io/github/repo-size/SevgiAkten/pycellga)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![GitHub Contributors](https://img.shields.io/github/contributors/SevgiAkten/pycellga)
[![PyPI version](https://img.shields.io/pypi/v/pycellga.svg?cacheBuster=123456)](https://pypi.org/project/pycellga/)



# pycellga: A Python Package for Improved Cellular Genetic Algorithms

`pycellga` is a Python package that implements cellular genetic algorithms (CGAs) for optimizing complex problems. CGAs combine the principles of cellular automata and traditional genetic algorithms, utilizing a spatially structured population organized in a grid-like topology. This structure allows each individual to interact only with its neighboring individuals, promoting diversity and maintaining a balance between exploration and exploitation during the optimization process. `pycellga` has machine coded operators with byte implementations. Beside it has Alpha-male CGA, Machine Coded Compact CGA and Improved CGA with Machine Coded Operaors for real-valued optimization problems. The `pycellga` package is designed to handle a wide range of optimization problems, including binary, real-valued, and permutation-based challenges, making it a versatile tool for diverse applications in evolutionary computation.

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

For full documentation, visit [here](https://sevgiakten.github.io/pycellga/) or click the badge below:

[![Doc](https://img.shields.io/badge/docs-dev-blue.svg)](https://sevgiakten.github.io/pycellga/)


## Usage Examples

In this section, we'll explain cga method in the optimizer and provide an example of how to use it. The package includes various ready-to-use crossover and mutation operators, along with real-valued, binary, and permutation functions that you can run directly. Examples for other methods are available in the `example` folder, while an example for cga is provided below.

### **cga (Cellular Genetic Algorithm)**

**cga** is a type of genetic algorithm where the population is structured as a grid (or other topologies), and each individual interacts only with its neighbors. This structure helps maintain diversity in the population and can prevent premature convergence. To specialize the CGA for real-valued optimization problems, ICGA (Improved CGA) with machine-coded representation can be used, applying byte operators. The encoding and decoding of numbers follow the IEEE 754 standard for floating-point arithmetic, yielding better results for continuous functions.

## Example Problem

Suppose we have a problem that we want to minimize using a Cellular Genetic Algorithm (CGA). The problem is defined as a simple sum of squares function, where the goal is to find a chromosome (vector) that minimizes the function.

The sum of squares function computes the sum of the squares of each element in the chromosome. This function reaches its global minimum when all elements of the chromosome are equal to 0. The corresponding function value at this point is 0.

### ExampleProblem Class

Here’s how we can define this problem in Python using the `ExampleProblem` class:

```python
from mpmath import power as pw
import pycellga 

class ExampleProblem:
    
    def __init__(self):
        pass
    
    def f(self, x):
        
        return sum(pw(xi, 2) for xi in x)
```
**Usage:**

```python
result = pycellga.optimizer.cga(
    n_cols=5,
    n_rows=5,
    n_gen=100,
    ch_size=5,
    gen_type=pycellga.optimizer.GeneType.REAL,
    p_crossover=0.9,
    p_mutation=0.2,
    problem=ExampleProblem(),  # Replace with a real problem instance as needed
    selection=pycellga.optimizer.TournamentSelection,
    recombination=pycellga.optimizer.ByteOnePointCrossover,
    mutation=pycellga.optimizer.ByteMutationRandom,
    mins=[-32.768] * 5,  # Minimum values for each gene
    maxs=[32.768] * 5,    # Maximum values for each gene
    seed_par=100  # Ensures the random number generation is repeatable
)

# Print the best solution details
print("Best solution chromosome:", result.chromosome)
print("Best fitness value:", result.fitness_value)
print("Generation found:", result.generation_found)

# Expected Output:
# Best solution chromosome: [0.0, 0.0, 0.0, 0.0, 0.0]
# Best fitness value: 0.0
# Generation found: <generation_number>

```

We have provided a basic example above. If you're interested in exploring more examples, you have two options:

- [Click here to see the other examples](https://github.com/SevgiAkten/pycellga/tree/main/pycellga/example) available directly in the repository.
- [Please click here to see the documentation](https://sevgiakten.github.io/pycellga/pycellga.example.html#pycellga-example-package) for more detailed examples and explanations.


## Contributing

Contributions are welcome! Please read the contributing guidelines first.

## Testing

To ensure that `pycellga` works as expected, we have provided a comprehensive suite of tests. Follow these steps to run the tests locally:

1. **Install dependencies**: Make sure you have installed all the necessary dependencies from `requirements.txt`. You can install them using the following command:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run tests**: Navigate to the root directory of the project and run the test suite using `pytest`. 

    ```bash
    pytest
    ```

    This will automatically discover and execute all the test cases.

3. **Check code coverage** (Optional): You can check the test coverage of the package using `pytest-cov`. First, ensure you have installed `pytest-cov`:

    ```bash
    pip install pytest-cov
    ```

    Then, run the tests with coverage reporting:

    ```bash
    pytest --cov=pycellga
    ```

    A summary of code coverage will be displayed in the terminal.
    
4. **Generate coverage reports**: If you want a detailed HTML report of the code coverage, run:

    ```bash
    pytest --cov=pycellga --cov-report=html
    ```

    Open the `htmlcov/index.html` file in a web browser to view the detailed coverage report.

5. **Add new tests (if applicable)**:
    - If your changes introduce new features or modify existing functionality, write additional test cases to cover these changes.
    - Place your tests in the appropriate subdirectory within the `tests` folder, following the naming convention `test_<feature_name>.py`.

6. **Review testing guidelines**:
    - Ensure your tests follow the existing style and structure used in the project. Use descriptive function names and provide comments where necessary to clarify the test's purpose.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Developed by Sevgi Akten Karakaya and Mehmet Hakan Satman.
Inspired by traditional genetic algorithms and cellular automata principles with machine coded operators.
For more information, please visit the project repository.

## Citation

If you use `pycellga` in your research, please cite it as follows:

**APA Format**

Karakaya, S. A., & Satman, M. H. (2024). An Improved Cellular Genetic Algorithm with Machine-Coded Operators for Real-Valued Optimisation Problems. *Journal of Engineering Research and Applied Science, 13*(1), 2500-2514.

**BibTeX Format**

For LaTeX users, please use the following BibTeX entry to cite `pycellga`:

```bibtex
@article{karakaya2024improved,
  title={An Improved Cellular Genetic Algorithm with Machine-Coded Operators for Real-Valued Optimisation Problems},
  author={Karakaya, Sevgi Akten and Satman, Mehmet Hakan},
  journal={Journal of Engineering Research and Applied Science},
  volume={13},
  number={1},
  pages={2500--2514},
  year={2024}
}
