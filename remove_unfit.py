from os import listdir
import pandas as pd

files =  listdir('shirts')

print(files)



df = pd.read_csv('shirts.csv')

print(df.describe())

new_df = df.loc[  df['Id'].isin(files)]

print(new_df.describe())


new_df.to_csv('shirts.csv')
