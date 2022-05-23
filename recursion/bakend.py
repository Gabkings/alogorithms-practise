import numpy as np 
import pandas as pd 
import requests 
from pprint import pprint

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
data1 =r.json()['data']



df = pd.DataFrame(np.array([data1]),columns=['key', 'age'])
print(df.shape)

# cols = pd.MultiIndex.from_product([columns])

# # df = pd.DataFrame(values,index,columns)
# df = pd.DataFrame(data1, columns=cols)

# df = pd.DataFrame(list(data1),columns=['Key','Age'])

output_dict = [x for x in df if x['age'] >= 50]

print(len(output_dict))
