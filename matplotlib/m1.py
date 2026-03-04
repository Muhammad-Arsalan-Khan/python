import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [10,20,90,30,70,60,80,20,90]

# plt.plot(x)
# plt.show()

# plt.plot(horizontal, vertical)
# plt.plot(x,y)
# plt.show()

x2 = ['monday', 'tuesday', 'wesday', 'thusday', 'friday', 'saturday', 'sunday']
y2 = [100,150,120,180,160,200,190]
# plt.plot(x, y, color='colorName', linestyle='--', linewidth=2, marker='o', label='2026 sale')
plt.plot(x2, y2, color='green', linestyle='--', linewidth=2, label='2026 sales data')
plt.title('bakery sales this week')
plt.xlabel('week of the day')
plt.ylabel('sales of per days')
plt.legend(loc='upper left')
plt.grid(color='brown', linestyle=':', linewidth=2)
# plt.xlim(1,3) # is se grap main sirf utna part nazar aye ga 
# plt.ylim(0, 160)
plt.xticks(['monday', 'tuesday', 'wesday','thusday', 'friday', 'saturday', 'sunday'],['Day1','Day2','Day3','Day4','Day5','Day6','Day7'])
plt.show()