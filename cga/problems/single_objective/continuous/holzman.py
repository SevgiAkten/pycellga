from problems.abstract_problem import AbstractProblem
from numpy import power as pw

# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,...,0) = 0


class Holzman(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)):
            fitness += i * pw(x[i],4)
        return round(fitness, 3)
