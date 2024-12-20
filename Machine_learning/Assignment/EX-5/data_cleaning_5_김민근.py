# 문제 5: 데이터 스케일링
# 데이터 스케일링은 데이터의 범위를 조정하는 작업을 의미합니다.
# 데이터 스케일링을 통해 데이터의 분포를 조정하고, 모델의 성능을 향상시킬 수 있습니다.
# 대표적인 데이터 스케일링 방법으로는 StandardScaler, MinMaxScaler, RobustScaler 등이 있습니다.
# 이번 문제에서는 StandardScaler를 사용하여 데이터를 표준화하는 방법을 실습합니다.

# Kaggle의 "Wine Quality" 데이터셋을 사용하여 데이터를 스케일링하세요.
# fixed acidity, volatile acidity, citric acid, residual sugar, chlorides 열의 값을 StandardScaler로 표준화하세요.
# 표준화된 결과를 출력하세요.

# 데이터셋 다운로드
# Kaggle Wine Quality 데이터셋 링크: https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009
# Kaggle Wine Quality 데이터셋 링크로 이동 -> Data 탭 -> winequality-red.csv 다운로드 -> winequality-red.csv 파일을 작업 디렉터리에 저장

# 데이터셋을 불러온 후, 데이터 스케일링을 수행하는 코드를 작성하세요.

import pandas as pd
from sklearn.preprocessing import StandardScaler

# 데이터 읽기기
df = pd.read_csv('winequality-red.csv')

# 스케일링 할 카테고리 선정
categories = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides']

# 스케일러 인스턴스 생성성
standardscaler = StandardScaler()

# 카테고리 별 스케일링 수행
for category in categories:
    df[category] = standardscaler.fit_transform(df[[category]])

print(df)