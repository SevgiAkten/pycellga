Recombination Operators
===================================

The `pycellga.recombination` package includes various recombination (crossover) operators used to combine genetic information from parent chromosomes to create offspring in genetic algorithms. Each crossover operator serves a unique purpose and is suitable for different types of genetic representations, including binary, real-valued, and permutation-based chromosomes.



**Arithmetic Crossover**
-------------------------

Performs arithmetic operations on parent genes to produce offspring. Often used in real-valued genetic algorithms to create intermediate values between parent genes.

.. automodule:: pycellga.recombination.arithmetic_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**BLX-Alpha Crossover**
------------------------

Generates offspring by creating genes within a specified range around parent genes, controlled by the `alpha` parameter. Effective in real-valued optimization for maintaining diversity.

.. automodule:: pycellga.recombination.blxalpha_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Byte One-Point Crossover**
------------------------------

A one-point crossover operator specifically designed for byte-based chromosomes, suitable for machine-coded genetic algorithms.

.. automodule:: pycellga.recombination.byte_one_point_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Byte Uniform Crossover**
---------------------------

Applies uniform crossover at the byte level, allowing fine control over gene mixing in machine-coded chromosomes.

.. automodule:: pycellga.recombination.byte_uniform_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Flat Crossover**
-------------------

Creates offspring by generating random values within a range defined by the parent genes. Suitable for real-valued chromosomes.

.. automodule:: pycellga.recombination.flat_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Linear Crossover**
---------------------

Generates offspring by linearly combining genes of the parents. This operator is useful in real-valued optimization for exploring intermediate values.

.. automodule:: pycellga.recombination.linear_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**One-Point Crossover**
------------------------

A classic crossover technique where a single crossover point is chosen to swap segments between parents. Commonly used in binary-encoded genetic algorithms.

.. automodule:: pycellga.recombination.one_point_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Partially Matched Crossover (PMX)**
---------------------------------------

A crossover method designed for permutation-based chromosomes, such as sequencing problems. Maintains gene order by partially matching segments between parents.

.. automodule:: pycellga.recombination.pmx_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Two-Point Crossover**
------------------------

A crossover method with two crossover points, allowing for a higher level of gene exchange between parents. Widely used in binary-encoded algorithms.

.. automodule:: pycellga.recombination.two_point_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Unfair Average Crossover**
------------------------------

Calculates the average of parent genes with a slight bias, leading to offspring that retain more traits of one parent. Used in real-valued genetic algorithms.

.. automodule:: pycellga.recombination.unfair_avarage_crossover
   :members:
   :undoc-members:
   :show-inheritance:

**Uniform Crossover**
----------------------

Swaps genes randomly between parents, creating diverse offspring. Suitable for both binary and real-valued genetic representations.

.. automodule:: pycellga.recombination.uniform_crossover
   :members:
   :undoc-members:
   :show-inheritance: