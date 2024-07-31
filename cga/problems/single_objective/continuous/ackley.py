from numpy import pi
from numpy import e
from numpy import cos
from numpy import sqrt
from numpy import exp
from problems.abstract_problem import AbstractProblem

"""
    The Ackley function is a commonly used benchmark function for optimization algorithms, especially 
    in continuous problem domains. It is characterized by its complex landscape, including many local 
    minima and a global minimum at the origin. The function is used to test the performance of optimization 
    algorithms due to its challenging, multi-modal nature and its ability to assess the balance between 
    exploration and exploitation strategies. The Ackley function features a large, flat outer region with 
    a steep drop-off to a narrow, deep central hole, making it a valuable test for algorithm robustness 
    and convergence behavior.
"""
# -32.768 ≤ xi ≤ 32.768
# global minumum at f(0, 0) = 0
class Ackley(AbstractProblem):

    def f(self, x: list) -> float:

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
