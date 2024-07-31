from problems.abstract_problem import AbstractProblem
from numpy import power as pw

"""
    The Styblinski-Tang function is a benchmark function used in continuous optimization problems, characterized by its 
    complex, multi-modal landscape with multiple local minima and a global minimum. The function is known for its challenging 
    surface, which includes a series of narrow, deep valleys and peaks, making it a rigorous test for optimization algorithms. 
    The Styblinski-Tang function is defined to evaluate an algorithm's ability to navigate through complex search spaces, balance 
    exploration and exploitation, and converge to the global optimum despite numerous local optima. Its intricate landscape 
    helps assess the robustness and efficiency of optimization techniques in handling multi-dimensional, non-convex problem domains.
"""
# -5 ≤ xi ≤ 5     i = 1,…,n
# global minumum at f(−2.903534, −2.903534) = −78.332

class StyblinskiTang(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)):
            fitness+= (pw(x[i],4)-16*(pw(x[i],2)))+5*x[i]
        
        fitness=fitness/len(x)
        return round(fitness, 3)