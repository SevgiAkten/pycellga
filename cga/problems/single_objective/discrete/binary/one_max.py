from problems.abstract_problem import AbstractProblem

"""
    The OneMax function is a benchmark function used in optimization problems, particularly in evolutionary algorithms. 
    It is characterized by its simple, single-objective landscape, where the goal is to maximize the number of ones in a 
    binary string. The function features a straightforward and linear surface with a global maximum corresponding to the 
    string of all ones. The OneMax function serves as a basic test for optimization algorithms, assessing their ability to 
    perform efficiently on simple, unimodal problems. It evaluates the algorithm's performance in finding the optimal solution 
    with minimal complexity, making it a valuable test case for basic evolutionary strategies and search techniques.
"""
class OneMax(AbstractProblem):
    def f(self, x) -> float:
        return sum(x)
