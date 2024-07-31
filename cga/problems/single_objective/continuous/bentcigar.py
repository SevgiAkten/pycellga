from problems.abstract_problem import AbstractProblem
import numpy as np
from numpy import power as pw

"""
    The Bent Cigar function is a benchmark function used in continuous optimization problems. It is known 
    for its distinctive landscape, characterized by a long, narrow, and deep cigar-shaped valley with a 
    global minimum located at one end of the valley. The function is used to assess optimization algorithms' 
    performance, particularly their ability to handle problems with elongated and narrow optima. The Bent 
    Cigar function is designed to test how well algorithms can navigate through a large, flat region with a 
    steep gradient leading to a narrow optimum. It is useful for evaluating the efficiency of search strategies 
    and convergence properties in continuous optimization tasks.
    """
# -100 ≤ xi ≤ 100     i = 1,…,n
# global minumum at f(0,...,0) = 0

class Bentcigar(AbstractProblem):
    def f(self, X: list) -> float:
        a=0.0
        b=0.0
        sum=0.0
        fitness = 0.0
        
        a = pw(X[0],2)
        b=pw(10,6)
        for i in range(2, len(X)):
            sum += pw(X[i], 2)
        
        fitness = a + (b * sum)
        return round(fitness, 3)
