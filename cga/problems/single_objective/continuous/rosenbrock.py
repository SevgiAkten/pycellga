from problems.abstract_problem import AbstractProblem
from numpy import power as pw

# -5 ≤ xi ≤ 10      i = 1,…,n
# global minumum at f(1,...,1) = 0


class Rosenbrock(AbstractProblem):
    def f(self, x: list) -> float:
        return round(sum([(100 * (pw((x[i+1] - pw(x[i], 2)), 2))) + pw((1 - x[i]), 2) for i in range(len(x) - 1)]), 3)
