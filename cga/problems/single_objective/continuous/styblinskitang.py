from problems.abstract_problem import AbstractProblem
from numpy import power as pw

# -5 ≤ xi ≤ 5     i = 1,…,n
# global minumum at f(−2.903534, −2.903534) = −78.332

class StyblinskiTang(AbstractProblem):
    def f(self, x: list) -> float:
        fitness=0.0
        for i in range (len(x)):
            fitness+= (pw(x[i],4)-16*(pw(x[i],2)))+5*x[i]
        
        fitness=fitness/len(x)
        return round(fitness, 3)