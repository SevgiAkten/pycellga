Mutation Operators
==============================

The `pycellga.mutation` module provides a comprehensive set of mutation operators designed to introduce variation into the population during the genetic algorithm optimization process. Each operator serves a unique purpose based on the representation of the chromosome (binary, real-valued, or permutation-based) and the specific requirements of the optimization problem.

This module includes the following mutation operators:

**Bit Flip Mutation**
------------------------------

Applies a bitwise flip to binary-encoded chromosomes. This operator is a classic choice for binary genetic algorithms, offering a simple yet effective mutation approach.

.. automodule:: pycellga.mutation.bit_flip_mutation
   :members:
   :undoc-members:
   :show-inheritance:

**Byte-Level Mutation**
------------------------------

Performs mutations at the byte level for real-valued chromosomes. This operator leverages byte manipulation to create small, precise adjustments in the solution space, optimizing the algorithm's performance for continuous functions.

.. automodule:: pycellga.mutation.byte_mutation
   :members:
   :undoc-members:
   :show-inheritance:

**Randomized Byte Mutation**
------------------------------

Introduces randomness at the byte level, enabling broader exploration in real-valued optimization tasks. This operator is particularly effective when a high degree of variation is desirable.

.. automodule:: pycellga.mutation.byte_mutation_random
   :members:
   :undoc-members:
   :show-inheritance:

**Uniform Float Mutation**
------------------------------

Applies uniform random mutations across real-valued chromosomes. This operator is suitable for continuous optimization, where each gene is adjusted within a defined range to enhance solution diversity.

.. automodule:: pycellga.mutation.float_uniform_mutation
   :members:
   :undoc-members:
   :show-inheritance:

**Insertion-Based Mutation**
------------------------------

A mutation strategy tailored for permutation-based representations, such as in sequencing and scheduling problems. This operator repositions a randomly selected gene within the chromosome, altering the order while preserving elements.

.. automodule:: pycellga.mutation.insertion_mutation
   :members:
   :undoc-members:
   :show-inheritance:


**Shuffle Mutation**
------------------------------

Randomly rearranges a subset of genes in the chromosome. This operator is effective in permutation-based problems, promoting diversity by shuffling segments without altering individual gene values.

.. automodule:: pycellga.mutation.shuffle_mutation
   :members:
   :undoc-members:
   :show-inheritance:

**Swap Mutation**
-------------------

Swaps the positions of two genes, introducing subtle changes ideal for permutation-based optimizations. This operator is commonly applied in combinatorial problems where order is significant.

.. automodule:: pycellga.mutation.swap_mutation
   :members:
   :undoc-members:
   :show-inheritance:

**Two-Opt Mutation**
----------------------

A mutation operator frequently used in path optimization problems, such as the Traveling Salesman Problem. It reverses a segment of the chromosome, allowing for new path configurations without altering the gene order.

.. automodule:: pycellga.mutation.two_opt_mutation
   :members:
   :undoc-members:
   :show-inheritance:

