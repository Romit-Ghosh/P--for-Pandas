'''
Write a Pandas program to rename columns of a given DataFrame.

Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 9
New DataFrame after renaming columns:
Column1 Column2 Column3
0 1 4 7
1 2 5 8
2 3 6 9
'''


import pandas as pd

# Sample data
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

# Create DataFrame
df = pd.DataFrame(data=d)

print("Original DataFrame:")
print(df)

# Rename columns using the rename method
df = df.rename(columns={'col1': 'column1', 'col2': 'column2', 'col3': 'column3'})

print("\nNew DataFrame after renaming columns:")
print(df)
