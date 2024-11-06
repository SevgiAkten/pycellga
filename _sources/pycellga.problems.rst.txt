Problem Definitions
===============================

The `pycellga.problems` package provides a collection of problem definitions for optimization tasks. Each problem is structured as a class inheriting from a common abstract base, ensuring consistency and flexibility across various types of optimization tasks. This module includes both single-objective and multi-objective problems, designed to serve as benchmarks or examples for testing and applying genetic algorithms.


**Abstract Problem Base**
--------------

This module defines an abstract base class, `AbstractProblem`, which provides a standard interface for defining optimization problems. By inheriting from this base class, users can create custom problem definitions that are compatible with the rest of the `pycellga` framework. Key components of the base class include methods for evaluating objective values, setting constraints, and managing design variables.

.. automodule:: pycellga.problems.abstract_problem
   :members:
   :undoc-members:
   :show-inheritance:

**Single-Objective Problems**
--------------
The `single_objective` subpackage includes a set of benchmark functions commonly used to evaluate optimization algorithms in terms of convergence speed, accuracy, and robustness. These problems are designed for scenarios where only one objective needs to be optimized.

.. toctree::
   :maxdepth: 2

   pycellga.problems.single_objective
