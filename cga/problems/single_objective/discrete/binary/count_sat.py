from problems.abstract_problem import AbstractProblem

# Length of chromosomes = 20
# Maximum Fitness Value = 6860


class CountSat(AbstractProblem):
    def f(self, x: list) -> float:

        variables = len(x)  # --> n is the length of x
        total_ones = 0
        for i in x:
            if i == 1:
                total_ones += 1

        fitness = total_ones + variables * (variables - 1) * (variables - 2) - (
            variables - 2) * total_ones * (total_ones - 1) + total_ones * (total_ones - 1) * (total_ones - 2)

        return fitness
