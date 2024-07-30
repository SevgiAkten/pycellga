from numpy import cos
from numpy import pi

from problems.abstract_problem import AbstractProblem

# -5.12 ≤ xi ≤ 5.12     i = 1,…,n
# global minumum at f(0,...,0) = 0


class Rastrigin(AbstractProblem):

    def f(self, x: list) -> float:
        A = 10.0
        return round((A*len(x)) + sum([((i*i) - (A * cos(2 * pi * i))) for i in x]), 3)
