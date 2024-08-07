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


date: 6 Aug 2024
bibliography: paper.bib
csl: apa.csl
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


# References
