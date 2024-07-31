from problems.abstract_problem import AbstractProblem

"""
    The Error Correcting Codes Design Problem (ECC) is a benchmark function used in optimization problems related to 
    the design and performance of error-correcting codes. The objective of the ECC function is to optimize the parameters 
    and structure of error-correcting codes to achieve desirable properties such as error detection and correction capabilities, 
    code length, and redundancy. The function evaluates an algorithm's ability to navigate through complex design spaces, 
    balance various trade-offs, and converge to optimal or near-optimal code designs. The ECC problem is particularly useful 
    for assessing the performance of optimization techniques in solving real-world problems related to coding theory and 
    communication systems.

    References
    Alba, E. and Dorronsoro B., 2008, Cellular genetic algorithms, Operations research/computer science interfaces series, Springer, US, ISBN: 978-0-387-77609-5.
"""
# Length of chromosomes = 144
# Maximum Fitness Value = 0.0674
# there is a bug that it find sometimes the fitness is bigger than the max, how it can be possible not solved yet

class Ecc(AbstractProblem):
    def f(self, x: list) -> float:

        individual_length = 12
        half_code = 12
        partial_fitness = 0.0
        hamming = 0
        fitness = 0.0

        for i in range(half_code):
            partial_fitness = partial_fitness + 1.0 / \
                (individual_length*individual_length)
            for j in range(half_code):
                if (j != i):
                    hamming = 1
                    for k in range(individual_length):
                        if (x[(i*individual_length+k) ^ x[(j*individual_length+k)]]):
                            hamming += 1

                    partial_fitness = partial_fitness + 1.0 / \
                        (hamming*hamming) + 1.0/((individual_length -
                                                  hamming) * (individual_length-hamming))

        fitness = 1.0/(2*partial_fitness)

        return round(fitness, 4)
