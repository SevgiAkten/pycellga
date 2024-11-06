Binary Optimization Problems
========================================

The `pycellga.problems.single_objective.discrete.binary` package provides a set of binary, single-objective benchmark functions. These discrete problems are commonly used to assess the performance of optimization algorithms on binary-encoded solutions. Each function presents unique challenges, such as local optima, multimodality, and rugged landscapes.


**Count SAT**
--------------

A binary satisfaction problem, often used to evaluate an algorithm’s ability to solve constraint satisfaction problems in a discrete search space.

.. automodule:: pycellga.problems.single_objective.discrete.binary.count_sat
   :members:
   :undoc-members:
   :show-inheritance:

**ECC Problem**
--------------

The ECC problem tests the efficiency of algorithms in solving problems related to error-correcting codes, which have discrete solution spaces and are commonly encountered in communication systems.

.. automodule:: pycellga.problems.single_objective.discrete.binary.ecc
   :members:
   :undoc-members:
   :show-inheritance:

**Fletcher-Powell (FMS) Binary Problem**
--------------

A binary version of the Fletcher-Powell function, used to evaluate robustness and efficiency in finding optimal solutions within a binary space.

.. automodule:: pycellga.problems.single_objective.discrete.binary.fms
   :members:
   :undoc-members:
   :show-inheritance:

**Max-Cut (100 nodes)**
--------------

A max-cut problem involving 100 nodes, often used in graph partitioning. This problem challenges algorithms in finding optimal binary partitions.

.. automodule:: pycellga.problems.single_objective.discrete.binary.maxcut100
   :members:
   :undoc-members:
   :show-inheritance:

**Max-Cut (20 nodes, Density 0.1)**
--------------

A max-cut problem with 20 nodes and a sparsity factor of 0.1. Suitable for testing performance on sparse graphs with limited connections.

.. automodule:: pycellga.problems.single_objective.discrete.binary.maxcut20_01
   :members:
   :undoc-members:
   :show-inheritance:

**Max-Cut (20 nodes, Density 0.9)**
--------------

A denser version of the max-cut problem with a density of 0.9, requiring algorithms to manage numerous connections and find optimal partitions.

.. automodule:: pycellga.problems.single_objective.discrete.binary.maxcut20_09
   :members:
   :undoc-members:
   :show-inheritance:

**Multi-modal Deceptive Problem (MMDP)**
--------------

A challenging binary problem with deceptive local optima, commonly used to assess an algorithm's ability to escape local traps in a binary landscape.

.. automodule:: pycellga.problems.single_objective.discrete.binary.mmdp
   :members:
   :undoc-members:
   :show-inheritance:

**One-Max Problem**
--------------

A classic benchmark in binary optimization, where the objective is to maximize the number of ones in a binary string. This problem tests the algorithm's ability to drive binary values towards an optimum.

.. automodule:: pycellga.problems.single_objective.discrete.binary.one_max
   :members:
   :undoc-members:
   :show-inheritance:

**Peak Problem**
--------------

A binary optimization problem featuring multiple peaks. This problem is suitable for evaluating an algorithm’s performance in a rugged binary landscape with multiple local optima.

.. automodule:: pycellga.problems.single_objective.discrete.binary.peak
   :members:
   :undoc-members:
   :show-inheritance:
