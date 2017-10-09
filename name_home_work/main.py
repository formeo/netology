import pandas as pd
#
import numpy as np
#
# import matplotlib.pyplot as plt

DATA_PATH = 'names/'
# print(pd.read_csv(DATA_PATH + 'yob1880.txt').head(10))



names_by_year = {}
for year in range(1900, 2000):
    names_by_year[year] = pd.read_csv(
        DATA_PATH + 'yob{}.txt'.format(year),
        names=['Name','Gender','Count']
    )
names_all = pd.concat(names_by_year,names=['Year', 'Pos'],ignore_index=True)
print(names_all)