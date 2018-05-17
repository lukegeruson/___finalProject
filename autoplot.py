import matplotlib.pyplot as plt
#this  graph will attempt to graph automatically
plt.title("autoplot", fontsize=24)

#get a list of 1000 values. Make the y values x**2 for each x value
x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

#set colormap
#the scatter function also takes away the edges because of the many plotted points, also sets color to red
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

#large axis corresponds with large amount of x values
plt.axis([0, 1100, 0, 1000000])

#set titles

plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

#save the file in finalproject folder

plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()