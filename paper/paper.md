---
title: 'pycellga: A Python package for improved cellular genetic algorithms'
tags:
  - Python
  - genetic algorithms
  - cellular automaton
authors:
  - name: Sevgi Akten Karakaya
    orcid: 0000-0001-9346-5795
    affiliation: 1
  - name: Mehmet Hakan Satman
    orcid: 0000-0002-9402-1982
    affiliation: 2
affiliations:
  - name: Department of Informatics, Istanbul University, Istanbul, Turkey
    index: 1
  - name: Department of Econometrics, Istanbul University, Istanbul, Turkey
    index: 2


date: 9 Aug 2024
bibliography: paper.bib
---

# Summary
`pycellga` is a `Python` package that implements cellular genetic algorithms (CGAs) for optimizing complex problems. CGAs combine the principles of cellular automata and traditional genetic algorithms, utilizing a spatially structured population organized in a grid-like topology. This structure allows each individual to interact only with its neighboring individuals, promoting diversity and maintaining a balance between exploration and exploitation during the optimization process.

The package is designed to be user-friendly, with a straightforward installation process and comprehensive documentation. Researchers and practitioners in fields such as operations research, artificial intelligence, and machine learning can leverage `pycellga` to tackle complex optimization challenges effectively. The integration of cellular automata with genetic algorithms in `pycellga` represents a significant advancement in the field of evolutionary computation, offering enhanced performance and versatility compared to traditional methods. `pycellga` has also machine coded operators with byte implementations which is developed by [@satman2013machine]. Beside it has Alpha-male CGA, Machine Coded Compact CGA and Improved CGA with Machine Coded Operaors for real-valued optimization problems [@karakaya2024improved].

# Introduction

Optimization problems are a fundamental aspect of various scientific and engineering fields, involving the search for the best solution among a large set of possible options. Genetic algorithms (GAs) have been widely used to address these problems due to their robustness and adaptability. Inspired by the process of natural selection, GAs operate on a population of potential solutions, applying operators such as selection, crossover, and mutation to evolve the population towards better solutions over successive generations [@holland1975adaptation; @goldberg1989genetic].

Despite their effectiveness, traditional GAs face challenges, particularly in maintaining diversity within the population and avoiding premature convergence to suboptimal solutions [@goldberg1991comparative]. To mitigate these issues, researchers have developed cellular genetic algorithms (CGAs), which introduce a spatial structure to the population [@manderick1989genetic; @whitley1993cellular]. In a CGA, individuals are placed on a grid, and interactions are restricted to neighboring individuals. This localized interaction promotes diversity and enables a more thorough exploration of the solution space.

`pycellga` is a Python package designed to implement CGAs efficiently. By integrating the principles of cellular automata with genetic algorithms, `pycellga` offers a robust framework for tackling complex optimization problems. The package includes several built-in functions for initialization, selection, crossover, mutation, and evaluation, as well as customization options to cater to different needs. This allows researchers and practitioners to apply CGAs to a wide range of problems with ease [@karakaya2024improved].

By providing a comprehensive toolkit for CGAs, `pycellga` aims to advance the field of evolutionary computation and equip researchers with the tools needed to solve increasingly complex optimization problems effectively. The integration of cellular automata with genetic algorithms in `pycellga` represents a significant advancement, offering enhanced performance and versatility compared to traditional methods [@michalewicz1996genetic; @eiben2003introduction; @karakaya2024improved]. `pycellga` has machine coded operators with byte implementations which is developed by [@satman2013machine]. Beside it has Alpha-male CGA, Machine Coded Compact CGA and Improved CGA with Machine Coded Operators [@karakaya2024improved]. An improved cellular genetic algorithm that uses machine-coded operators specifically designed for real-valued optimization problems. This method stands out by employing byte-based operators, which are crafted to process numerical data efficiently in terms of memory usage.


# State of the field

There are several existing software packages that implement genetic algorithms, such as DEAP and PyGAD. However, most of these packages do not specifically focus on the integration of cellular automata with genetic algorithms except for JCell which is Java implementation of CGAs [@alba2008cellular]. `pycellga` addresses this gap by offering a specialized toolkit for CGAs, leveraging the strengths of both methodologies. `pycellga`  includes machine-coded operators with byte-level implementations. Additionally, it features methods such as Alpha-male CGA, Machine Coded Compact CGA, and Improved CGA with Machine Coded Operators.

# Statement of need 

The need for `pycellga` arises from the increasing complexity of optimization problems and the limitations of traditional genetic algorithms in handling these complexities. By incorporating cellular automata, `pycellga` introduces localized interactions and diversity within the population, which can lead to more effective and efficient solutions. This package is particularly useful for researchers and practitioners who wish to explore advanced genetic algorithm techniques. `pycellga` includes machine-coded operators with byte-level implementations developed by [@satman2013machine]. Additionally, it features Alpha-male CGA, Machine Coded Compact CGA and an Improved CGA with Machine Coded Operators for real valued optimization problems [@karakaya2024improved].

# Installation and basic usage

`pycellga` can be downloaded and installed by using the following command:

```python
pip install pycellga
```
## Usage Examples

In this section, we'll explain what each method in the optimizer does and provide examples of how to use them. The package includes various ready-to-use crossover and mutation operators, along with Real-valued, Binary, and Permutation functions that you can run directly —examples are available in the `main.py` file. Please configure the `gen_type` attribute as `Real-valued`, `Binary`, or `Permutation` according to the type of problem you want to solve.

### 1. **cga (Cellular Genetic Algorithm)**

**cga** is a type of genetic algorithm where the population is structured as a grid (or other topologies) and each individual interacts only with its neighbors. This structure helps maintain diversity in the population and can prevent premature convergence. To convert it from classcical cga into a specialized algorithm, ICGA (Improved CGA) with machine-coded representation for real-valued problems, you should use byte operators. The formulation for encoding and decoding numbers was created by an algorithm specified in the IEEE 754 – IEEE Standards for Floating-Point Arithmetic. This approach yields better results for continuous functions.

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


# References
