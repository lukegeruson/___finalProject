import matplotlib.pyplot as plt
#this  graph scatters the plots instead of
plt.title("scattermemes", fontsize=24)

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values, y_values, s=50)
plt.show()

#set titles

plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', which=major, labelsize=14)

plt.show