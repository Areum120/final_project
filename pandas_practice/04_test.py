
import pandas as pd

df = pd.read_csv('groupby_test.csv')
print(df)

gr = df.groupby('gender')
print(gr.describe())

result = gr['age'].age(['sum','mean'])
print(result)