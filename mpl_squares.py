#I successfully installed pip!!
#looks like I wil be using python 2.7 cause thats what the crash course uses
#seems like it isn't as simple as syntax, because python 3.6 appears to not be able to import matplotlib

#a simple graph!

#rename to plt for convenience
import matplotlib.pyplot as plt

#title
plt.title("memegraph", fontsize=30)
#this is the list that is plotted
x_values = [100, 200, 300, 400, 500]
y_values = [25, 22, 16, 16, 14]
#this plots and shows graph

plt.plot(x_values, y_values, linewidth=5)
# Set chart title and label axes. vplt.title("Square Numbers", fontsize=24) wplt.xlabel("Value", fontsize=14)
plt.ylabel("frequency of prime numbers", fontsize=20)
plt.xlabel("occuring in the range of", fontsize=20)
   # Set size of tick labels.
   #can change both with x or y
plt.tick_params(axis='both', labelsize=10)

plt.show()
