'''
Write a Pandas program to count the NaN values in one or more columns in DataFrame.
'''

import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("Original DataFrame")
print(df)
print("\nNumber of NaN values in one or more columns:")
print(df.isnull().values.sum())

'''nan_count = 0
for null in df.columns:
    if null == np.nan:
        nan_count = nan_count+1

print("\nNumber of NaN values in one or more columns:")
print(nan_count)'''
