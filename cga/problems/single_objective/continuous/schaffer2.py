from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

"""
    The Modified Schaffer Function #2 is a benchmark function used in continuous optimization problems. It is an adaptation 
    of the original Schaffer function, featuring a complex landscape with a global minimum and several local minima. This 
    modified version alters the function's structure to create a challenging surface with varying degrees of smoothness and 
    oscillation. The function is designed to test optimization algorithms' effectiveness in exploring and exploiting intricate 
    search spaces. It evaluates the ability of algorithms to converge to the global optimum despite the presence of numerous 
    local optima. The Modified Schaffer Function #2 provides a rigorous test of the robustness and efficiency of optimization 
    techniques in handling multi-dimensional and complex problem domains.
"""
# -100 ≤ xi ≤ 100     i = 1,…,n
# global minumum at f(0,...,0) = 0

# Modified Schaffer function #2

class Schaffer2(AbstractProblem):
    def f(self, X: list) -> float:
        fitness = 0.0
        for i in range(len(X)-1):
            fitness += (0.5 + ((pw(np.sin(pw(X[i],2)-pw(X[i+1],2)), 2) - 0.5) / pw((1 + 0.001*(pw(X[i],2) + pw(X[i+1],2))), 2)))
        return round(fitness, 3)
