import pandas as pd
import numpy as np
import random
# Full path use karein (r prefix lagana mat bhooliyega)
# \U ka matlab hota hai Unicode Character (jo ke 8 digits ka code expect karta hai).
# df = pd.read_excel('C:\Users\Tech Mart\Desktop\python\numpy\MOCK_DATA.xlsx') wrong path
# q ky unki \U ke baad 8 digits ka code expect karta hai, isliye error aata hai. tuhum r prefix use karo ya double backslashes use karo, jese ke:

df1 = pd.read_excel('C:/Users/Tech Mart/Desktop/python/numpy/MOCK_DATA.xlsx')     
# right path with forward slashes
df2 = pd.read_excel('C:\\Users\\Tech Mart\\Desktop\\python\\numpy\\MOCK_DATA.xlsx')
# right path with double slashes
df3 = pd.read_excel(r'C:\Users\Tech Mart\Desktop\python\numpy\MOCK_DATA.xlsx')
# right path with r prefix
print(df1.head())
# print(df2.head())
# print(df3.head())
print("--------------------------------")
print('missing values in df1:')
print(df1.isnull().sum())

number = random.randrange(1, 10)

df1['experience'] = df1['experience'].fillna(number)
# Yeh tariqa warning nahi dega

# Agar aap inplace=True hi use karna chahte hain, to pure DataFrame par method chalayein aur dictionary ka use karein:
# df1.fillna({'experience': number}, inplace=True)


# Yeh sabse behtareen tariqa hai
mean_val = df1['performance_rate'].mean()
df1['performance_rate'] = df1['performance_rate'].fillna(mean_val)

df1.replace([np.inf, -np.inf], np.nan, inplace=True)

df1.fillna(df1.mean(), inplace=True)

df1.drop_duplicates(inplace=True)

df1['age'] = np.where(df1['age'] < 0,df1['age'].mean(), df1['age'] )