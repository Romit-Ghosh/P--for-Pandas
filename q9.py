 #  Write a Pandas program to convert a given Series to an array.

import pandas as pd
import numpy as np
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Series to an array: ")
a = s1.values
print(a)
print(type(a))
