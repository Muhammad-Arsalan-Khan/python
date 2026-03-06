import matplotlib.pyplot as plt

section_a_marks = [50, 60, 70, 80, 90]
section_b_marks = [70, 85, 90, 95, 99]
exam_hourse = [2, 3, 4, 5, 6]



plt.scatter( exam_hourse, section_a_marks, color='blue', label='Section A', marker='o')
plt.scatter(exam_hourse, section_b_marks , color='red', label='Section B', marker='^')
plt.title("Scatter Plot Example")
plt.xlabel("Section")
plt.ylabel("Exam Hours")
plt.legend()
plt.show()  