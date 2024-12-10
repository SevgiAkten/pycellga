Single-Objective Optimization Problems
==================================================

The `pycellga.problems.single_objective` package includes a diverse collection of single-objective optimization problems. These problems are commonly used to benchmark and evaluate the performance of optimization algorithms. The package is organized into two main subpackages, each addressing different types of problem structures: continuous and discrete.

**Continuous Optimization Problems**
---------------------------------------
The `continuous` subpackage provides a set of continuous benchmark functions designed to evaluate algorithms on continuous search spaces. These functions are ideal for testing an algorithm’s performance in terms of accuracy, convergence speed, and robustness on smooth, differentiable landscapes.

.. toctree::
   :maxdepth: 2

   pycellga.problems.single_objective.continuous

**Discrete Optimization Problems**
-----------------------------------
The `discrete` subpackage includes binary and permutation-based problems where solutions are represented as discrete values or permutations. This subpackage is particularly useful for assessing algorithms that handle combinatorial and discrete optimization challenges.

.. toctree::
   :maxdepth: 2

   pycellga.problems.single_objective.discrete
