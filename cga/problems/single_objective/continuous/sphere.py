from problems.abstract_problem import AbstractProblem
from numpy import sum

# -5.12 ≤ xi ≤ 5.12
# global minumum at f(0,...,0) = 0


class Sphere(AbstractProblem):
    def f(self, x: list) -> float:
        return sum([i*i for i in x])
