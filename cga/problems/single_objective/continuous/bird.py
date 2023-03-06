from numpy import sin
from numpy import cos
from numpy import exp
from numpy import pi

from problems.abstract_problem import AbstractProblem

# -2π ≤ x, y ≤ 2π

# two global minima at
# f(4.70104 ,3.15294) = -106.7785949110127
# f(−1.58214 ,−3.13024) = -106.77859490782035


class Bird(AbstractProblem):

    def f(self, x: float, y: float) -> float:
        return sin(x)*(exp(1-cos(y))**2)+cos(y)*(exp(1-sin(x))**2)+(x-y)**2
