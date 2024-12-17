Problem Definitions
===============================

The `pycellga.problems` package provides a collection of problem definitions for optimization tasks. Each problem is structured as a class inheriting from a common abstract base, ensuring consistency and flexibility across various types of optimization tasks. This module includes single-objective problems, designed to serve as benchmarks or examples for testing and applying genetic algorithms.


**AbstractProblem Class**
------------------------------

The `AbstractProblem` class is an abstract base class designed to standardize the definition of optimization problems within the `pycellga` framework. It integrates seamlessly with the **pymoo** optimization library and provides a consistent structure for implementing custom problem definitions.

Key Features
------------

- **Gene Type Specification**: 
  The `gen_type` attribute allows users to define the type of genes (`REAL`, `BINARY`, etc.), ensuring flexibility for various problem domains.
  
- **Design Variable Management**: 
  Users can define the number of variables (`n_var`) and their bounds (`xl` and `xu`), accurately capturing the problem's decision space.

- **Abstract Fitness Function**: 
  The `f` method must be implemented in subclasses to compute the fitness of a solution, serving as the core of any optimization problem.

- **Compatibility with Optimizers**: 
  The `evaluate` method ensures smooth integration with `pymoo` optimizers, handling batch evaluations and storing results efficiently.

Attributes
----------

- **`gen_type`**: Specifies the gene type for the problem (e.g., `REAL`, `BINARY`).
- **`n_var`**: Number of design variables in the problem.
- **`xl` and `xu`**: Lower and upper bounds for each design variable, provided as lists or arrays.

Methods
-------

- **`f(x: List[Any]) -> float`**:
  Abstract method for computing the fitness of a solution. This must be implemented in derived classes.

- **`evaluate(x, out, *args, **kwargs)`**:
  A method compatible with `pymoo` optimizers that wraps the `f` method and stores computed fitness values in an output dictionary.

Example
-------

Below is an example of how to create a custom optimization problem by inheriting from `AbstractProblem`:

.. code-block:: python

   from pycellga.problems.abstract_problem import AbstractProblem
   from pycellga.common import GeneType

   from typing import List
   import numpy as np

   class MyProblem(AbstractProblem):
       def __init__(self):
           super().__init__(gen_type=GeneType.REAL, n_var=10, xl=10, xu=10)

       def f(self, x: List[float]) -> float:
           # Example fitness function: Sphere function
           return np.sum(np.square(x))

This structure simplifies the process of defining optimization problems, enabling experimentation with diverse formulations while ensuring compatibility with modern optimization libraries.


**API References**
------------------

.. automodule:: pycellga.problems.abstract_problem
   :members:
   :undoc-members:
   :show-inheritance:

**Single-Objective Problems**
------------------------------
The `single_objective` subpackage includes a set of benchmark functions commonly used to evaluate optimization algorithms in terms of convergence speed, accuracy, and robustness. These problems are designed for scenarios where only one objective needs to be optimized.

.. toctree::
   :maxdepth: 2

   pycellga.problems.single_objective
