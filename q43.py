'''
to replace a specific row with another
'''

import pandas as pd

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace row with index 2 (Charlie) with new data
new_data = {'Name': 'Eva', 'Age': 32, 'City': 'San Francisco'}
df.loc[2] = new_data

print("\nDataFrame after replacing row with index 2:")
print(df)
