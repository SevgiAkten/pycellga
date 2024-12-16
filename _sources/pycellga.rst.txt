Components of pycellga
=======================

`pycellga` is a comprehensive Python library designed for implementing and experimenting with **cellular genetic algorithms (CGAs)**. CGAs are evolutionary algorithms characterized by structured populations and localized interactions, making them suitable for a wide range of optimization problems. This guide provides a detailed breakdown of each module within `pycellga`, highlighting their purpose, key features, and practical use cases.

.. toctree::
   :maxdepth: 1

   pycellga.neighborhoods
   pycellga.mutation
   pycellga.recombination
   pycellga.selection
   pycellga.problems
   pycellga.example


**Core Modules API Refences**
------------------------------

Population Management
----------------------

Handles the initialization and management of the population in CGA. It includes methods for population updates, replacement, and neighborhood interactions within the grid structure.

.. automodule:: pycellga.population
   :members:
   :undoc-members:
   :show-inheritance:


Individual Representation
--------------------------

Represents an individual in the population, encapsulating attributes like the chromosome and fitness value. This module provides the fundamental building blocks for individuals used within the CGA framework.

.. automodule:: pycellga.individual
   :members:
   :undoc-members:
   :show-inheritance:


Grid Structure
--------------

Defines the grid structure for the cellular genetic algorithm. The grid layout restricts interactions to neighboring individuals, which helps maintain population diversity and allows for more controlled exploration.

.. automodule:: pycellga.grid
   :members:
   :undoc-members:
   :show-inheritance:


Byte Operators
--------------

Implements low-level byte-based operations that support machine-coded genetic algorithms. These operators are used for efficient encoding and decoding of chromosome data, enhancing the speed and memory usage for real-valued optimizations.

.. automodule:: pycellga.byte_operators
   :members:
   :undoc-members:
   :show-inheritance:



Optimizer
===========

The `pycellga.optimizer` module is the core component of the library, responsible for managing the execution of cellular genetic algorithms (CGAs). It integrates key evolutionary processes such as selection, mutation, recombination, and evaluation. The optimizer module also provides flexibility to implement and experiment with different CGA variants, each suited to specific optimization challenges.



**Cellular Genetic Algorithm (cga)**
-------------------

The standard Cellular Genetic Algorithm (cga) operates with a fixed neighborhood structure and asynchronous updates. This approach provides robust performance for a wide range of problems, leveraging local interactions to explore the search space efficiently.

.. image:: images/cga.png
   :scale: 50%
   :align: center
   :alt: Standard CGA Example

Figure 1: Illustration of the standard CGA process.


**Synchronous Cellular Genetic Algorithm (sync_cga)**
-------------------

Synchronous CGA (sync_cga) updates the entire population simultaneously in each generation. This ensures consistent progress across the population but may lead to premature convergence in some cases.


**Alpha Male Cellular Genetic Algorithm (alpha_cga)**
-------------------

This strategy developed to enhance the performance of Cellular Genetic Algorithms is the Alpha-Male Cellular Genetic Algorithm (alpha_cga). Alpha-Male Genetic Algorithm divides individuals in a population into social groups. A social group consists of females that select the same alpha male. In each social group, one individual is labeled as the alpha male, while the rest are productive females.

In their research, scientists integrated the alpha-male structure into the genetic algorithm and conducted simulation studies on some test functions. As a result, the new algorithm was observed to produce better outcomes compared to classical genetic algorithms. Similarly, this algorithm was developed by integrating a structure that allows a certain number of alpha male individuals in the population to pair with a defined number of female individuals into the Cellular Genetic Algorithm structure.

However, due to its inherent structure, Cellular GA is already limited to pairing with neighbors. Although directly combining the cellular structure with the alpha-male algorithm is not possible, a new structure incorporating both approaches is illustrated in the following figure:

.. image:: images/alpha_cga.png
   :scale: 50%
   :align: center
   :alt: Alpha CGA Example

Figure 2: Integration of alpha-male structure into Cellular Genetic Algorithm.

**Improved CGA with Machine-Coded Operators**
------------------------------------------------

Enhanced performance in real-valued optimization problems is achieved through the use of `machine-coded byte operators`. This approach focuses on leveraging the representation of numerical data in memory to improve the efficiency and accuracy of genetic algorithms.


**Understanding Machine-Coded (Byte) Genetic Operators**

In computer programs, numerical data is typically stored in memory as byte sequences. A byte consists of eight bits, each capable of holding a value of zero or one. For small numbers, a few bytes suffice, but larger numbers or those requiring higher precision need more bytes. This problem is mitigated by the use of data types in compilers and interpreters.

The storage of a numerical value in memory involves a finite number of bytes, implying that representing real values with absolute precision is impossible. As the number of bytes increases, so does precision, allowing for a more accurate representation of real values. The byte sequence shown in Table 1 was generated using a formulation algorithm specified in the IEEE 754 Standard for Floating-Point Arithmetic. Compilers commonly implement this standard when converting real numbers to and from byte sequences.

For instance, consider a variable `f` with a numerical value accurate to 15 decimal places:

f = 12.508239423942167

When the variable f is converted to bytes, an 8-element byte array is obtained, each of which ranges from 0 to 255. This byte array is shown in Table 1.

.. image:: images/f_byte.png
   :scale: 50%
   :align: center
   :alt: f example

Table 1: Byte representation of variable f.

As shown in Figure 3, traditional crossover operators can be directly applied to the byte representation of real values.

.. image:: images/icga.png
   :scale: 50%
   :align: center
   :alt: f example

Figure 3: Application of traditional traversal operators to byte arrays


**Machine-Coded Compact Cellular Genetic Algorithm (mcccga)**
-------------------------------------------------------------

The Machine-Coded Compact Cellular Genetic Algorithm (mcccga) is a specialized approach to solving real-valued optimization problems by combining the principles of compact genetic algorithms and cellular structures. This method is particularly effective for memory-efficient optimization in large solution spaces.

**Overview of Compact Genetic Algorithm**

Compact Genetic Algorithms are evolutionary algorithms designed to efficiently handle binary-encoded representations of solutions. Instead of maintaining a population of solutions, cGA uses a **probability vector** to represent the population's characteristics. Each element of the vector corresponds to the probability of a particular bit being `1` at a specific position in the solution space.

Key features of Compact GA:

- **Compact Representation**: Uses a probability vector instead of a full population.
- **Efficient Updates**: Updates the vector through a compact rule based on fitness comparisons.
- **Memory Efficiency**: Requires significantly less memory than classical genetic algorithms.

**Transition to Machine-Coded Compact GA**

Building on the compact GA framework, **Machine-Coded Compact GA** extends the algorithm to real-valued optimization problems by leveraging the IEEE 754 standard for floating-point arithmetic. Real-valued variables are encoded into binary form and processed using the cGA principles. When needed, the binary representation is decoded back to real values using the same standard.

**Integration with Cellular Structures**

The Machine-Coded Compact Cellular GA adapts the compact GA principles to a cellular structure, where each individual interacts with its neighbors. This adaptation enables local exploration and facilitates parallelism in optimization.

Key enhancements:

- **Real-Valued Adaptation**: Compact GA is extended to handle real-valued problems through encoding and decoding of variables.
- **Cellular Structure**: Implements a grid-based interaction model, enhancing local exploration and reducing premature convergence.
- **Dynamic Probability Updates**: Starts with a narrowed probability vector based on the variable's range, improving convergence speed.

In Figure 4, a sample coding of the number -12345.6789 with 1 bit for the sign part, 8 bits for the exponent part and 23 bits for the decimal part, totaling 32 bits, is realized according to the IEEE-754 standard.

.. image:: images/ieee.png
   :scale: 50%
   :align: center
   :alt: MMCGA Illustration

Figure 4: Encoding the number according to the IEEE-754 standard.


**API References**
-------------------

The following section provides the API reference for the `pycellga.optimizer` module.

.. automodule:: pycellga.optimizer
   :members:
   :undoc-members:
   :show-inheritance:
