from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,...,0) = 0


class Matyas(AbstractProblem):
    def f(self, X: list) -> float:
        fitness = 0.0
        for i in range(len(X)-1):
            fitness += 0.26*(pw(X[i], 2)+pw(X[i+1], 2)) - 0.48*X[i]*X[i+1]
        return round(fitness, 3)
