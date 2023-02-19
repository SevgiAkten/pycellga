from problems.abstract_problem import AbstractProblem

class TSP(AbstractProblem):
    def f(self, x) -> float:
        raise NotImplementedError()
