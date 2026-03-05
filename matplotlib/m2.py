import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

# Create horizontal bar chart
plt.bar(categories, values, color='blue', edgecolor='red', linewidth=2, alpha=0.7, hatch='/*', label='Data Values', zorder=3, width=0.5)
# plt.barh(categories, values) # horizontal bar chart
plt.legend(loc='upper right', fontsize='large', title='Legend', title_fontsize='x-large', shadow=True, fancybox=True, borderpad=1, frameon=True, facecolor='lightgray', edgecolor='black', framealpha=0.8, ncol=1, markerscale=1.5, handlelength=2, handletextpad=0.5, columnspacing=1, labelspacing=0.5)
# Labels and title
plt.xlabel("Values")
plt.ylabel("Categories")
plt.title("Horizontal Bar Chart Example")

plt.show()