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


date: 14 Aug 2024
bibliography: paper.bib
---

# Summary
`pycellga` is a Python package that implements cellular genetic algorithms (CGAs) for optimizing complex problems. CGAs combine the principles of cellular automata and traditional genetic algorithms, utilizing a spatially structured population organized in a grid-like topology. This structure allows each individual to interact only with its neighboring individuals, promoting diversity and maintaining a balance between exploration and exploitation during the optimization process.

While CGAs themselves are not a novel contribution of this work, `pycellga` significantly enhances their applicability by integrating advanced features and providing unparalleled versatility. The package supports binary, real-valued, and permutation-based optimization problems, making it adaptable to a wide variety of problem domains. Its use of machine-coded operators for real-valued optimization, adhering to IEEE 754 floating-point arithmetic standards, ensures high precision and computational efficiency. Moreover, `pycellga` is designed to be extensible, enabling users to easily customize selection, crossover, and mutation operators to suit specific problem requirements.

The package is designed to be user-friendly, with a straightforward installation process and comprehensive documentation. Researchers and practitioners in fields such as operations research, artificial intelligence, and machine learning can leverage `pycellga` to tackle complex optimization challenges effectively. By integrating the principles of cellular automata with genetic algorithms, `pycellga` represents a significant advancement in the field of evolutionary computation, offering increased flexibility and adaptability compared to traditional methods.

Additionally, `pycellga` includes machine-coded operators with byte implementations, developed by [@satman2013machine]. It features Alpha-male CGA, Machine-Coded Compact CGA, and Improved CGA with Machine-Coded Operators for real-valued optimization problems [@karakaya2024improved].


# Introduction

Optimization problems are a fundamental aspect of various scientific and engineering fields, involving the search for the best solution among a large set of possible options. Genetic algorithms (GAs) have been widely used to address these problems due to their robustness and adaptability. Inspired by the process of natural selection, GAs operate on a population of potential solutions, applying operators such as selection, crossover, and mutation to evolve the population toward better solutions over successive generations [@holland1975adaptation; @goldberg1989genetic].

Despite their effectiveness, traditional GAs face challenges, particularly in maintaining diversity within the population and avoiding premature convergence to suboptimal solutions [@goldberg1991comparative]. To mitigate these issues, researchers have developed cellular genetic algorithms (CGAs), which introduce a spatial structure to the population [@manderick1991genetic; @whitley1993cellular]. In a CGA, individuals are placed on a grid, and interactions are restricted to neighboring individuals. This localized interaction promotes diversity and enables a more thorough exploration of the solution space.

`pycellga` is a Python package designed to efficiently implement CGAs. By integrating the principles of cellular automata with genetic algorithms, `pycellga` offers a robust framework for tackling complex optimization problems. The `pycellga` package is designed to handle a wide range of optimization problems, including binary, real-valued, and permutation-based challenges, making it a versatile tool for diverse applications in evolutionary computation. The package includes several built-in functions for initialization, selection, crossover, mutation, and evaluation, as well as customization options to cater to different needs. This flexibility allows researchers and practitioners to apply CGAs to a wide range of problems with ease [@karakaya2024improved].

By providing a comprehensive toolkit for CGAs, `pycellga` aims to advance the field of evolutionary computation and equip researchers with the tools needed to solve increasingly complex optimization problems effectively. The integration of cellular automata with genetic algorithms in `pycellga` represents a significant advancement, offering greater flexibility and adaptability compared to traditional methods [@michalewicz1996genetic; @eiben2003introduction; @karakaya2024improved]. 

The `pycellga` package includes machine-coded operators with byte-level implementations, developed by [@satman2013machine]. In the context of genetic algorithms, "machine-coded" refers to a specialized encoding technique optimized for real-parameter optimization. This approach differs from standard coding practices by emphasizing efficient data processing through byte-level manipulation. Originally introduced by [@satman2013machine], this technique is particularly advantageous for real-valued optimization tasks, as it allows direct manipulation of byte-representations to enhance computational performance. Encoding and decoding of numerical values conform to the IEEE 754 standard for floating-point arithmetic, further improving precision and effectiveness in optimizing continuous functions. By using machine-coded operators, `pycellga` leverages this efficiency to handle complex optimization challenges more effectively.

In addition, the `pycellga` package features Alpha-male CGA, developed based on insights from [@satman2019alpha_male_ga]; Machine-Coded Compact CGA, inspired by [@satman2020machine_coded_cga]; and Improved CGA with Machine-Coded Operators [@karakaya2024improved]. The improved cellular genetic algorithm utilizes machine-coded operators specifically tailored for real-valued optimization problems. This method is particularly distinctive for its use of byte-based operators, which are designed to process numerical data efficiently in terms of memory usage.


# State of the field

There are several existing software packages that implement genetic algorithms, such as DEAP and PyGAD. These libraries provide a wide range of tools for evolutionary computation and are highly flexible for various optimization tasks. However, most of these packages do not specifically focus on the integration of cellular automata with genetic algorithms, except for JCell, which is a Java implementation of CGAs [@alba2008cellular]. 

The lack of CGA variants in widely used Python libraries may be attributed to the complexity and niche appeal of cellular genetic algorithms. CGAs, by design, require a spatially structured population and localized interactions, which add an extra layer of complexity compared to traditional GAs. Additionally, while traditional GAs are well-documented and widely adopted, CGAs have been primarily explored in academic research, with fewer applications in mainstream problem-solving scenarios. This may have led to limited adoption in general-purpose optimization libraries.

`pycellga` addresses this gap by offering a specialized toolkit for CGAs, leveraging the strengths of both cellular automata and genetic algorithms. By incorporating features such as Alpha-male CGA, Machine-Coded Compact CGA, and Improved CGA with Machine-Coded Operators, `pycellga` provides unparalleled support for tackling complex optimization problems. Its use of machine-coded operators, adhering to IEEE 754 floating-point arithmetic standards, ensures high precision and computational efficiency, making it a significant advancement in the field.

The introduction of `pycellga` represents a deliberate effort to bring CGA variants into broader usage, making these powerful algorithms more accessible to researchers and practitioners. By providing a Python-based implementation, `pycellga` bridges the gap between theoretical advancements in CGA research and their practical applications, thus addressing the limitations in existing software ecosystems.



# Statement of need 

The need for advanced optimization frameworks like `pycellga` arises from the growing complexity of real-world problems, which often involve high-dimensional search spaces, mixed-variable types, and intricate constraints. Traditional Genetic Algorithms (GAs), while highly versatile and widely adopted, face several limitations in addressing these challenges. These include a tendency toward premature convergence, difficulty in maintaining population diversity, and an inability to balance global exploration with local exploitation effectively [@holland1975adaptation; @goldberg1989genetic].

Cellular Genetic Algorithms (CGAs) offer a compelling solution by introducing a spatially structured population. In CGAs, individuals are arranged in a grid-like topology and interact only with their neighbors. This localized interaction not only enhances population diversity but also mitigates the risk of premature convergence, a common issue in traditional GAs [@manderick1991genetic; @whitley1993cellular]. By promoting a gradual spread of genetic material through localized selection and crossover, CGAs achieve a more thorough exploration of the solution space, particularly in high-dimensional and multi-modal optimization problems [@alba2008cellular]. These attributes make CGAs especially effective for tackling complex challenges in scheduling, resource allocation, and multi-objective optimization [@coello2007multiobjective].

Despite the clear advantages of CGAs, their implementation in existing tools remains limited. Frameworks such as JCell, while functional, lack the flexibility, extensibility, and user-friendly features offered by modern programming environments like Python [@alba2008cellular]. To address this gap, `pycellga` provides a Python-based framework that combines the strengths of CGAs with the convenience and power of Python's ecosystem. The package includes efficient byte-level implementations of machine-coded operators, as introduced by [@satman2013machine], which significantly enhance performance for real-valued optimization problems. Additionally, it incorporates advanced CGA variants, such as Alpha-male CGA [@satman2019alpha_male_ga], Machine-Coded Compact CGA [@satman2020machine_coded_cga], and an Improved CGA with Machine-Coded Operators [@karakaya2024improved].

The unique contributions of `pycellga` extend beyond its robust implementation of CGAs. By supporting binary, real-valued, and permutation-based optimization problems, the package offers unparalleled versatility. Its use of machine-coded operators for real-valued optimization, adhering to IEEE 754 floating-point arithmetic standards, ensures high precision and computational efficiency. Moreover, `pycellga` is designed to be extensible, enabling users to easily customize selection, crossover, and mutation operators to suit specific problem domains.

In a field where traditional GAs have seen extensive research to address their inherent limitations [@eiben2003introduction], CGAs provide a novel and effective approach to further these advancements. `pycellga` stands out as a modern, accessible, and feature-rich toolkit that equips researchers and practitioners to tackle increasingly complex optimization challenges with confidence.



# Installation and basic usage

`pycellga` can be downloaded and installed by using the following command:

```python
pip install pycellga
```
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
```
**Usage:**

```python
result = cga(
    n_cols=5,
    n_rows=5,
    n_gen=100,
    ch_size=5,
    gen_type=GeneType.REAL,
    p_crossover=0.9,
    p_mutation=0.2,
    problem=ExampleProblem(),  # Replace with a real problem instance as needed
    selection=TournamentSelection,
    recombination=ByteOnePointCrossover,
    mutation=ByteMutationRandom,
    mins=[-32.768] * 5,  # Minimum values for each gene
    maxs=[32.768] * 5,    # Maximum values for each gene
    seed_par=100  # Ensures the random number generation is repeatable
)

# Print the best solution details
print("Best solution chromosome:", result.chromosome)
print("Best fitness value:", result.fitness_value)

# Expected Output:
# Best solution chromosome: [0.0, 0.0, 0.0, 0.0, 0.0]
# Best fitness value: 0.0

```

# References
