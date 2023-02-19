from problems.abstract_problem import AbstractProblem

class Ackley(AbstractProblem):
    def f(self, x) -> float:
        raise NotImplementedError()
