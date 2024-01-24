from problems.abstract_problem import AbstractProblem
import numpy as np
import math as m

# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,....,0) = 0


class Sumofdifferentpowers(AbstractProblem):
    def f(self, x: list) -> float:
        fitness = 0.0

        for i in range (1, len(x)):
            a = np.abs(x[i-1])
            b = i+1
            fitness +=  np.power(a,b)

        return round(fitness, 3)