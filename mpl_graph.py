#tutorial from crash course by
#by eric mathes
#a simple graph!

#rename to plt for convenience
import matplotlib.pyplot as plt

#title
plt.title("memegraph", fontsize=30)
#this is the list that is plotted
#I changed names of variables and values
x_values = [100, 200, 300, 400, 500]
y_values = [25, 22, 16, 16, 14]
#this plots and shows graph

plt.scatter(x_values, y_values, linewidth=5)
# Set chart titles
plt.ylabel("frequency of prime numbers", fontsize=20)
plt.xlabel("occuring in the range of", fontsize=20)

# change tick size
plt.tick_params(axis='both', labelsize=10)

plt.show()
