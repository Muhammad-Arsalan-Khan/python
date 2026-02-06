import numpy as np 

array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],])

# print("2d array",array_2d)
print("Array shape:", array_2d.shape)  # Output: (2, 3)
print("Array dimensions:", array_2d.ndim)  # Output: 2
print("Array data type:", array_2d.dtype)  # Output: int64 (or int32 depending on the system)
print("Array size:", array_2d.size)  # Output: 6
print("Element size in bytes:", array_2d.itemsize)  # Output: 8 (or 4 depending on the system)  
print("Total bytes consumed by the array:", array_2d.nbytes)  # Output: 48 (or 24 depending on the system)

print("--------------------------------")

arr2d = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])
# print("2d array",arr2d)
print("Array shape:", arr2d.shape)  # Output: (3, 5
print("Array dimensions:", arr2d.ndim)  # Output: 2
print("Array data type:", arr2d.dtype)  # Output: int64 (or int32 depending on the system)
print("Array size:", arr2d.size)  # Output: 15      
print("Element size in bytes:", arr2d.itemsize)  # Output: 8 (or 4 depending on the system)
print("Total bytes consumed by the array:", arr2d.nbytes)  # Output: 120 (or 60 depending on the system)    
print("--------------------------------")

arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])

# print("3d array",arr3d)
print("Array shape:", arr3d.shape)  # Output: (3, 2, 2)
print("Array dimensions:", arr3d.ndim)  # Output: 3 
print("Array data type:", arr3d.dtype)  # Output: int64 (or int32 depending on the system)
print("Array size:", arr3d.size)  # Output: 12  
print("Element size in bytes:", arr3d.itemsize)  # Output: 8 (or 4 depending on the system)
print("Total bytes consumed by the array:", arr3d.nbytes)  # Output: 96 (or 48 depending on the system)
print("--------------------------------")

arr4d = np.array([
    [   # Block 0
        [   # Layer 0
            [1, 2],
            [3, 4]
        ],
        [   # Layer 1
            [5, 6],
            [7, 8]
        ]
    ],
    [   # Block 1
        [   # Layer 0
            [9, 10],
            [11, 12]
        ],
        [   # Layer 1
            [13, 14],
            [15, 16]
        ]
    ]
])

# print(arr4d)
print("Array shape:", arr4d.shape)  # Output: (2, 2, 2, 2)
print("Array dimensions:", arr4d.ndim)  # Output: 4     
print("Array data type:", arr4d.dtype)  # Output: int64 (or int32 depending on the system)
print("Array size:", arr4d.size)  # Output: 16
print("Element size in bytes:", arr4d.itemsize)  # Output: 8 (or 4 depending on the system)
print("Total bytes consumed by the array:", arr4d.nbytes)  # Output: 128 (or 64 depending on the system)    
print("--------------------------------")

arr5d = np.arange(32).reshape(2, 2, 2, 2, 2)
# print(arr5d)
print("Array shape:", arr5d.shape)  # Output: (2, 2, 2, 2, 2)
print("Array dimensions:", arr5d.ndim)  # Output: 5     
print("Array data type:", arr5d.dtype)  # Output: int64 (or int32 depending on the system)
print("Array size:", arr5d.size)  # Output: 32
print("Element size in bytes:", arr5d.itemsize)  # Output: 8 (or 4 depending on the system)
print("Total bytes consumed by the array:", arr5d.nbytes)  # Output: 256 (or 128 depending on the system)
print("--------------------------------")


arr6d = np.arange(64).reshape(2, 2, 2, 2, 2, 2)
# print("Array shape:", arr6d)  # Output: (2, 2, 2, 2, 2, 2)

astype_arr = np.array([1, 2, 3, 4, 5])
print("Original array data type:", astype_arr.dtype)  # Output: int64 (or int32 depending on the system)
float_arr = astype_arr.astype(np.float64)
print("Converted array data type:", float_arr.dtype)  # Output: float64

aggregate_arr = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(aggregate_arr))  # Output: 15  
print("Mean:", np.mean(aggregate_arr))  # Output: 3.0
print("Standard Deviation:", np.std(aggregate_arr))  # Output: 1.4142135623730951
print("Variance:", np.var(aggregate_arr))  # Output: 2.0
print("Minimum:", np.min(aggregate_arr))  # Output: 1
print("Maximum:", np.max(aggregate_arr))  # Output: 5
print("--------------------------------")

print("add", aggregate_arr + 10)  # Output: [11 12 13 14 15]
print("subtract", aggregate_arr - 2)  # Output: [-1 0 1 2 3]
print("multiply", aggregate_arr * 3)  # Output: [ 3 6 9 12 15]
print("divide", aggregate_arr / 2)  # Output: [0.5 1.  1.5 2.  2.5]
print("power", aggregate_arr ** 2)  # Output: [ 1 4 9 16 25]        
print("modulus", aggregate_arr % 2)  # Output: [1 0 1 0 1]
print("--------------------------------")