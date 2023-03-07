from problems.abstract_problem import AbstractProblem

# -5 ≤ xi ≤ 10      i = 1,…,n
# global minumum at f(1,...,1) = 0


class Rosenbrock(AbstractProblem):
    def f(self, x: list) -> float:
        return sum([(100 * ((x[i+1] - (x[i]**2)) ** 2)) + ((1 - x[i]) ** 2) for i in range(len(x) - 1)])
