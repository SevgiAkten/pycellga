from numpy import cos
from numpy import pi
from numpy import power as pw
from problems.abstract_problem import AbstractProblem

"""
    The Bohachevsky function is a benchmark function commonly used to evaluate optimization algorithms 
    in continuous problem domains. It is characterized by a smooth landscape with a global minimum 
    and a few local minima. The function is defined with two variables and is known for its ability 
    to test optimization algorithms' performance in terms of handling both convex and non-convex regions. 
    The Bohachevsky function is useful for assessing how well an algorithm can navigate through complex 
    landscapes, balancing exploration and exploitation to find the global optimum efficiently. It helps 
    evaluate the robustness and accuracy of optimization techniques in continuous domains.
"""
# -15 ≤ xi ≤ 15    i = 1,…,n
# global minumum at f(0,...,0) = 0

class Bohachevsky(AbstractProblem):

    def f(self, x: list) -> float:
        return round(sum([(pw(x[i], 2) + (2*pw(x[i+1], 2)) - (0.3*cos(3*pi*x[i])) - (0.4*cos(4*pi*x[i+1])) + 0.7) for i in range(len(x)-1)]), 3)
