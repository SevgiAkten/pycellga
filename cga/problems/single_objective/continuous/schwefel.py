from numpy import sin
from numpy import sqrt
from problems.abstract_problem import AbstractProblem

"""
    The Schwefel function is a benchmark function used in continuous optimization problems, known for its challenging 
    landscape with a global minimum and numerous local minima. It features a complex surface that includes both smooth 
    and highly oscillatory regions, making it a demanding test for optimization algorithms. The Schwefel function is 
    characterized by its global minimum at the origin and a landscape that grows increasingly steep away from the minimum. 
    It evaluates the performance of optimization algorithms in handling functions with a rugged and complex search space, 
    testing their ability to balance exploration and exploitation and converge efficiently to the global optimum. The function 
    is useful for assessing the robustness and efficiency of various optimization techniques in navigating intricate problem domains.
"""
# -500 ≤ xi ≤ 500     i = 1,…,n
# global minumum at f(420.9687,…,420.9687)) = 0

class Schwefel(AbstractProblem):

    def f(self, x: list) -> float:

        fitness = 0.0
        d = len(x)
        for i in range(d):
            fitness += x[i] * sin(sqrt(abs(x[i])))
        fitness = (418.9829 * d) - fitness

        return round(fitness, 3)
