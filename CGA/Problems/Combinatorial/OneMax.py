from Problems.abstractproblem import AbstractProblem

class OneMax(AbstractProblem):
    def f(self, x) -> float:
        return sum(x)
