from numpy import pi
from numpy import e
from numpy import cos
from numpy import sqrt
from numpy import exp
from problems.abstract_problem import AbstractProblem

# -32.768 ≤ xi ≤ 32.768
# global minumum at f(0, 0) = 0


class Ackley(AbstractProblem):

    def f(self, x: list) -> float:
        # t1 = -20 * (exp(-0.2 * (sqrt(0.5 * (sum([i*i for i in x]))))))
        # t2 = -(exp(0.5 * (sum([cos(2 * pi * i) for i in x]))))
        # result = t1 + t2 + e + 20

        sum1 = 0.0
        sum2 = 0.0
        fitness = 0.0

        for i in range(len(x)):
            gene = x[i]
            sum1 += gene*gene
            sum2 += cos(2*pi*gene)
        fitness += -20.0 * exp(-0.2*sqrt(sum1/len(x))) - \
            exp(sum2/len(x)) + 20.0 + e

        return round(fitness, 3)
