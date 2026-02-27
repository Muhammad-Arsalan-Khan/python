# reshaping & flattening & manipulating  & transposing & swapping axes  & stacking & splitting & copying & viewing & broadcasting & memory layout & advanced indexing 

import numpy as np

# reshaping(row, column) if dimensions match
 
a = np.array([[1, 2, 3, 4, 5, 6]])
b = a.reshape(2, 3)
print("Reshaped array:\n", b)
# is return a view or copy so if effect on original array it's dosn't cretate new array 
print("--------------------------------")


# & flattening & flatten() & ravel()
# flatten() -> returns a copy of the array collapsed into one dimension
# ravel()  -> returns a flattened array as a view if possible

# flatten() aur ravel() dono NumPy array ko 1D (single dimension) mein convert karte hain
c = np.array([[1, 2, 3], [4, 5, 6]])
flat_c = c.flatten()    
ravel_c = c.ravel() 
print("Flattened array using flatten():", flat_c) # copy banata hain
print("Flattened array using ravel():", ravel_c)  # original array
print("--------------------------------")

#manipulating
a = np.array([1,2,3])
print(a + 10 )       # [11 12 13]
print(a * 2 )        # [2 4 6]
print("--------------------------------")

# math main matric transpose bolty hain 
# transposing 

# Ye NumPy array ka attribute hai
# Simple aur fast tareeqa
# Sirf 2D array (matrix) ke liye mostly use hota hai
# Readability achi hoti hai (math style)
d = np.array([[1, 2, 3], [4, 5, 6]])
d_transposed = d.T
print("Transposed array:\n", d_transposed)  

# Ye NumPy ka function hai
# Zyada flexible hai
# Multi-dimensional arrays (3D, 4D) ke liye bhi kaam karta hai
# Tum axes bhi specify kar sakte ho
e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
e_transposed = np.transpose(e)  
print("Transposed array using np.transpose():\n", e_transposed)
print(e.ndim)  # Output: 3

#  swapping axes
print(np.transpose(e, (2, 1, 0)))
#Axes reverse ho jati hain

print(np.transpose(e, (1, 0, 2)))  # is main 0 or 1 swap ho jata hain, 2 same rehta hain
# Iska matlab:
# New axis 0 ← old axis 1
# New axis 1 ← old axis 0
# New axis 2 ← old axis 2
# 👉 Sirf axis 0 aur 1 swap, axis 2 same
print("--------------------------------")

# stack abhi b sai se clear ni howa concept 
# stacking   array ko jorna 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("normal stack",np.stack((a,b)))
print("horizontal stack",np.hstack((a,b)))
print("vertical stack",np.vstack((a,b)))
print("depth stack",np.dstack((a,b)))
print("axis 0",np.stack((a, b), axis=0))
print("axis 1",np.stack((a, b), axis=1))
print("concatenate",np.concatenate((a, b)))


a2 = np.array([[1,2],[3,4]])
b2 = np.array([[5,6],[7,8]])
print("horizontal stack 2d",np.hstack((a2, b2)))

print("concatenate a2 b2 2d",np.concatenate((a2, b2)))
print("concatenate a2 b2 with axis 0 2d",np.concatenate((a2, b2), axis=0))  # vertical
print("concatenate a2 b2 with axis 1 2d",np.concatenate((a2, b2), axis=1))  # horizontal
#real life example rgb = np.dstack((red, green, blue)) or (height, width, 3)
print("--------------------------------")

#splitting array ko todna
a = np.array([1, 2, 3, 4, 5, 6])
print("array split into 3 parts",np.array_split(a, 3))  # array ko 3 parts main split karna, agar equal parts main ni banta to last part chota hoga
print("array split into 2 parts",np.array_split(a, 2))  # array ko 2 parts main split karna, agar equal parts main ni banta to last part chota hoga
print("array split into 4 parts",np.array_split(a, 4))  # array ko 4 parts main split karna, agar equal parts main ni banta to last part chota hoga

A = np.array([[1,2,3,4],[5,6,7,8]])
print("2d array split into 2 horizontal parts",np.hsplit(A, 2))  # along rows
print("2d array split into 2 vertical parts",np.vsplit(A, 2))  # along columns
print("--------------------------------")

# copying & viewing
a = np.array([1, 2, 3]) 
b = a                    # b is a reference to the same array as a (no new array created)
c = a.copy()             # c is a new array that is a copy of a
print("Original array a:", a)
print("Reference copy b (same as a):", b)   
print("Deep copy c (new array):", c)
b[0] = 10  # This will change both a and b since they reference
print("After modifying b:")
print("Array a (affected):", a)
print("Array b (affected):", b)
print("Array c (unaffected):", c)  # c remains unchanged
b = np.append(b, 4)  # This will change b but not a because append creates a new array
print("Array a (unaffected):", a)
print("Array b (affected):", b)
print("------------------")

# viewing
a = np.array([1,2,3])
b = a.view()
print("Original array a:", a)
print("View of array a (b):", b)    
b[0] = 10  # This will change both a and b since they share the same data
print("After modifying b:") 
print("Array a (affected):", a)
print("Array b (affected):", b)  # b is affected because it's a view   
# a ----> [1,2,3]
#   ↑
#   b  (same memory)
print("--------------------------------")

# broadcasting
item = np.array([200, 300, 350, 500])
a2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])  
print("Broadcasting addition:", a + b)  # Element-wise addition  
print("Broadcasting multiplication:", a * b)  # Element-wise multiplication
print("10% discount ",item - (item / 10) )
print("match dimension", a + b) # a and b have the same shape, so they can be added directly
print("broadcasting with different shapes", a + 10)  # a is added to the scalar 10, which is broadcasted to match the shape of a
### print("broadcasting with different shapes", a + np.array([10, 20]))  # This will raise an error because the shapes are not compatible for broadcasting  
print("Broadcasting with different shapes:", a + a2d)
print("--------------------------------")


A = np.array([[1,2,3],
              [4,5,6]])
b = np.array([10,20,30])
print("Broadcasting addition with 2D array:", A + b)  # Broadcasting b across each row of A
print("Broadcasting multiplication with 2D array:", A * b)  # Broadcasting b across each row of A
print("--------------------------------")

# memory layout
arr = np.array([[1, 2, 3], [4, 5, 6]], order='C')  # C-style (row-major)
print("C-style array (row-major):\n", arr)
print("Memory layout (C-style):", arr.flags['C_CONTIGUOUS'])    
arr = np.array([[1, 2, 3], [4, 5, 6]], order='F')  # Fortran-style (column-major)
print("Fortran-style array (column-major):\n", arr)
print("Memory layout (Fortran-style):", arr.flags['F_CONTIGUOUS'])
print("--------------------------------")

# advanced indexing
arrindexing = np.array([[10, 20, 30, 40, 50],
                         [60, 70, 80, 90, 100],
                         [110, 120, 130, 140, 150]])
print("first row, second column",arrindexing[0, 1])  # first row, second column
print("second row, third column",arrindexing[1, 2])   # second row, third column
print("third row, first column", arrindexing[2, 0])   # third row, first column
print("first row",arrindexing[0, :])   # first row  
print("second row",arrindexing[1, :])   # second row
print("second column",arrindexing[:, 1])   # second column  
print("first column",arrindexing[:, 0])   # first column
print("all rows, columns 0 to 2",arrindexing[:, 0:3]) # all rows, columns 0 to 2
print("first two rows, all columns",arrindexing[0:2, :])
print("second row, columns 1 to 3",arrindexing[1, 1:4]) # second row, columns 1 to 3
print("first two rows, columns 1 to 3",arrindexing[0:2, 1:4]) # first two rows, columns 1 to 3
print("every second ele", arrindexing[::2])  # every second element from the array
print("every third ele", arrindexing[::3])  # every third element from the array
print("reversed arr", arrindexing[::-1])  # reversed array  

A = np.array([10,20,30,40])
print("every second ele", A[::2])  # every second element from the array
print("every third ele", A[::3])  # every third element from the array  
print("reversed arr", A[::-1])  # reversed array
print(A[[0,2]])


A = np.array([10,22,35,20,30,40,21])
print("Elements greater than 20:", A[A > 20])
print("Elements between 20 and 30:", A[(A > 20) & (A < 30)])


A = np.array([[1,2,3],
              [4,5,6]])
#A[[r1, r2, r3], [c1, c2, c3]]
print(A[[0,1], [2,1]])
print(A[:, 1:3]) # all rows, columns 1 to 2 (3 is exclusive)
print("--------------------------------")









