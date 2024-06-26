'''
Write a Pandas program to select a row of series/dataframe by given integer index.

Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
Index-2: Details
col1 col2 col3
2 3 6 9
'''

import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
result = df.iloc[2:3, : ]
print("Index-2: Details")
print(result)
