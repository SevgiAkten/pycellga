from problems.abstract_problem import AbstractProblem
from numpy import power as pw

"""
    The Zettle function is a benchmark function used in continuous optimization problems, characterized by its complex 
    and multi-modal landscape. It features a global minimum and multiple local minima, creating a challenging environment 
    for optimization algorithms. The function typically combines polynomial terms and interactions between variables, resulting 
    in a surface with various peaks and valleys. The Zettle function is useful for testing an algorithm's ability to navigate 
    intricate problem spaces, balance exploration and exploitation, and converge to the global optimum amidst numerous local 
    optima. It helps evaluate the robustness and efficiency of optimization techniques in handling complex, multi-dimensional 
    domains.
"""
# -5 ≤ xi ≤ 5     i = 1,…,n
# global minumum at f(−0.0299, 0) = −0.003791

class Zettle(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)-1):
            fitness+= pw((pw(x[i],2)+pw(x[i+1],2))-2*x[i],2)+0.25*x[i]
        return round(fitness, 6)