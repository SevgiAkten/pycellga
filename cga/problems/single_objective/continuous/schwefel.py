from numpy import sin
from numpy import sqrt

from problems.abstract_problem import AbstractProblem

# -500 ≤ xi ≤ 500     i = 1,…,n
# global minumum at f(420.9687,…,420.9687)) = 0


class Schwefel(AbstractProblem):

    def f(self, x: list) -> float:
        return 418.9829*len(x) - sum([i * sin(sqrt(abs(i))) for i in x])
