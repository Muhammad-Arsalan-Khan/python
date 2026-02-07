import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array 0 index", arr[0])  
print("Array 3 index", arr[3])
print("every second ele", arr[::2])  # every second element from the array
print("every third ele", arr[::3])  # every third element from the array
print("reversed arr", arr[::-1])  # reversed array
print("--------------------------------")

arrindexing = np.array([
    [1, 2, 3, 5 ,7],
    [4, 5, 52, 9 ,10],
    [7, 8, 9, 5 ,6],
    [71, 90, 9, 50 ,4],
    [74, 59, 9, 49 ,56],
    [75, 85, 9, 45 ,58]
])

print("first row, second column",arrindexing[0, 1])  # first row, second column
print("second row, third column",arrindexing[1, 2])   # second row, third column
print("third row, first column", arrindexing[2, 0])   # third row, first column
print("first row",arrindexing[0, :])   # first row
print("second row",arrindexing[1, :])   # second row
print("second column",arrindexing[:, 1])   # second column
print("first column",arrindexing[:, 0])   # first column
print("all rows, columns 0 to 2",arrindexing[:, 0:3]) # all rows, columns 0 to 2
print("first two rows, all columns",arrindexing[0:2, :]) # first two rows, all columns
print("second row, columns 1 to 3",arrindexing[1, 1:4]) # second row, columns 1 to 3
print("first two rows, columns 1 to 3",arrindexing[0:2, 1:4]) # first two rows, columns 1 to 3
print("every second ele", arrindexing[::2])  # every second element from the array
print("every third ele", arrindexing[::3])  # every third element from the array
print("reversed arr", arrindexing[::-1])  # reversed array

#fancy indexing
indices = [0, 2, 4] # Indices of the rows we want to select 
selected_rows = arrindexing[indices]
print("Selected rows using fancy indexing:\n", selected_rows)

# boolean indexing
bool_idx = (arrindexing > 50) & (arrindexing < 60)
filtered = arrindexing[bool_idx]
print("Elements greater than 50:\n", filtered)

print("arrindexing shape",arrindexing.shape)
print("--------------------------------")

arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
print("arr 3d",arr3d)
print("first block, first row, second column", arr3d[0, 0, 1])  # first block, first row, second column
print("second block, second row, first column", arr3d[1, 1, 0])  # second block, second row, first column
print("third block, first row, first column", arr3d[2, 0, 0])  # third block, first row, first column
print("first block", arr3d[0, :, :])  # first block 
print("second block", arr3d[1, :, :])  # second block
print("first row of all blocks", arr3d[:, 0, :])  # first row of all blocks
print("second column of all blocks", arr3d[:, :, 1])  # second column of all blocks
print("arr 3d shape",arr3d.shape)
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
print("arr 4d",arr4d)
print("first block, first layer, first row, second column", arr4d[0, 0, 0, 1])  # first block, first layer, first row, second column
print("second block, second layer, second row, first column", arr4d[1, 1, 1, 0])  # second block, second layer, second row, first column
print("first block, first layer", arr4d[0, 0, :, :])  # first block, first layer
print("second block, second layer", arr4d[1, 1, :, :])  # second block, second layer
print("first layer of all blocks", arr4d[:, 0, :, :])  # first layer of all blocks
print("second row of all layers and blocks", arr4d[:, :, 1, :])  # second row of all layers and blocks
print("arr 4d shape",arr4d.shape)