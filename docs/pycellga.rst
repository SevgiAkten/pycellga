pycellga: API Reference
========================

The `pycellga` package is a Python library for implementing and testing cellular genetic algorithms (CGAs). This guide provides an in-depth look at each module, offering descriptions and use cases to help users understand and utilize the library effectively.

.. toctree::
   :maxdepth: 1

   pycellga.neighborhoods
   pycellga.mutation
   pycellga.recombination
   pycellga.selection
   pycellga.problems
   pycellga.example


**Core Modules**
------------------

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
--------------

The core optimization module that manages the genetic algorithm's execution. This includes processes like selection, mutation, recombination, and evaluation of individuals. The `optimizer` module serves as the main interface for running different CGA variants.

.. automodule:: pycellga.optimizer
   :members:
   :undoc-members:
   :show-inheritance: