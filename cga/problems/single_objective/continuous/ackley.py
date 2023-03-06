from numpy import pi
from numpy import e
from numpy import cos
from numpy import sqrt
from numpy import exp
from problems.abstract_problem import AbstractProblem

# -32.768 ≤ x, y ≤ 32.768
# global minumum at f(0, 0) = 0


class Ackley(AbstractProblem):

    def f(self, x: float, y: float) -> float:
        return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 *
                                                                        pi * x)+cos(2 * pi * y))) + e + 20
