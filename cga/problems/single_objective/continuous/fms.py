from problems.abstract_problem import AbstractProblem
from numpy import pi
from numpy import sin
from numpy import random

"""
References
    1. Tsutsui, S., & Fujimoto, Y. (1993). Forking Genetic Algorithm with Blocking and Shrinking Modes (fGA). In ICGA (pp. 206-215).
    2. Tsutsui, S., Ghosh, A., Corne, D., & Fujimoto, Y. (1997). A Real Coded Genetic Algorithm with an Explorer and an Exploiter Populations. In ICGA (pp. 238-245).
    3. Alba, E., Giacobini, M., Tomassini, M., & Romero, S. (2002). Comparing synchronous and asynchronous cellular genetic algorithms. In Parallel Problem Solving from Nature—PPSN VII: 7th International Conference Granada, Spain, September 7–11, 2002 Proceedings 7 (pp. 601-610). Springer Berlin Heidelberg.
    4. Alba, E., Dorronsoro, B., Giacobini, M., & Tomassini, M. (2004). Decentralized cellular evolutionary algorithms. International Journal of Applied Mathematics and Computer Science, 14(3), 101-117.

Note:The problem is to evolve a solution the vector of x consisting in 6 real parameters (the vector of x =< a1, w1, a2, w2, a3, w3 >) each one encoded with  bits in the range [-6.4, 6.35].
"""

# -6.4 ≤ xi ≤ 6.35
# Length of chromosomes = 6

# Maximum Fitness Value = 0.01
# Maximum Fitness Value Error = 10^-2


class Fms(AbstractProblem):
    def f(self, x: list) -> float:

        theta = (2.0*pi)/100.0
        random.seed(100)

        a1 = x[0]
        w1 = x[1]
        a2 = x[2]
        w2 = x[3]
        a3 = x[4]
        w3 = x[5]

        def yzero(t):
            return 1.0*sin((5.0*theta*t)-(1.5 * sin((4.8*theta*t)+(2.0*sin(4.9*theta*t)))))

        distance = 0.0
        partialfitnesss = 0.0
        fitness = 0.0
        for k in range(101):
            distance = (
                a1*sin((w1*theta*k) - (a2 * sin((w2*theta*k)+(a3*sin(w3*theta*k)))))) - yzero(k)
            partialfitnesss = partialfitnesss + (distance*distance)
        fitness = partialfitnesss
        return round(fitness, 3)
