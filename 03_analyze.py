import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('max_columns', None)

df = pd.read_csv('result.csv')

df = df[['ADQ1', 'ADQ2', 'competency', 'accessibility', 'utiliz']]

gr_by_gender = df.groupby(by='ADQ2')

print(gr_by_gender.describe())
