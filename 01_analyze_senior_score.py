import pandas as pd

df = pd.read_csv('senior_answers_sheet.csv')

print(df.shape)
# print(df)

def calculate_accessibility(x):

    print(x['Q1A1'])

def calculate_competency(x):
    q4_sum = sum([ x['Q4A{}'.format(i)] for i in range(1, 7 + 1)])
    q5_sum = sum([ x['Q5A{}'.format(i)] for i in range(1, 7 + 1)])
    return 50 * q4_sum / 28 + 50 * q5_sum / 28

# df0.apply(lambda x: calculate_accessibility(x))

#접근, 역량, 활용

df['competency'] = df.apply(lambda x: calculate_competency(x), axis=1)


