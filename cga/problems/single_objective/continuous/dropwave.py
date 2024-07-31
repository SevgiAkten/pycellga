from problems.abstract_problem import AbstractProblem
from numpy import *

"""
    The Dropwave function is a benchmark function used in continuous optimization problems. It is known for its 
    distinctive landscape, featuring a large central drop or "wave" with a global minimum at the center, surrounded 
    by a flat region and a few local minima. The function presents a challenging test for optimization algorithms 
    due to its steep drop-off and the difficulty of navigating from the flat region to the steep descent. The Dropwave 
    function is useful for evaluating the performance of optimization techniques in handling complex, multi-modal 
    landscapes, balancing exploration and exploitation, and achieving convergence to the global optimum. Its unique 
    shape helps assess the robustness and efficiency of various optimization strategies.
"""
# -5.12 ≤ xi ≤ 5.12    i = 1,2
# global minumum at f(0,0) = −1


class Dropwave(AbstractProblem):
    def f(self, x: list) -> float:
        
        x1 = x[0]
        x2 = x[1]

        sqrts_sums = power(x1,2)+power(x2,2)
        b = 0.5*(sqrts_sums)+2
        fitness = -(1 + cos(12*sqrt(sqrts_sums)))/b

        return round(fitness, 3)