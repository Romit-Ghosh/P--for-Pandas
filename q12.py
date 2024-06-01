# Write a Pandas program to create a subset of a given series based on value and condition.

import pandas as pd

s = pd.Series([0, 1, 2, 3, 40, 5, 6, 7, 8, 9, 1.6])
print("Original Data Series:")
print(s)

print("\nSubset of the above Data Series:")
n = 6
new_s = s[s < n].reset_index(drop=True)  # Reset index after filtering
print(new_s)
