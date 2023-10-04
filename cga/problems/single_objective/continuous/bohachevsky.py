from numpy import cos
from numpy import pi
from numpy import power as pw

from problems.abstract_problem import AbstractProblem

# -15 ≤ xi ≤ 15    i = 1,…,n
# global minumum at f(0,...,0) = 0


class Bohachevsky(AbstractProblem):

    def f(self, x: list) -> float:
        return round(sum([(pw(x[i], 2) + (2*pw(x[i+1], 2)) - (0.3*cos(3*pi*x[i])) - (0.4*cos(4*pi*x[i+1])) + 0.7) for i in range(len(x)-1)]), 3)
