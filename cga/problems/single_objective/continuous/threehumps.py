from problems.abstract_problem import AbstractProblem
from numpy import power as pw

"""
    The Three Humps function is a benchmark function used in continuous optimization problems, known for its distinctive 
    multi-modal landscape. It features three prominent peaks (or "humps") with a global minimum situated between them. 
    The function's surface includes both smooth and steep regions, creating a challenging environment for optimization algorithms. 
    The Three Humps function is useful for testing an algorithm's capability to navigate through complex landscapes, effectively 
    balance exploration and exploitation, and converge to the global optimum amidst several local optima. It helps evaluate 
    the robustness and efficiency of optimization techniques in handling multi-modal problem domains with multiple significant 
    features.
"""
# -5 ≤ xi ≤ 5     i = 1,…,n
# global minumum at f(0,..,0) = 0

class Threehumps (AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)-1):
            fitness+= 2*pw(x[i],2) - 1.05*pw(x[i],4)+(pw(x[i],6)/6) + (x[i]*x[i+1])+ pw(x[i+1],2)
        return round(fitness, 6)