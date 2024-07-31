from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

"""
    The Modified Schaffer Function #1 is a benchmark function used in continuous optimization problems. It is a variation 
    of the original Schaffer function, designed to have a complex, multi-modal landscape with a global minimum and numerous 
    local minima. This modified version introduces changes to the function's structure, resulting in a surface with varying 
    degrees of smoothness and oscillation. The function is used to test optimization algorithms' performance in navigating 
    through intricate search spaces, balancing exploration and exploitation strategies, and achieving convergence to the global 
    optimum. The Modified Schaffer Function #1 assesses the robustness and efficiency of optimization techniques in handling 
    challenging, multi-dimensional problem domains.
"""
# -100 ≤ xi ≤ 100     i = 1,…,n
# global minumum at f(0,...,0) = 0

# Modified Schaffer function #1

class Schaffer(AbstractProblem):
    def f(self, X: list) -> float:
        fitness = 0.0
        for i in range(len(X)-1):
            fitness += (0.5 + ((pw(np.sin(pw(X[i],2)+pw(X[i+1],2)), 2) - 0.5) / pw((1 + 0.001*(pw(X[i],2) + pw(X[i+1],2))), 2)))
        return round(fitness, 3)
