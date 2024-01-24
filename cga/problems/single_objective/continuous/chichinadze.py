from problems.abstract_problem import AbstractProblem
import numpy as np


# -30 ≤ x, y ≤ 30      i = 1,…,n
# global minumum at f(5.90133, 0.5) = −43.3159


class Chichinadze(AbstractProblem):

    def f(self, X: list) -> float:
        x = X[0]
        y = X[1]
        fitness = (np.power(x,2) - 12 * x + 11 + (10 * np.cos((np.pi * x )/ 2))
                + (8 * np.sin(5 * np.pi * x)) - (1.0 / np.sqrt(5) * np.exp(-(np.power((y - 0.5), 2))/2)))
        
        return round(fitness, 4)
    