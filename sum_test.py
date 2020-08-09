import pandas as pd

df = pd.read_csv('test.csv')

print(df['math'])
df['total'] = df.apply(lambda x: x['math'] + x['english'], axis=1)
print(df)