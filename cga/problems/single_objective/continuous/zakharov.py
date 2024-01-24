from problems.abstract_problem import AbstractProblem
import math
from numpy import power as pw

# -5 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,..,0) = 0


class Zakharov (AbstractProblem):
    def f(self, x: list) -> float:
        fitness1=0.0
        fitness2=0.0
        fitness3=0.0
        fitness=0.0
        
        for i in range (len(x)-1):
            fitness1 += pw(x[i],2)

        for i in range (len(x)-1):
            fitness2 +=0.5*i*x[i]
        fitness2 = pw(fitness2,2)

        for i in range (len(x)-1):
            fitness3 +=0.5*i*x[i]
        fitness3 = pw(fitness2,4)

        fitness = fitness1 + fitness2 + fitness3

        return round(fitness, 6)