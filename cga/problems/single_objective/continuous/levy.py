from problems.abstract_problem import AbstractProblem
import math
from numpy import power as pw

"""
    The Levy function is a benchmark function used in continuous optimization problems known for its challenging 
    landscape. It features multiple local minima and a global minimum, with a complex structure that includes both 
    smooth and highly oscillatory regions. The Levy function is useful for testing optimization algorithms' ability to 
    handle diverse search spaces, requiring effective exploration and exploitation strategies. Its design evaluates the 
    robustness and convergence behavior of optimization techniques in navigating complex, multi-modal landscapes and 
    finding optimal solutions.
"""
# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(1,1) = 0

class Levy(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)-1):
            fitness+= pw((math.sin(3*x[i]*math.pi)),2) + (pw((x[i] - 1),2))*(1 + pw((math.sin(3*x[i+1]*math.pi)),2)) + (pw((x[i+1] - 1),2))*(1 + pw((math.sin(2*x[i+1]*math.pi)),2))
        return round(fitness, 3)