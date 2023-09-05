from problems.abstract_problem import AbstractProblem

# Massively Multimodal Deceptive Problem (MMDP)
"""
References
    
    1.Goldberg, D. E., Deb, K., & Horn, J. (1992, April). Massive Multimodality, Deception, and Genetic Algorithms. In PPSN (Vol. 2).

    2. Alba, E., Giacobini, M., Tomassini, M., & Romero, S. (2002). Comparing synchronous and asynchronous cellular genetic algorithms. In Parallel Problem Solving from Nature—PPSN VII: 7th International Conference Granada, Spain, September 7–11, 2002 Proceedings 7 (pp. 601-610). Springer Berlin Heidelberg.

    3. Giacobini, M., Preuss, M., & Tomassini, M. (2006). Effects of Scale-Free and Small-World Topologies on Binary Coded Self-adaptive CEA. Lecture Notes in Computer Science, 86-98.

    """

# Length of chromosomes = 240
# Maximum Fitness Value = 40


class Mmdp(AbstractProblem):

    def f(self, x: list) -> float:

        subproblems_length = 6
        subproblems_number = 40
        total_ones = 0
        partial_fitness = 0.0
        fitness = 0.0

        for i in range(subproblems_number):
            total_ones = 0
            for j in range(subproblems_length):
                if (x[i * subproblems_length + j]) == 1:
                    total_ones += 1

            if (total_ones == 0 or total_ones == 6):
                partial_fitness = 1.0
            elif (total_ones == 1 or total_ones == 5):
                partial_fitness = 0.0
            elif (total_ones == 2 or total_ones == 4):
                partial_fitness = 0.360384
            elif (total_ones == 3):
                partial_fitness = 0.640576

            fitness = fitness + partial_fitness

        fitness_normalized = fitness/40

        return round(fitness_normalized, 3)
