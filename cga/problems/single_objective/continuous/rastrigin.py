from numpy import cos
from numpy import pi
from problems.abstract_problem import AbstractProblem

"""
    The Rastrigin function is a widely used benchmark function in continuous optimization problems. It is known 
    for its challenging landscape, characterized by a large number of local minima surrounding a global minimum. 
    The function features a periodic, oscillatory surface with a global minimum located at the origin. The Rastrigin 
    function is defined to test optimization algorithms' ability to handle complex, multi-modal landscapes and assess 
    their performance in navigating through numerous local optima. It helps evaluate an algorithm's robustness, 
    convergence behavior, and efficiency in solving optimization problems with highly variable and rugged landscapes.
    """
# -5.12 ≤ xi ≤ 5.12     i = 1,…,n
# global minumum at f(0,...,0) = 0

class Rastrigin(AbstractProblem):

    def f(self, x: list) -> float:
        A = 10.0
        return round((A*len(x)) + sum([((i*i) - (A * cos(2 * pi * i))) for i in x]), 3)
