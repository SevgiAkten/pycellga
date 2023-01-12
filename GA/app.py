import numpy as np
import matplotlib as plt
from ypstruct import structure  # modified version of dictionary type of python
import ga

# Sphere Test Function
def sphere(x):
    return sum(x**2)


# Problem Definition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

# GA parameters
params = structure()
params.maxit = 100
params.npop = 20
params.pc = 1
params.gamma = 0.1
params.mu = 0.2
params.sigma = 0.1

# Run GA
out = ga.run(problem, params)

# Results
plt.plot(out.bestcost)
plt.xlim(0, params.maxit)
plt.xlabel("Iterations")
plt.ylabel("Best Cost")
plt.title("Genetic Algorithm (GA)")
plt.grid(True)
plt.show()
