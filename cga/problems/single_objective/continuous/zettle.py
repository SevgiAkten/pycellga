from problems.abstract_problem import AbstractProblem
import math
from numpy import power as pw

# -5 ≤ xi ≤ 5     i = 1,…,n
# global minumum at f(−0.0299, 0) = −0.003791


class Zettle(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)-1):
            fitness+= pw((pw(x[i],2)+pw(x[i+1],2))-2*x[i],2)+0.25*x[i]
        return round(fitness, 6)