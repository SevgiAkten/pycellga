from problems.abstract_problem import AbstractProblem

# -5.12 ≤ xi ≤ 5.12      i = 1,…,n
# global minumum at f(0,...,0) = 0


class Sphere(AbstractProblem):
    def f(self, x: list) -> float:
        return round(sum([i*i for i in x]), 3)
