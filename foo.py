#task 0
import pandas as pd

print('hello')

df = pd.read_csv("cereal.csv")
#print(df.head)

#task 1
"""
print(df.info())
"""

#task 2
"""
#output first rows
print(df.iloc[1:3])
#output number of rows and columns
print(df.shape)
#output column header names
print(df.columns.values)
#output detailed 
df.describe()
"""

#task 3
"""
#output 3rd row
print(df.iloc[3:4])
#output last row
print(df.iloc[,:-1])
#output the first column
print(df.iloc[:, :1])
#output the first 2 columns of the first 10 rows
print(df.iloc[:10, :2])
"""

#task 3.5
"""
#which cereals are made by Kellogs
print(df["mfr"] == "K")
#find average fiber in cereals
print(df["fiber"].mean())
"""

#task 4
"""
#what are the different serving sizes
print(df["cups"]) 
#how many are on the top 3 shelfs
print(df["shelf"] <= 3)
#what are the average calories
print(df["calories"].mean())
#whats the highest sodium
print(df["sodium"].max())
#whats the lowest fiber
print(df["fiber"].min())
#what cereals have a lower than sixty percent rating
print(df["rating"] < 60)
"""

#task 4 extension
"""
#output the names and the calories
print(df[["name", "calories"]])
#output Froot Loops and Golden Grahams
print(df.iloc[25], df.iloc[31])
#output a small square of data from the middle of the file
print(df.iloc[6:16, 4:7])
#[rows, cols]
"""
