from problems.abstract_problem import AbstractProblem
import numpy as np

"""
    The Sum of Different Powers function is a benchmark function designed for evaluating optimization algorithms in continuous 
    domains. It features a complex and multi-faceted landscape with a global minimum surrounded by multiple local minima. 
    The function is constructed by summing various powers of the input variables, creating a surface with both smooth and 
    oscillatory regions. This complexity presents a challenging test for optimization techniques, requiring effective exploration 
    of diverse areas and precise exploitation of promising regions. The Sum of Different Powers function is particularly useful 
    for assessing an algorithm's performance in navigating through intricate problem spaces and achieving convergence to the 
    optimal solution despite the presence of numerous local optima.
"""
# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,....,0) = 0

class Sumofdifferentpowers(AbstractProblem):
    def f(self, x: list) -> float:
        fitness = 0.0

        for i in range (1, len(x)):
            a = np.abs(x[i-1])
            b = i+1
            fitness +=  np.power(a,b)

        return round(fitness, 3)