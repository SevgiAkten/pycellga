from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,...,0) = 0
"""
    The Matyas function is a benchmark function used in continuous optimization problems, known for its simple 
    yet effective testing of optimization algorithms. It features a smooth, quadratic landscape with a single global 
    minimum. The function is designed to test an algorithm's ability to handle smooth, convex problems and converge 
    efficiently to the optimal solution. Despite its simplicity, the Matyas function is valuable for assessing basic 
    optimization performance and robustness in continuous domains.
"""
class Matyas(AbstractProblem):
    def f(self, X: list) -> float:
        fitness = 0.0
        for i in range(len(X)-1):
            fitness += 0.26*(pw(X[i], 2)+pw(X[i+1], 2)) - 0.48*X[i]*X[i+1]
        return round(fitness, 3)
