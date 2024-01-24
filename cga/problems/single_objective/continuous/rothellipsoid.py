from problems.abstract_problem import AbstractProblem
import numpy as np

# -100 ≤ xi ≤ 100     i = 1,…,n
# global minumum at f(0,....,0) = 0

# ROTATED HYPER-ELLIPSOID FUNCTION

class Rothellipsoid(AbstractProblem):
    def f(self, x: list) -> float:
        fitness = 0.0
        d=len(x)+1

        for i in range (1, d):
            fitness +=  (d+1-i)*np.power(x[i-1],2)

        return round(fitness, 3)