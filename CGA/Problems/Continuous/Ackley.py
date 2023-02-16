from Problems.abstractproblem import AbstractProblem

class Ackley(AbstractProblem):
    def f(self, x) -> float:
        raise NotImplementedError()
