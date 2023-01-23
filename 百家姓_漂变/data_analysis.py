import numpy as np
import pandas as pd
from random import choice
from tool_kit import *

## csv file has something special with the encoding
df = pd.read_csv('./data_rank.csv', encoding= 'GB18030', header = None)
df.columns = ['rank', 'surname', 'percent', 'population', 'province'] # Define column names
df['population'] = df['population'] * 10
df['population'] = df['population'].apply(int)
print(df)

## Basic Info
total_population = sum(df['population'])
pool_sur = []


## Generate population pool
### Add surname into pool
for i in range(len(df)):
    cur = [df['surname'][i]] * int(df['population'][i])
    pool_sur += cur

### Next generation
# generation_1 = next_generation(pool_sur)
# result_begin = df[['surname', 'population']]
# result_1 = pd.value_counts(generation_1)
# result_1 = result_1.to_frame()
# result_1 = result_1.reset_index()
# result_1.columns = ['surname', 'population']
# result_combine = pd.merge(result_begin, result_1,how='outer', on='surname')
# print(result_combine)

### 10 generations
# generation_ten = generation_by_generation(pool_sur, 10, df)
# generation_ten.to_csv('10_generations.csv', encoding='GB18030')


### 20 generations
# generation_twenty = generation_by_generation(pool_sur, 20, df)
# generation_twenty.to_csv('20_generations.csv', encoding='GB18030')

### 50 generations
generation_fifty = generation_by_generation(pool_sur, 50, df)
generation_fifty.to_csv('50_generations.csv', encoding='GB18030')