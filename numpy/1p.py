import numpy as np

tp = np.array([1, 2, 3])
avg = np.mean(tp)
print("Average:", avg)  # numpy mean function

# dirference between list and numpy array\
lst = [1, 2, 3]
arr = np.array([1, 2, 3, 4, 5])
print("list", lst , "array", arr)  # numpy array is more efficient than list for numerical computations

# numpy array supports element-wise operations
arr2 = arr * 2  
print("Element-wise multiplication:", arr2)  # numpy array supports element-wise operations

# numpy array supports 2d-dimensional arrays
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)  # numpy array supports multi-dimensional arrays

arr2d = np.array([
    [1, 2, 3, 5 ,7],
    [4, 5, 6, 9 ,10],
    [7, 8, 9, 5 ,6]
])
print(arr2d)
print("first row, second column",arr2d[0, 1])   # first row, second column
print("second row, third column",arr2d[1, 2])   # second row, third column
print("third row, first column",arr2d[2, 0])   # third row, first column
print("first row",arr2d[0, :])   # first row
print("second row",arr2d[1, :])   # second row
print("second column",arr2d[:, 1])   # second column
print("first column",arr2d[:, 0])   # first column
print("all rows, columns 0 to 2",arr2d[:, 0:3]) # all rows, columns 0 to 2
print("first two rows, all columns",arr2d[0:2, :]) # first two rows, all columns
print("second row, columns 1 to 3",arr2d[1, 1:4]) # second row, columns 1 to 3
print("first two rows, columns 1 to 3",arr2d[0:2, 1:4]) # first two rows, columns 1 to 3


filtered = arr2d[arr2d > 5]
print("2d array grater then 5",filtered)

print("arr 2d shape",arr2d.shape)

arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
# output will be (3, 2, 2) A = 3, B = 2, C = 2
# A = kitni 2D tables (layers)
# B = har table mein kitni rows
# C = har row mein kitne columns


print("arr 3d",arr3d)
print("arr 3d shape",arr3d.shape)




# numpy array supports broadcasting 
arr3 = arr + np.array([15, 17, 19, 21, 23])                                   
print("Broadcasting addition:", arr3) # numpy array supports broadcasting
# 1  + 15 = 16
# 2  + 17 = 19
# 3  + 19 = 22
# 4  + 21 = 25
# 5  + 23 = 28


# numpy provides various mathematical functions
squared = np.sqrt(arr)  
print("Square root:", squared)  # numpy provides various mathematical functions


subsetarr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# numpy supports advanced indexing and slicing
subset = subsetarr[1:9]   
print("Subset:", subset)  # numpy supports advanced indexing and slicing

# numpy supports advanced indexing and slicing
subset2 = subsetarr[1:11:2]   
print("Subset2:", subset2)  # numpy supports advanced indexing and slicing

# numpy supports boolean indexing
booleanarray = np.array([1,10,11,30,50,40,33,7,44,9])
bool_idx2 = booleanarray > 12   
filtered2 = booleanarray[bool_idx2]
print("Filtered (greater than 12):", filtered2)  # numpy supports boolean indexing


# default array value 
defaultarr = np.zeros((3, 4))
print("Default array (zeros):\n", defaultarr)  # numpy provides functions to

defaultarr2 = np.ones((2, 5))
print("Default array (ones):\n", defaultarr2)  # numpy provides functions

defaultarr3 = np.full((4, 3), 7)
print("Default array (full of 7s):\n", defaultarr3)  # numpy provides functions to create arrays filled with a specific value

defaultarr4 = np.eye(5)
print("Default array (identity matrix):\n", defaultarr4)  # numpy provides functions to create identity matrices

n = 3
matrix_off_diagonal_ones = np.ones((n, n)) - np.eye(n)
print("Matrix with ones off the diagonal:\n", matrix_off_diagonal_ones)  # creating a matrix with ones off the diagonal


defaultarr5 = np.arange(0, 20)
print("Default array (arange):\n", defaultarr5)  # numpy provides functions to create arrays with a range of values 
defaultarr5_with_step = np.arange(0, 20, 2)
print("Default array (arange with step):\n", defaultarr5_with_step)  # numpy provides functions to create arrays with a range of values and a step size

defaultarr6 = np.linspace(0, 2, 5)  # (start, end, number of values)
print("Default array (linspace):\n", defaultarr6)  # numpy provides functions to create arrays with a specified number of evenly spaced values between a start and end point
 
defaultarr7 = np.random.rand(3, 4)
print("Default array (random):\n", defaultarr7)  # numpy provides functions to create arrays with random values

defaultarr8 = np.random.randint(0, 10, (3, 4))
print("Default array (random integers):\n", defaultarr8)  # numpy provides

defaultarr9 = np.diag([1, 2, 3, 4])
print("Default array (diagonal):\n", defaultarr9)  # numpy provides functions to create diagonal matrices
#  [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]
