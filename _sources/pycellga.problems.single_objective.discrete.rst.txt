Discrete Optimization Problems
==========================================

The `pycellga.problems.single_objective.discrete` package contains discrete, single-objective optimization problems. These problems are specifically designed to evaluate optimization algorithms on discrete search spaces, where solutions are typically represented in binary or permutation forms. This package includes both binary-based and permutation-based subpackages, each tailored for different types of optimization tasks.


**Binary-Based Problems**
------------------------------
The `binary` subpackage contains a set of benchmark problems where solutions are represented as binary strings. These problems are widely used to test algorithms’ performance on discrete, combinatorial spaces with binary encoding. 

.. toctree::
   :maxdepth: 2

   pycellga.problems.single_objective.discrete.binary

**Permutation-Based Problems**
--------------------------------
The `permutation` subpackage focuses on problems where the solution is a permutation of elements, such as sequencing or ordering tasks. This subpackage is particularly useful for evaluating algorithms that work on combinatorial optimization problems, such as the Traveling Salesman Problem (TSP).

.. toctree::
   :maxdepth: 2

   pycellga.problems.single_objective.discrete.permutation
