from problems.abstract_problem import AbstractProblem
from numpy import power as pw

"""
    The Pow function is a benchmark function used in continuous optimization problems. It is characterized by its 
    polynomial landscape, which features a smooth surface with a global minimum. The function typically involves 
    raising variables to a power, creating a landscape that tests the optimization algorithm's ability to handle 
    polynomially increasing complexities. The Pow function is useful for evaluating how well algorithms manage smooth 
    and continuous functions, balance exploration and exploitation, and achieve convergence to the global optimum 
    in polynomial problem domains.
"""
# -5.0 ≤ xi ≤ 15.0
# global minumum at f(5, 7, 9, 3, 2) = 0

class Pow(AbstractProblem):

    def f(self, x: list) -> float:

        fitness = 0.0
        for i in range(len(x)):
            fitness += pw(x[i] - 5, 2) + pw(x[i+1] - 7, 2) + \
                pw(x[i+2] - 9, 2) + pw(x[i+3] - 3, 2) + pw(x[i+4] - 2, 2)

            return round(fitness, 2)
