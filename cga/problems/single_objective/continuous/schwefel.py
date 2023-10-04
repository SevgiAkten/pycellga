from numpy import sin
from numpy import sqrt

from problems.abstract_problem import AbstractProblem

# -500 ≤ xi ≤ 500     i = 1,…,n
# global minumum at f(420.9687,…,420.9687)) = 0


class Schwefel(AbstractProblem):

    def f(self, x: list) -> float:

        fitness = 0.0
        d = len(x)
        for i in range(d):
            fitness += x[i] * sin(sqrt(abs(x[i])))
        fitness = (418.9829 * d) - fitness

        return round(fitness, 3)
