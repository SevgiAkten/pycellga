from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

# -100 ≤ xi ≤ 100     i = 1,…,n
# global minumum at f(0,...,0) = 0

# Modified Schaffer function #1

class Schaffer(AbstractProblem):
    def f(self, X: list) -> float:
        fitness = 0.0
        for i in range(len(X)-1):
            fitness += (0.5 + ((pw(np.sin(pw(X[i],2)+pw(X[i+1],2)), 2) - 0.5) / pw((1 + 0.001*(pw(X[i],2) + pw(X[i+1],2))), 2)))
        return round(fitness, 3)
