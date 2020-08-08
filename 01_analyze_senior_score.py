import pandas as pd
df = pd.read_csv('senior_answers_sheet.csv')

print(df.shape)
# print(df)

#접근
def calculate_accessibility(x):
    q1_sum = 0
    if (x['Q1A1'] == 1) or (x['Q1A2'] == 1) or (x['Q1A1'] == 1 & x['Q1A2'] == 1) :
        q1_sum += 100
    q2_sum = 0
    if x['Q2A11'] == 1:
        q2_sum += 50
    elif x['Q2A11'] == 2:
        q2_sum += 10
    elif x['Q2A12'] == 2:
        q2_sum += 10
    elif x['Q2A11'] == 2 & x['Q2A12'] == 2:
        q2_sum += 20

    # print(q1_sum, q2_sum)
    if (x['Q2A2'] == 1) & (x['Q2A3'] == 1):
        q2_sum += 40
    elif (x['Q2A2'] == 1) or (x['Q2A3'] == 1):
        q2_sum += 20

    # print(q1_sum, q2_sum)
    q3 = 0
    if x['Q3'] == 1:
        q3 += 100

    return q1_sum + q2_sum + q3

# 문1) Q1A1 1:있다 100 2:없다 0 / Q1A2 1:있다 100 2:없다 0 / Q1A1, Q1A2 1,1: 둘 다 있다 100
# (컴퓨터 or 노트북 2중의 1개만 있음 100점)
# 문2-1) Q2A11 1:스마트폰 50 / 2:피쳐폰 10 / 3: 없다 0
# Q2A2 1:스마트패드 있다 20 / 2: 없다 0
# Q2A3 1:스마트주변기기 있다 20 / 2: 없다 0
# (스마트폰은 50점 피쳐폰은 10점, 스마트패드 20점, 스마트주변기기 20점 스마트폰 비중을 가장 높게 넣고 각 기기별 차등점수 부여)
# 문3) Q3 1:이용할 수 있다 100 / 2:이용할 수 없으면 0

#역량
def calculate_competency(x):
    q4_sum = sum([ x['Q4A{}'.format(i)] for i in range(1, 7 + 1)])
    q5_sum = sum([ x['Q5A{}'.format(i)] for i in range(1, 7 + 1)])
    return 50 * q4_sum / 28 + 50 * q5_sum / 28

# 4번 항목&5번 항목만 우선 역량 점수에 넣고 실태보고서 퍼센티지 비교하여 6&7번 항목 계산하면서 오차줄이기 (4번 총합 50 5번 총합 50 비율로 총 100)
# q4_sum = 7 : 28 = x : 50 (4번 항목이 7개 이므로 1개 항목당 4점 만점으로 7개 28점 만점이라고 보았을 때)
# q5_sum = 7 : 28 = x : 50 (5번도 마찬가지)
# df0.apply(lambda x: calculate_accessibility(x))


#활용
#PC : A , Mo : B
def calculate_utiliz(x):
    #q8a~q14b까지 sums로 반복문 돌리기
    sums8 = [0] * 2
    sums9 = [0] * 2
    sums10 = [0] * 2
    sums11 = [0] * 2
    sums12 = [0] * 2
    sums13_14 = [0] * 4

    sums8[0] = sum([ x['Q8A{}'.format(i)] for i in range(1, 4 + 1)])
    sums8[1] = sum([ x['Q8B{}'.format(i)] for i in range(1, 4 + 1)])

    sums9[0] = sum([ x['Q9A{}'.format(i)] for i in range(1, 5 + 1)])
    sums9[1] = sum([ x['Q9B{}'.format(i)] for i in range(1, 5 + 1)])

    sums10[0] = sum([ x['Q10A{}'.format(i)] for i in range(1, 4 + 1)])
    sums10[1] = sum([ x['Q10B{}'.format(i)] for i in range(1, 4 + 1)])

    sums11[0] = sum([ x['Q11A{}'.format(i)] for i in range(1, 2 + 1)])
    sums11[1] = sum([ x['Q11B{}'.format(i)] for i in range(1, 2 + 1)])

    sums12[0] = sum([ x['Q12A{}'.format(i)] for i in range(1, 2 + 1)])
    sums12[1] = sum([ x['Q12B{}'.format(i)] for i in range(1, 2 + 1)])

    sums13_14[0] = sum([ x['Q13A{}'.format(i)] for i in range(1, 4 + 1)])
    sums13_14[1] = sum([ x['Q13B{}'.format(i)] for i in range(1, 4 + 1)])
    sums13_14[2] = sum([ x['Q14A{}'.format(i)] for i in range(1, 4 + 1)])
    sums13_14[3] = sum([ x['Q14B{}'.format(i)] for i in range(1, 4 + 1)])

    # list에 값 A, B가 들어있어서 모두 더하기
    total = sum(sums8) + sum(sums9) + sum(sums10) + sum(sums11) /2 * 0.4
    total2 = sum(sums12) + sum(sums13_14) /2 * 0.2

    # 문제8
    # 총점: 32
    # 문제9
    # 총점: 40
    # (sum8 + sum9) / 2 * 0.4 = 14.4

    # 문제10
    # 총점: 32
    # 문제11
    # 총점: 16
    # 48 / 2 * 0.4 = 9.6

    # 문제12
    # 총점: 16
    # 문제13
    # 총점: 32
    # 문제14
    # 총점: 32
    # 80 / 2 * 0.2 = 8

    # 100점 = > 32

    '''
    c(a + b) = ca + cb
    10 * a / 28 + 10 * b / 28
    10 / 28 * a + 10 / 28 * b
    10 / 28(a + b + c + d)
    '''
    return total


# 유선 및 모바일 인터넷 이용여부(0.4)
# 문제 8A + 8B
# 문제 9A + 9B

# 인터넷 서비스 이용 다양성(0.4)
# 문제 10A + 10B
# 문제 11A + 11B

# 인터넷 심화 활용정도(0.2)
# 문제 12A + 12B
# 문제 13A + 13B
# 문제 14A + 14B

#접근, 역량, 활용
#astype(int)를 해줘야 float 오류 방지
df['Q2A12'] = df['Q2A12'].fillna(0).astype(int)
df.iloc[:, 31:80] = df.iloc[:, 31:81].fillna(0).astype(int)


df['competency'] = df.apply(lambda x: calculate_competency(x), axis=1)
df['accessibility'] = df.apply(lambda x: calculate_accessibility(x), axis=1)
df['utiliz'] = df.apply(lambda x: calculate_utiliz(x), axis=1)
#
print(df['utiliz'])

# df.to_csv('result.csv')
# test
# x = {}
# x['Q1A1'] = 1
# x['Q1A2'] = 1
# x['Q2A11'] = 1
# x['Q2A12'] = 0
# x['Q2A2'] = 1
# x['Q2A3'] = 1
# x['Q3'] = 1
# print(calculate_accessibility(x))
