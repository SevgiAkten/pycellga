from problems.abstract_problem import AbstractProblem
import math
from numpy import power as pw

# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(1,1) = 0


class Levy(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)-1):
            fitness+= pw((math.sin(3*x[i]*math.pi)),2) + (pw((x[i] - 1),2))*(1 + pw((math.sin(3*x[i+1]*math.pi)),2)) + (pw((x[i+1] - 1),2))*(1 + pw((math.sin(2*x[i+1]*math.pi)),2))
        return round(fitness, 3)