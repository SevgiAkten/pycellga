Recombination Operators
===================================

Recombination (crossover) is a fundamental genetic algorithm operator that combines the genetic information of two parents to generate new offspring. The choice of a recombination operator depends on the chromosome representation (binary, real-valued, or permutation-based) and the nature of the optimization problem.


**Understanding Recombination**
--------------------------------

Recombination operators promote diversity and exploration in the solution space. They allow offspring to inherit traits from both parents, which can lead to better solutions over generations.

Below are some common recombination techniques used in genetic algorithms:

- **Binary Chromosomes**: Techniques like One-Point Crossover and Uniform Crossover are well-suited for binary representations, where each gene is a bit (0 or 1).
- **Real-Valued Chromosomes**: Methods such as Byte One Point Crossover, Arithmetic Crossover and BLX-Alpha Crossover facilitate exploration in continuous domains.
- **Permutation-Based Chromosomes**: Operators like PMX (Partially Matched Crossover) ensure valid offspring while preserving order relationships in sequencing problems.


**Recombination Examples**
--------------------------

**One-Point Crossover**

One-Point Crossover is one of the simplest and most widely used techniques for binary chromosomes. A random crossover point is selected, and segments from the parents are swapped to create offspring.

.. image:: images/one_point_c.png
   :scale: 50%
   :align: center
   :alt: One-Point Crossover

Figure 1: An example of One-Point Crossover.


**Two-Point Crossover**

Two-Point Crossover extends the idea of One-Point Crossover by selecting two random crossover points. The segment between the two points is swapped between the parents, producing offspring with potentially more diverse genetic combinations.

.. image:: images/two_point_c.png
   :scale: 50%
   :align: center
   :alt: Two-Point Crossover

Figure 2: An example of Two-Point Crossover.


**Uniform Crossover**

In Uniform Crossover, a mask composed of bits is determined over the length of the chromosome. These bits, which take the value 0 or 1, specify which parent the gene for the offspring will be chosen from. Bits with the value 1 are distributed uniformly with a probability of 0.5.

For example, as illustrated below, bits in the mask with a 0 value indicate that the gene will be selected from Parent X, while bits with a 1 value indicate that the gene will be selected from Parent Y. The reverse process is applied to produce the second offspring.

.. image:: images/uniform_c.png
   :scale: 50%
   :align: center
   :alt: Uniform Crossover

Figure 3: An example of Uniform Crossover.


**API References**
------------------

The following sections provide detailed documentation for the recombination operators available in the `pycellga.recombination` package.

**Arithmetic Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.arithmetic_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**BLX-Alpha Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.blxalpha_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Byte One-Point Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.byte_one_point_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Byte Uniform Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.byte_uniform_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Flat Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.flat_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Linear Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.linear_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**One-Point Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.one_point_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Partially Matched Crossover (PMX)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.pmx_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Two-Point Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.two_point_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Unfair Average Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.unfair_avarage_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Uniform Crossover**
^^^^^^^^^^^^^^^^^^^^^^^^
.. automodule:: pycellga.recombination.uniform_crossover
   :members:
   :undoc-members:
   :show-inheritance:
