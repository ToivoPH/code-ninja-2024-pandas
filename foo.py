#task 0
import pandas as pd

print('hello')

df = pd.read_csv("cereal.csv")
#print(df.head)

#task 1 paper 1
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

#task 1 paper 2
"""
#to get the rating of the cerial AND the manufacturer
df[(df.rating >= 50) & (df.mfr == 'K')]
df.loc[(df['mfr']=='K') & (df['fiber']<2)]
#make a query to get the levels of ingredients
df.query('sodium >= 100 & sugars > 10')
"""

#task 2
"""
#output the kelloggs in ascending values
print(df[df['mfr'] == 'K'].sort_values(by='rating'))
"""

#task 3
"""
#Rank the Cereals made by General Mills (G) and Nabisco (N), according to the number of
#calories (highest first) and then, by the amount of fat (lowest first).
print(df[df['mfr'] == 'G'].sort_values(by='calories', ascending=True))
print(df[df['mfr'] == 'N'].sort_values(by='fat', ascending=False))
"""

#task 4
"""
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

result = pd.concat([df1, df2], axis=0)  
#concatenate along rows (axis=0)
print(result)

#output multiple columns
print (kelloggs.sort_values(by=['fiber', 'sodium'], ascending=[False, True]))
"""

#task 5
#print the calories in order then those calories ratings in order
"""
from pathlib import Path

print('hello')
filepath = Path('/workspaces/code-ninja-2024-pandas')
for i in filepath.glob('cereal'):
    print(i)
print(df.sort_values(by=['calories', 'rating'], ascending=[False, False]))
"""


#there are 12 tasks so far