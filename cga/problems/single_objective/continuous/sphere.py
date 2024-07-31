from problems.abstract_problem import AbstractProblem

"""
    The Sphere function is a widely used benchmark function in continuous optimization problems, known for its simple 
    and smooth landscape. It features a convex surface with a single global minimum at the origin. The function is 
    characterized by its quadratic nature, where the value increases with the distance from the minimum. The Sphere function 
    is often used to test basic optimization algorithms' performance due to its straightforward structure. It is useful for 
    evaluating an algorithm's ability to handle smooth, convex problems and achieve efficient convergence to the optimal solution. 
    The function provides a fundamental test for assessing the robustness and efficiency of optimization techniques in continuous 
    problem domains.
"""
# -5.12 ≤ xi ≤ 5.12      i = 1,…,n
# global minumum at f(0,...,0) = 0

class Sphere(AbstractProblem):
    def f(self, x: list) -> float:
        return round(sum([i*i for i in x]), 3)
