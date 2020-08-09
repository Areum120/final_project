import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.set_option('display.max_colwidth', None)
# pd.set_option('max_columns', None)

#male&female 접근,역량,활용 분석
df = pd.read_csv('result_senior.csv')
df = df[['ADQ1', 'ADQ2', 'competency', 'accessibility', 'utilize']]

def meke_gender(x):
    if x['ADQ2'] == 1:
        return 'male'
    elif x['ADQ2'] == 2:
        return 'female'
    else:
        return 'no answer'
print(df['ADQ2'])

df['gender'] = df.apply(lambda x: meke_gender(x), axis=1)

#결측치 처리
df = df[df['ADQ2']!= '*']

print(df.shape)

gr_by_gender = df.groupby(by='ADQ2')

#역량 평균은 남자가 높고 상위 75%까지 남자가 높다, but 표준편차는 여자가 적으며 최댓값은 여자가 압도적으로 높다
# print(gr_by_gender['competency'].describe())
#접근은 하위 50%미만 분포도 여성과 남성 차이가 높다
# print(gr_by_gender['accessibility'].describe())
#활용은 최댓값이 값고 75%미만에서는 남성이 평균적으로 높은 편
# print(gr_by_gender['utilize'].describe())

#여성이 남성보다 11.5% 더 많음
#여성이 여건이 낮으며, 3개 항목 전체 평균은 남성이 높으나
#역량 부분에서 최댓값은 여성이 높은편, 상위비율 25% 에서는 접근, 역량, 활용
#남성, 여성 차이가 없고 50%미만(평균의 중앙값) 하위로 갈수록 여성이 남성보다 낮은편

#차트1 남성/여성 항목별 평균 (line chart)

df = np.random.exponential(1, 100)
mean_plot = gr_by_gender['accessibility ','competency','utilize'].mean().plot()

plt.xlabel('digital_ability')
plt.ylabel('sex')
plt.title('male vs female')
plt.legend(['male', 'female'])
plt.show()

#차트2 남성/여성 상위/하위 비교 #cluster analysis #funnel chart #gantt chart bubble chart, stacked chart
#차트3 남성/여성 최댓값 비교 (barm histogram)

