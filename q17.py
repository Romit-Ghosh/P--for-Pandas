

import pandas as pd
import numpy as np
num_series = pd.Series([1,2,2,1,6,6,6,10,10,15,15,11,11,15,15,6,10,6,10,6,1,1,1,1,1,1,1,1])
print("Original Series:")
print(num_series)
print("Frequency of each unique value of the said series.")
result = num_series.value_counts()
print(result)
