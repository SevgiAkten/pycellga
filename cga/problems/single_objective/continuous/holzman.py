from problems.abstract_problem import AbstractProblem
from numpy import power as pw

"""
    The Holzman function is a benchmark function used in continuous optimization problems. It is known for its 
    challenging landscape, which includes multiple local minima and a global minimum. The function is designed to 
    test the performance of optimization algorithms in handling complex, multi-modal search spaces. The Holzman function 
    evaluates an algorithm's ability to balance exploration and exploitation, navigate through diverse regions, and 
    converge to the global optimum. Its intricate structure makes it a valuable test for assessing the robustness and 
    efficiency of various optimization techniques in continuous domains.
"""
# -10 ≤ xi ≤ 10     i = 1,…,n
# global minumum at f(0,...,0) = 0

class Holzman(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)):
            fitness += i * pw(x[i],4)
        return round(fitness, 3)
