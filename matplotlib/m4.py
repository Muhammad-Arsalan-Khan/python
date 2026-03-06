import matplotlib.pyplot as plt
# histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4,4]
# plt.hist(data, bins=num_of_bin, color='blue') 
plt.hist(data, bins=4, color='blue', edgecolor='black') 
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
