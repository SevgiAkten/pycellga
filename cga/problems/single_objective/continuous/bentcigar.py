from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

# -100 ≤ xi ≤ 100     i = 1,…,n
# global minumum at f(0,...,0) = 0


class Bentcigar(AbstractProblem):
    def f(self, X: list) -> float:
        a=0.0
        b=0.0
        sum=0.0
        fitness = 0.0
        
        a = pw(X[0],2)
        b=pw(10,6)
        for i in range(2, len(X)):
            sum += pw(X[i], 2)
        
        fitness = a + (b * sum)
        return round(fitness, 3)
