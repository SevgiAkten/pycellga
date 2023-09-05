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

Note:The problem is to evolve a solution the vector of x consisting in 6 real parameters (the vector of x =< a1, w1, a2, w2, a3, w3 >) each one encoded with 8 bits in the range [-6.4, 6.35]. 
"""

# Length of chromosomes = 192
# Maximum Fitness Value = 0.01
# Maximum Fitness Value Error = 10^-2


class Fms(AbstractProblem):
    def f(self, x: list) -> float:

        theta = (2.0*pi)/100.0
        random.seed(100)

        # initialize parameters
        a1_int = 0
        w1_int = 0
        a2_int = 0
        w2_int = 0
        a3_int = 0
        w3_int = 0

        # calculate parameter a1_int
        for i in range(32):
            if x[i] == 1:
                a1_int += 1
            a1_int <<= 1
        a1_int >>= 1

        # calculate parameter w1_int
        for i in range(32, 64):
            if x[i] == 1:
                w1_int += 1
            w1_int <<= 1
        w1_int >>= 1

        # calculate parameter a2_int
        for i in range(64, 96):
            if x[i] == 1:
                a2_int += 1
            a2_int <<= 1
        a2_int >>= 1

        # calculate parameter w2_int
        for i in range(96, 128):
            if x[i] == 1:
                w2_int += 1
            w2_int <<= 1
        w2_int >>= 1

        # calculate parameter a3_int
        for i in range(128, 160):
            if x[i] == 1:
                a3_int += 1
            a3_int <<= 1
        a3_int >>= 1

        # calculate parameter w3_int
        for i in range(160, 192):
            if x[i] == 1:
                w3_int += 1
            w3_int <<= 1
        w3_int >>= 1

        a1 = -6.4+(12.75*(a1_int/4294967295.0))
        w1 = -6.4+(12.75*(w1_int/4294967295.0))
        a2 = -6.4+(12.75*(a2_int/4294967295.0))
        w2 = -6.4+(12.75*(w2_int/4294967295.0))
        a3 = -6.4+(12.75*(a3_int/4294967295.0))
        w3 = -6.4+(12.75*(w3_int/4294967295.0))

        target = list()
        target = [random.randint(2) for g in range(101)]
        for i in range(101):
            target[i] = 1.0*sin((5.0*theta*i)-(1.5 *
                                sin((4.8*theta*i)+(2.0*sin(4.9*theta*i)))))
        y = list()
        y = [random.randint(2) for g in range(101)]
        for j in range(101):
            y[j] = a1*sin((w1*theta*j) -
                          (a2 * sin((w2*theta*j)+(a3*sin(w3*theta*j)))))

        distance = 0.0
        partialfitnesss = 0.0
        fitness = 0.0
        for k in range(101):
            distance = target[k] - y[k]
            partialfitnesss = partialfitnesss + (distance*distance)
        fitness = partialfitnesss
        return round(fitness, 2)
