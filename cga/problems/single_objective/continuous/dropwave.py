from problems.abstract_problem import AbstractProblem
import math
from numpy import *

# -5.12 ≤ xi ≤ 5.12    i = 1,2
# global minumum at f(0,0) = −1


class Dropwave(AbstractProblem):
    def f(self, x: list) -> float:
        
        x1 = x[0]
        x2 = x[1]

        sqrts_sums = power(x1,2)+power(x2,2)
        b = 0.5*(sqrts_sums)+2
        fitness = -(1 + cos(12*sqrt(sqrts_sums)))/b

        return round(fitness, 3)