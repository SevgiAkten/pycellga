# pycellga: A Python Package for Improved Cellular Genetic Algorithms

`pycellga` is a Python package that implements cellular genetic algorithms (CGAs) for optimizing complex problems. CGAs combine the principles of cellular automata and traditional genetic algorithms, utilizing a spatially structured population organized in a grid-like topology. This structure allows each individual to interact only with its neighboring individuals, promoting diversity and maintaining a balance between exploration and exploitation during the optimization process. `pycellga` has machine coded operators with byte implementations. Beside it has Alpha-male CGA, Machine Coded Compact CGA and Improved CGA with Machine Coded Operaors for real-valued optimization problems.

## Features

- **Cellular Genetic Algorithms (CGAs)**: Efficient implementation of CGAs with various built-in functions.
- **Machine-Coded Operators**: Includes byte-based and machine-coded operators for efficient numerical data handling.
- **Customizable**: Various customization options to suit different optimization problems.
- **Alpha-male CGA**: A specialized CGA variant.
- **Machine Coded Compact CGA**: Optimized for compact representations.
- **Improved CGA with Machine Coded Operators**: Enhanced performance for real-valued optimization problems.

## Installation

You can install `pycellga` via pip:

```bash
pip install pycellga
```

## Documentation

Comprehensive documentation is available on the official documentation site.

## Example 

Can we put a small code snipped here, for example finding the global minimum of Ackley function or something more interesting? It would also be nice to see more than one feature of the package with combining different algorithms and cases, e.g. different operators, byte-bit encodings, permutation, binary, or real, etc.

```python
# The function to be minimized
def f(x):
    return (x[0] - 3.14159264)**2 + (x[1] - 2.71828)**2

result = optimizer(f, ....)

# The result is 
# x[0] = 3.14159265
# x[1] = 2.71828
```

## Contributing

Contributions are welcome! Please read the contributing guidelines first.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Developed by Sevgi Akten Karakaya and Mehmet Hakan Satman.
Inspired by traditional genetic algorithms and cellular automata principles with machine coded operators.
For more information, please visit the project repository.