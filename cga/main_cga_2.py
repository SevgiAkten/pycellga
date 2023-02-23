from optimizer import *
import matplotlib.pyplot as plt

res = optimize()

# res[0] = optimizer_result, type is dict
# res[1] = best_objectives, type is list
# res[2] = avg_objectives, type is list

# exucute optimize function print optimizer_result dict keys and values
[print(i, res[0][i]) for i in res[0]]

# plot result
plt.plot(res[1])  # best_objectives
plt.plot(res[2])  # avg_objectives
plt.title("Objectives", fontsize=20, fontweight="bold"),
plt.xlabel("Generations", fontsize=16, fontweight="bold"),
plt.ylabel("Cost", fontsize=16, fontweight="bold"),
plt.show()
