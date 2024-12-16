Selection Operators
=====================

The `pycellga.selection` module provides selection operators that determine how individuals are chosen from the population to act as parents in genetic algorithms. These operators play a critical role in balancing exploration and exploitation during the optimization process, directly impacting convergence and diversity.

**Selection Mechanism**
------------------------

Selection in genetic algorithms determines which individuals contribute their genetic material to the next generation. The choice of selection mechanism can significantly influence the algorithm's performance, impacting how quickly the population converges and whether diversity is preserved.

**Importance of Selection**

- **Exploration**: Encourages searching new areas in the solution space.
- **Exploitation**: Focuses on refining solutions near already known good solutions.


**Selection Example**
------------------------

**Roulette Wheel Selection**

Roulette Wheel Selection resembles the classic roulette wheel game. As shown in the diagram below, each chromosome occupies a portion of the wheel proportional to its fitness value. After a fixed point on the wheel is chosen, the roulette wheel is spun. The individual whose section aligns with the fixed point is selected. The higher the fitness value of an individual, the greater their chance of being chosen.

.. image:: images/roulette_wheel_selection.png
   :scale: 50%
   :align: center
   :alt: Roulette Wheel Selection Example

Figure 1: An example of Roulette Wheel Selection.


**API References**
------------------

The following sections provide detailed documentation for the selection operators available in the `pycellga.selectlon` package.

**Tournament Selection**
^^^^^^^^^^^^^^^^^^^^^^^^^^

Implements a tournament selection method, where a subset of individuals competes, and the best-performing individual is selected as a parent. This method is useful in maintaining diversity and is effective in multimodal optimization landscapes.

.. automodule:: pycellga.selection.tournament_selection
   :members:
   :undoc-members:
   :show-inheritance:

**Roulette Wheel Selection**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Implements a roulette wheel selection mechanism where each individual’s chance of being selected is proportional to its fitness. This method is widely used for its simplicity and is effective in problems where fitness proportionate selection is beneficial.

.. automodule:: pycellga.selection.roulette_wheel_selection
   :members:
   :undoc-members:
   :show-inheritance:
