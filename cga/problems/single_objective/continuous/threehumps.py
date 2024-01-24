from problems.abstract_problem import AbstractProblem
import math
from numpy import power as pw

# -5 ≤ xi ≤ 5     i = 1,…,n
# global minumum at f(0,..,0) = 0


class Threehumps (AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)-1):
            fitness+= 2*pw(x[i],2) - 1.05*pw(x[i],4)+(pw(x[i],6)/6) + (x[i]*x[i+1])+ pw(x[i+1],2)
        return round(fitness, 6)