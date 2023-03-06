from numpy import cos
from numpy import pi

from problems.abstract_problem import AbstractProblem

# -100 ≤ x, y ≤ 100
# global minumum at f(0, 0) = 0


class Bohachevsky(AbstractProblem):

    def f(self, x: float, y: float) -> float:
        return x**2 + 2*(y**2)-0.3*cos(3*pi*x)-0.4*cos(4*pi*y)+0.7
