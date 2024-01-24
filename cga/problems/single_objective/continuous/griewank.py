from problems.abstract_problem import AbstractProblem
import math

# -600 ≤ xi ≤ 600      i = 1,…,n
# global minumum at f(0,...,0) = 0


class Griewank(AbstractProblem):
    def f(self, X: list) -> float:
        sum = 0
        for x in X:
            sum += x * x
        fitness = 1
        for i in range(len(X)):
            fitness *= math.cos(X[i] / math.sqrt(i + 1))
        return round((1 + sum / 4000 - fitness), 3)
