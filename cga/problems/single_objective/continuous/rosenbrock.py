from problems.abstract_problem import AbstractProblem
from numpy import power as pw

"""
    The Rosenbrock function, also known as the Rosenbrock's valley or Rosenbrock's banana function, is a popular benchmark 
    function used in continuous optimization problems. It is characterized by a narrow, curved valley containing the 
    global minimum, with the function value increasing sharply away from the valley. The function features a global 
    minimum inside a long, narrow, and parabolic-shaped region. The Rosenbrock function is useful for testing optimization 
    algorithms' ability to converge to the global minimum in the presence of a flat and wide region and a narrow, steep 
    valley. It evaluates the algorithm's efficiency in navigating complex landscapes and finding optimal solutions within 
    challenging search spaces.
"""
# -5 ≤ xi ≤ 10      i = 1,…,n
# global minumum at f(1,...,1) = 0

class Rosenbrock(AbstractProblem):
    def f(self, x: list) -> float:
        return round(sum([(100 * (pw((x[i+1] - pw(x[i], 2)), 2))) + pw((1 - x[i]), 2) for i in range(len(x) - 1)]), 3)
