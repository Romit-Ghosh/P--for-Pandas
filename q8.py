# Write a Pandas program to convert the first column of a DataFrame as a Series.

import pandas as pd

d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)

print("Original DataFrame")
print(df)

# Using iloc
s1 = df.iloc[:, 0]

# Alternatively, you can directly reference the column by name
#s1 = df['col1']

print("\n1st column as a Series:")
print(s1)
print(type(s1))
