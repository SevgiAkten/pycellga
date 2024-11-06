Selection Operators
===============================

The `pycellga.selection` package provides various selection operators that determine how individuals are chosen from the population to act as parents in genetic algorithms. Selection operators play a key role in balancing exploration and exploitation during the optimization process, directly impacting convergence and diversity.


**Tournament Selection**
--------------

Implements a tournament selection method, where a subset of individuals competes, and the best-performing individual is selected as a parent. This method is useful in maintaining diversity and is effective in multimodal optimization landscapes.

.. automodule:: pycellga.selection.tournament_selection
   :members:
   :undoc-members:
   :show-inheritance:

**Roulette Wheel Selection**
--------------

Implements a roulette wheel selection mechanism where each individual’s chance of being selected is proportional to its fitness. This method is widely used for its simplicity and is effective in problems where fitness proportionate selection is beneficial.

.. automodule:: pycellga.selection.roulette_wheel_selection
   :members:
   :undoc-members:
   :show-inheritance:
