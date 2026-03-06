import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

plt.pie(values, labels=categories, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'orange'], explode=(0.1, 0.2, 0, 0), shadow=True)
# startangle=140, explode=(0.1, 0, 0, 0), shadow=True
plt.title("Pie Chart Example")
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()