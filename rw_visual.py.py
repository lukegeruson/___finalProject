#reddit /r/ow posts per week
import matplotlib.pyplot as plt
from random_walk import RandomWalk
#####################################################

while True:
    #make a random walk, and plot the points 
    rw = RandomWalk()

    #calls the method in the RandomWalk class
    rw.fill_walk()

   
   #the xvalues and yvalues have been created as a list to continueously increase with random integers until the max plots are reached
   #looks like coloring doesnt work

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=15)
 
 #this will emphasize first and last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

#remove axes
    plt.axes().get_xaxis().set_visible(false)
    plt.axes().get_yaxis().set_visible(false)


 #the amount of blues shows where the plot started and ended
    plt.show()

    keep_running = raw_input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

#loop simply has the user asked to run program again