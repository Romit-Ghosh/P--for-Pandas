# Write a Pandas program to add some data to an existing Series.

import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
print("\nData Series after adding some data:")
new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index=True)
print(new_s)
