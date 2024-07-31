from problems.abstract_problem import AbstractProblem
from numpy import random

"""
    The P-Peak (P-PEAK) Problem is a benchmark function used in optimization, known for its complex and multi-modal landscape. 
    It is designed to test optimization algorithms' ability to handle problems with a specified number of peaks (P), where each 
    peak represents a local optimum. The objective is to navigate through a rugged search space with multiple local optima and 
    identify the global optimum among them. The P-PEAK function evaluates the performance of algorithms in exploring and exploiting 
    diverse areas of the search space, effectively balancing exploration to discover new peaks and exploitation to refine solutions 
    around known peaks. It is valuable for assessing the robustness and efficiency of optimization techniques in handling complex, 
    high-dimensional problem domains with multiple significant features.

    References
    1. De Jong, K.A., Potter, M.A. & Spears, W.M. (1997). Using problem generators to explore the e®ects of epistasis. In T. Back, editor, Proceedings of the Seventh ICGA, Morgan Kaufmann, 338-345.
    2. Alba, E., Dorronsoro, B., Giacobini, M., & Tomassini, M. (2004). Decentralized cellular evolutionary algorithms. International Journal of Applied Mathematics and Computer Science, 14(3), 101-117.
"""
# Length of chromosomes = 100
# Maximum Fitness Value = 1.0

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
