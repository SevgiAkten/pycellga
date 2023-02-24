from optimizer import *
import matplotlib.pyplot as plt

result_tuple = optimize()

# result_tuple[0] = optimizer_result, type is dict
# result_tuple[1] = parameters, type is dict
# result_tuple[2] = best_objectives, type is list
# result_tuple[3] = avg_objectives, type is list

# exucute optimize function print optimizer_result dict keys and values
print("-------------#### Solution Output ####-------------")
[print(i, result_tuple[0][i]) for i in result_tuple[0]]

print("-------------##### Parameters #####-------------")
[print(i, result_tuple[1][i]) for i in result_tuple[1]]

# plot result
plt.plot(result_tuple[2])  # best_objectives
plt.plot(result_tuple[3])  # avg_objectives
plt.title("Objectives", fontsize=20, fontweight="bold"),
plt.xlabel("Generations", fontsize=16, fontweight="bold"),
plt.ylabel("Cost", fontsize=16, fontweight="bold"),
plt.show()
