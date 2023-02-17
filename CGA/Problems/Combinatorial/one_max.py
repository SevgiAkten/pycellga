from problems.abstract_problem import AbstractProblem

class OneMax(AbstractProblem):
    def f(self, x) -> float:
        return sum(x)
