from problems.abstract_problem import AbstractProblem
import numpy as np

# -4 ≤ xi ≤ 5     i = 1,…,n
# global minumum at f(0,....,0) = 0


class Powell(AbstractProblem):
    def f(self, x: list) -> float:
        fitness = 0.0
        a = 0.0
        b = 0.0
        c = 0.0
        e = 0.0
        
        d = round(len(x)/4)

        for i in range (1, d):
            a = np.power((x[4*i-3]+10*x[4*i-2]),2)
            b = np.power((x[4*i-1]-x[4*i]),2)
            c = np.power((x[4*i-2]-2*x[4*i-1]),4)
            e = np.power((x[4*i-3]-x[4*i]),4)
            fitness +=  a + 5*b + c + 10*e

        return round(fitness, 3)