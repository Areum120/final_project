import pandas as pd
df = pd.read_csv('senior_answers_sheet.csv')

print(df.shape)
# print(df)

def calculate_accessibility(x):
    q1_sum = sum([ x['Q1A{}'.format(i)] for i in range(1, 2)])
    q2_sum = sum([ x['Q2A{}'.format(i)] for i in range(1, 2 + 1)])
    q3 = x['Q3']
    return

# 문1) Q1A1 1:있다 100 2:없다 0 / Q1A2 1:있다 100 2:없다 0 / Q1A1, Q1A2 1,1: 둘 다 있다 100
# (컴퓨터 or 노트북 2중의 1개만 있음 100점)
# 문2-1) Q2A11 1:스마트폰 50 / 2:피쳐폰 10 / 3: 없다 0
# Q2A2 1:스마트패드 있다 20 / 2: 없다 0
# Q2A3 1:스마트주변기기 있다 20 / 2: 없다 0
# (스마트폰은 50점 피쳐폰은 10점, 스마트패드 20점, 스마트주변기기 20점 스마트폰 비중을 가장 높게 넣고 각 기기별 차등점수 부여)
# 문3) Q3 1:이용할 수 있다 100 / 2:이용할 수 없으면 0

def calculate_competency(x):
    q4_sum = sum([ x['Q4A{}'.format(i)] for i in range(1, 7 + 1)])
    q5_sum = sum([ x['Q5A{}'.format(i)] for i in range(1, 7 + 1)])
    return 50 * q4_sum / 28 + 50 * q5_sum / 28

# 4번 항목&5번 항목만 우선 역량 점수에 넣고 실태보고서 퍼센티지 비교 (4번 총합 50 5번 총합 50 비율로 총 100)
# q4_sum = 7 : 28 = x : 50 (4번 항목이 7개 이므로 1개 항목당 4점 만점으로 7개 28점 만점이라고 보았을 때)
# q5_sum = 7 : 28 = x : 50 (5번도 마찬가지)
# df0.apply(lambda x: calculate_accessibility(x))

#접근, 역량, 활용

df['competency'] = df.apply(lambda x: calculate_competency(x), axis=1)


