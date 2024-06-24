'''
Write a Pandas program to add one row in an existing DataFrame.

Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
After add one row:
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
5 10 11 12
'''

import pandas as pd

# Existing DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# New row data
new_row = {'Name': 'David', 'Age': 40}

# Adding new row using .append()
df = df._append(new_row, ignore_index=True)

print("\nDataFrame after adding new row:")
print(df)

