from problems.abstract_problem import AbstractProblem
from numpy import power as pw
# -5.0 ≤ xi ≤ 15.0
# global minumum at f(5, 7, 9, 3, 2) = 0


class Pow(AbstractProblem):

    def f(self, x: list) -> float:

        fitness = 0.0
        for i in range(len(x)):
            fitness += pw(x[i] - 5, 2) + pw(x[i+1] - 7, 2) + \
                pw(x[i+2] - 9, 2) + pw(x[i+3] - 3, 2) + pw(x[i+4] - 2, 2)

            return round(fitness, 2)
