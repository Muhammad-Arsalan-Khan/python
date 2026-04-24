import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    "emp_id": [0, 1, 2],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 42],
    "City": ["New York", "Los Angeles", None],    
    "Occupation": ["Engineer", "Doctor", "Artist"],
    "Salary": [np.inf, 126000.0, 52500.0],      
    "bonus": [7000.0, -np.inf, 5000.0],          
    "Department": ["IT", None, None],
    "yearly_bonus": [3500.0, 6000.0, np.nan]     
}

df = pd.DataFrame(data)
print(df)