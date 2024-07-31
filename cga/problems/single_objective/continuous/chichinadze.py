from problems.abstract_problem import AbstractProblem
import numpy as np

"""
    The Chichinadze function is a benchmark function used in continuous optimization to assess the performance 
    of optimization algorithms. It is characterized by its complex landscape, which includes multiple local 
    minima and a global minimum. The function typically involves nonlinear interactions between variables, 
    presenting a challenging test for algorithms in terms of handling diverse regions of the solution space. 
    The Chichinadze function is valuable for evaluating the capability of optimization techniques to balance 
    exploration and exploitation, navigate through intricate landscapes, and converge to the global optimum. 
    Its design makes it suitable for testing the robustness and efficiency of various optimization strategies.
"""
# -30 ≤ x, y ≤ 30      i = 1,…,n
# global minumum at f(5.90133, 0.5) = −43.3159

class Chichinadze(AbstractProblem):

    def f(self, X: list) -> float:
        x = X[0]
        y = X[1]
        fitness = (np.power(x,2) - 12 * x + 11 + (10 * np.cos((np.pi * x )/ 2))
                + (8 * np.sin(5 * np.pi * x)) - (1.0 / np.sqrt(5) * np.exp(-(np.power((y - 0.5), 2))/2)))
        
        return round(fitness, 4)
    