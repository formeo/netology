import pandas as pd
#
import numpy as np
#
# import matplotlib.pyplot as plt

DATA_PATH = 'names/'
# print(pd.read_csv(DATA_PATH + 'yob1880.txt').head(10))



def  count_top3(year_list):
    names_by_year = {}
    for year in year_list:
        names_by_year[year] = pd.read_csv(DATA_PATH + 'yob{}.txt'.format(year),names=['Name','Gender','Count'])
    names_all = pd.concat(names_by_year)
    l = names_all.groupby('Name').sum().sort_values(by='Count', ascending=False).head(3)
    return l.axes[0].values

count_top3([1900, 1950, 2000])


def count_dynamics(year_list):
    names_by_year = {}
    for year in year_list:
        names_by_year[year] = pd.read_csv(DATA_PATH + 'yob{}.txt'.format(year), names=['Name', 'Gender', 'Count'])
    names_all = pd.concat(names_by_year, names=['Year', 'Pos'])
    l = names_all.groupby([names_all.index.get_level_values(0), 'Gender']).sum()
    result = {}
    M = []
    F = []
    for enum_values in l.values.tolist()[::2]:
        F.append(enum_values)
    for enum_values in l.values.tolist()[1::2]:
        M.append(enum_values)
    result['M'] = M
    result['F'] = F
    return result

count_dynamics([1900, 1950, 2000])

# {'M': [146391, 1675092, 1262262], 'F': [279409, 1390888, 670434]}





# df = pd.DataFrame({'group':[0,1,1,1,2,2,3,3,3], 'val':np.arange(9)})
# gp = df.groupby('group')
# print(gp)
# gp.groups.keys()


# def count_dynamics():
#     pass
# count_top3([1880]) == ['John', 'William', 'Mary']
# count_top3([1900, 1950, 2000]) == ['James', 'John', 'Robert']
#
#
# count_dynamics([1900, 1950, 2000]) == {
#           'F': [299810, 1713259, 1814922],
#           'M': [150486, 1790871, 1962744]
#         }


# for year in range(1900, 2001, 10):
#     names_by_year[year] = pd.read_csv(
#         '/Users/ashvets/Temp/names/yob{}.txt'.format(year),
#         names=['Name','Gender','Count']
#     )
# names_all = pd.concat(names_by_year, names=['Year', 'Pos'])