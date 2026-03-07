import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [10,20,90,30,70,60,80,20,90]

plt.subplot(2, 2, 1) # 2 rows, 2 columns, 1st plot
plt.plot(x, y, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 sales data')
plt.title('Line Plot')

plt.subplot(2, 2, 2) # 2 rows, 2 columns, 2nd plot
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'orange'], explode=(0.1, 0.2, 0, 0), shadow=True)
plt.title("Pie Chart Example")


plt.subplot(2, 2, 3) # 2 rows, 2 columns, 3rd plot
section_a_marks = [50, 60, 70, 80, 90]
section_b_marks = [70, 85, 90, 95, 99]  
exam_hours = [2, 3, 4, 5, 6]
plt.scatter(exam_hours, section_a_marks, color='blue', label='Section A', marker='o')
plt.scatter(exam_hours, section_b_marks , color='red', label='Section B', marker='^')
plt.title("Scatter Plot Example")   
plt.xlabel("Exam Hours")
plt.ylabel("Marks")
plt.legend()


plt.subplot(2, 2, 4) # 2 rows, 2 columns, 4th plot
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4,4]
plt.hist(data, bins=4, color='blue', edgecolor='black') 
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout() # Adjusts the spacing between subplots


# plt.savefig('file name with extension', dpi= number, quality=number, optimize=True/False, bbox_inches='tight') # is se apne graph ko save kar sakte hai
# dpi = dot pr inches = resolution of the saved image, quality is for jpeg images, optimize is for optimizing the file size, bbox_inches='tight' is for removing extra white space around the saved image.

# agar folder nahi hai to error aayega
plt.savefig('pic/my_plots.png', dpi=300, bbox_inches='tight')
plt.show()
# 2:00 to 2:06 wapis dekh leya 