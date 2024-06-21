'''
Write a Pandas program to iterate over rows in a DataFrame.

Sample Python dictionary data and list labels:
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
'''

import pandas as pd
import numpy as np
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
label = ['a', 'b', 'c']
df = pd.DataFrame(exam_data, index= label)
for index, row in df.iterrows():
    print(row['name'], row['score'])
