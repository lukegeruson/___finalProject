import matplotlib.pyplot as plt
#this  graph will attempt to graph automatically
plt.title("autoplot", fontsize=24)

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)

plt.axis([0, 1100, 0, 1100000])

#set titles

plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show