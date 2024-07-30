from problems.abstract_problem import AbstractProblem
from numpy import random

# P-PEAK Problem
"""
References
    1. De Jong, K.A., Potter, M.A. & Spears, W.M. (1997). Using problem generators to explore the e®ects of epistasis. In T. Back, editor, Proceedings of the Seventh ICGA, Morgan Kaufmann, 338-345.
    2. Alba, E., Dorronsoro, B., Giacobini, M., & Tomassini, M. (2004). Decentralized cellular evolutionary algorithms. International Journal of Applied Mathematics and Computer Science, 14(3), 101-117.
"""
# Length of chromosomes = 100
# Maximum Fitness Value = 1.0
# there is a problem, how can apply crossover and mutation operator for this chorosome structure [[]]


class Peak(AbstractProblem):
    def f(self, x: list) -> float:

        random.seed(100)

        problem_length = len(x)
        number_of_peaks = 100
        p_target = list()
        p_target = [[random.randint(2) for g in range(100)]
                    for h in range(100)]

        for m in range(number_of_peaks):
            distance = 0
            for n in range(problem_length):
                if (p_target[m][n] != x[m][n]):
                    distance += 1

        fitness = distance/100.0

        return round(fitness, 3)
