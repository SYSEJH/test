import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 불러오기
df = pd.read_excel('C:/Users/hanjh/Desktop/조형기 분석 데이터/조형기 전류 데이터 기반 작동 여부 코드/3.xlsx')

# y값이 50 이상인 경우에는 1, 아니면 0으로 값을 설정한 새로운 열 추가
df['is_above_50'] = (df.iloc[:, 1] >= 50).astype(int)

# 첫 번째 서브플롯: 원래의 그래프
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(20, 15))
ax1.plot(df.iloc[:, 0], df.iloc[:, 1], color='blue')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Current (A)')

# 두 번째 서브플롯: 점과 선으로 표시
ax2.plot(df.iloc[:, 0], df.iloc[:, 2], marker='o', linestyle='-', color='orange')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Current above 50A')

# 세 번째 서브플롯: y값이 1인 지점으로부터 다음 1이 나타나는 x축 간격이 20이하인 구간에서 모든 y축을 1로 변경
df['is_above_50_new'] = df['is_above_50'].copy()
idx = df['is_above_50'].where(df['is_above_50'] == 1).dropna().index
for i in range(len(idx)-1):
    start = idx[i]
    end = idx[i+1]
    if (df.iloc[end, 0] - df.iloc[start, 0]) <= 30:
        df.loc[start+1:end, 'is_above_50_new'] = 1

ax3.plot(df.iloc[:, 0], df.iloc[:, 3], linestyle='--', color='red')
ax3.fill_between(df.iloc[:, 0], 0, df.iloc[:, 3], where=df.iloc[:, 3] == 1, color='grey')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Operation status')

plt.show()