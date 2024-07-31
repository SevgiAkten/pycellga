from problems.abstract_problem import AbstractProblem
import math

"""
    The Griewank function is a benchmark function commonly used in continuous optimization problems. It features a 
    complex, multi-modal landscape with numerous local minima and a global minimum. The function combines smooth and 
    oscillatory characteristics, making it a challenging test for optimization algorithms. The Griewank function is 
    useful for evaluating an algorithm's ability to navigate through intricate search spaces, balancing exploration of 
    diverse regions with exploitation of promising areas. It helps assess the robustness, efficiency, and convergence 
    properties of optimization techniques in handling functions with both smooth and complex features.
"""
# -600 ≤ xi ≤ 600      i = 1,…,n
# global minumum at f(0,...,0) = 0


class Griewank(AbstractProblem):
    def f(self, X: list) -> float:
        sum = 0
        for x in X:
            sum += x * x
        fitness = 1
        for i in range(len(X)):
            fitness *= math.cos(X[i] / math.sqrt(i + 1))
        return round((1 + sum / 4000 - fitness), 3)
