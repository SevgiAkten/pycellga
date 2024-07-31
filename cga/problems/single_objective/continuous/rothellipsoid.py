from problems.abstract_problem import AbstractProblem
import numpy as np

"""
    The Rotated Hyper-Ellipsoid function is a benchmark function used in continuous optimization problems. It is known 
    for its complex landscape, featuring a rotated ellipsoidal shape that introduces challenges for optimization algorithms. 
    The function is characterized by its global minimum at the origin and a surface that gradually increases in complexity 
    as the distance from the minimum grows. The rotation of the hyper-ellipsoid adds difficulty to the optimization process, 
    requiring algorithms to effectively navigate through a distorted search space. The Rotated Hyper-Ellipsoid function tests 
    the ability of optimization algorithms to handle rotated and skewed landscapes, balancing exploration and exploitation 
    strategies while converging to the global optimum.
"""
# -100 ≤ xi ≤ 100     i = 1,…,n
# global minumum at f(0,....,0) = 0

# ROTATED HYPER-ELLIPSOID FUNCTION

class Rothellipsoid(AbstractProblem):
    def f(self, x: list) -> float:
        fitness = 0.0
        d=len(x)+1

        for i in range (1, d):
            fitness +=  (d+1-i)*np.power(x[i-1],2)

        return round(fitness, 3)