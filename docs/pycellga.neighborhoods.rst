Neighborhood Operators
==================================

The `pycellga.neighborhoods` module provides various neighborhood structures that define how individuals interact with their neighbors in the cellular genetic algorithm (CGA). These neighborhood operators are essential for managing the flow of information and maintaining diversity within the population.
Each neighborhood module defines a specific spatial structure. Depending on the problem and the desired interaction level, users can select different neighborhood sizes and arrangements.


**Linear 5**
--------------

Defines a linear neighborhood where each individual interacts with 5 neighbors arranged in a line. This structure is suitable for problems where limited, sequential interaction is beneficial.

.. automodule:: pycellga.neighborhoods.linear_5
   :members:
   :undoc-members:
   :show-inheritance:

**Linear 9**
--------------

A linear arrangement with 9 neighbors, encouraging a higher level of information flow along a line. This structure is ideal for applications that require extended sequential interactions.

.. automodule:: pycellga.neighborhoods.linear_9
   :members:
   :undoc-members:
   :show-inheritance:

**Compact 9**
--------------

A compact neighborhood structure with 9 neighbors. This layout offers dense interaction among individuals, facilitating rapid convergence while maintaining diversity.

.. automodule:: pycellga.neighborhoods.compact_9
   :members:
   :undoc-members:
   :show-inheritance:

**Compact 13**
--------------

Defines a compact neighborhood structure where each individual interacts with its immediate and extended neighbors in a 13 grid. This structure allows moderate information sharing across neighboring cells.

.. automodule:: pycellga.neighborhoods.compact_13
   :members:
   :undoc-members:
   :show-inheritance:

**Compact 21**
--------------

Provides a compact arrangement where individuals have a 21 neighborhood structure. This layout encourages local exploration and is useful in tightly clustered populations.

.. automodule:: pycellga.neighborhoods.compact_21
   :members:
   :undoc-members:
   :show-inheritance:

**Compact 25**
--------------

An extended compact neighborhood that includes more neighbors, with a 25 structure. This layout promotes broader information sharing, enhancing convergence in larger populations.

.. automodule:: pycellga.neighborhoods.compact_25
   :members:
   :undoc-members:
   :show-inheritance: