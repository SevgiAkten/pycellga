from problems.abstract_problem import AbstractProblem
from numpy import power as pw

"""
    The Zakharov function is a benchmark function used in continuous optimization problems, known for its smooth and 
    multi-modal landscape. It features a global minimum at the origin, with a landscape that includes a series of 
    increasingly complex, quadratic-like ridges and valleys. The function combines quadratic and linear terms to create 
    a surface that grows increasingly steep as the distance from the origin increases. The Zakharov function is used to 
    evaluate an optimization algorithm's performance in handling smooth and continuous problem spaces with subtle variations. 
    It assesses the ability of algorithms to efficiently explore and exploit the search space, and converge to the global 
    optimum despite the function's gradual complexity.
"""
# -5 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,..,0) = 0

class Zakharov (AbstractProblem):
    def f(self, x: list) -> float:
        fitness1=0.0
        fitness2=0.0
        fitness3=0.0
        fitness=0.0
        
        for i in range (len(x)-1):
            fitness1 += pw(x[i],2)

        for i in range (len(x)-1):
            fitness2 +=0.5*i*x[i]
        fitness2 = pw(fitness2,2)

        for i in range (len(x)-1):
            fitness3 +=0.5*i*x[i]
        fitness3 = pw(fitness2,4)

        fitness = fitness1 + fitness2 + fitness3

        return round(fitness, 6)