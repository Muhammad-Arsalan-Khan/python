import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original array:", arr)
print(np.insert(arr, 5, 99))  # Insert 99 at index 5
print(np.delete(arr, 5))       # Delete element at index 5
print(np.unique([1, 2, 2, 3, 4, 4, 5]))  # Unique elements
print("--------------------------------")

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array:\n", arr_2d)
print("Insert a new row at index 1:\n", np.insert(arr_2d, 1, [10, 11, 12], axis=0))  # Insert a new row
print("Insert a new column at index 2:\n", np.insert(arr_2d, 2, [13, 14, 15], axis=1))  # Insert a new column
print(np.insert(arr_2d, 1, [10, 11, 12], axis=None))  # Insert a new row
print("--------------------------------")

#append
arr2 = np.array([11, 12, 13])
print("Original array:", arr)   
print("Appended array:", np.append(arr, arr2))  # Append arr2 to arr
print("--------------------------------")

# concatenate
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])   
print("Array 1:\n", arr1)   
print("Array 2:\n", arr2)
print("Concatenated along axis 0:\n", np.concatenate((arr1, arr2), axis=0))  # Along rows
print("Concatenated along axis None:\n", np.concatenate((arr1, arr), axis=None))

# delete
arr_2d = np.array([[1,2,3],[4,5,6]])
print("Original 2D array:\n", arr_2d)
print("Delete row at index 0:\n", np.delete(arr_2d, 0, axis=0))  # Delete first row
print("Delete column at index 1:\n", np.delete(arr_2d, 1, axis=1))  # Delete second column
print("--------------------------------")

# broadcasting vs vectorization
a = np.array([1, 2, 3]) 
b = np.array([10, 20, 30])
print("Broadcasting addition:", a + b)  # Element-wise addition
print("Vectorized addition:", np.add(a, b))  # Using np.add for vectorized addition
print("Broadcasting multiplication:", a * b)  # Element-wise multiplication 
print("Vectorized multiplication:", np.multiply(a, b))  # Using np.multiply for vectorized multiplication
print("--------------------------------")