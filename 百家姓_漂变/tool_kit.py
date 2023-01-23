from random import choice
import random
import pandas as pd
### Next generation
def next_generation(pool:list):
    num = len(pool)
    male_num = num // 2
    male = random.sample(pool, male_num)
    next_pool = []
    for i in male:
        next_pool.append(i)
        next_pool.append(i)

    return next_pool

### Generation by Generation
def generation_by_generation(pool:list,generation:int, initial_df):
    gen = pool
    result_combine = initial_df[['surname', 'population']]
    for i in range(generation):
        gen = next_generation(gen)

        result_1 = pd.value_counts(gen)
        result_1 = result_1.to_frame()
        result_1 = result_1.reset_index()
        population_name = 'population' + str(i)
        result_1.columns = ['surname', population_name]
        result_combine = pd.merge(result_combine, result_1, how='outer', on='surname')

    return(result_combine)




