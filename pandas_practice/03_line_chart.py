import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#ADQ2 1:남성, 2:여성
#Y값: 접근, 역량, 활용 (0, 100)
#X값 : 남성의 접근, 역량, 활용 평균값, 여성의 접근, 역량, 활용의 평균값(무응답 제외)


df=pd.DataFrame({'x': range(1,11), 'y': np.random.randn(10)})

plt.plot(['accessibility','competency','utilize'], [?,?,?]) #남성
plt.plot(['accessibility','competency','utilize'], [?,?,?]) #여성
plt.xlabel('digital_ability')
plt.ylabel('sex')
plt.title('male vs female')
plt.legend(['male', 'female'])
plt.show()

#컬러
plt.plot( 'x', 'y', data=df, color='skyblue')

#선 스타일
plt.plot( [1,1.1,1,1.1,1], linestyle='-' , linewidth=4)
plt.text(1.5, 1.3, "linestyle = '-' ", horizontalalignment='left', size='medium', color='C0', weight='semibold')
plt.axis('off')
plt.show()


