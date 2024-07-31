from problems.abstract_problem import AbstractProblem

"""
    The CountSat function is a benchmark function used in continuous optimization problems, specifically related to satisfiability 
    problems. It focuses on the task of counting the number of solutions that satisfy a given set of constraints. The function's 
    landscape is designed to represent the complexity of finding feasible solutions to constraint satisfaction problems, with a 
    goal of optimizing the count of valid solutions. The CountSat function challenges optimization algorithms to navigate through 
    diverse solution spaces, effectively balance exploration and exploitation, and identify the optimal count of satisfiable solutions. 
    It is valuable for evaluating the robustness and efficiency of techniques in handling constraint-based optimization problems.
    
    References
    1. Droste, S., Jansen, T., & Wegener, I. (2000). A natural and simple function which is hard for all evolutionary algorithms. In 2000 26th Annual Conference of the IEEE Industrial Electronics Society. IECON 2000. 2000 IEEE International Conference on Industrial Electronics, Control and Instrumentation. 21st Century Technologies (Vol. 4, pp. 2704-2709). IEEE.
    2. Giacobini, M., Preuss, M., & Tomassini, M. (2006). Effects of Scale-Free and Small-World Topologies on Binary Coded Self-adaptive CEA. Lecture Notes in Computer Science, 86-98.
"""
# Length of chromosomes = 20
# Maximum Fitness Value = 6860
# Maximum Fitness Value (normalized)= 1

class CountSat(AbstractProblem):
    def f(self, x: list) -> float:

        variables = len(x)  # --> n is the length of x
        total_ones = 0
        fitness = 0
        fitness_normalized = 0.0
        for i in x:
            if i == 1:
                total_ones += 1

        fitness = total_ones + (variables * (variables - 1) * (variables - 2)) - ((variables - 2)
                                                                                  * total_ones * (total_ones - 1)) + (total_ones * (total_ones - 1) * (total_ones - 2))
        fitness_normalized = fitness/6860
        return round(fitness_normalized, 3)
