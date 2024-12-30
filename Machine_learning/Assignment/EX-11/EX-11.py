import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# 데이터 로드
data = pd.read_csv('creditcard.csv')

# 데이터 스케일링링
std_scaler = StandardScaler()

features = data.drop('Class', axis=1)

features_scaled = std_scaler.fit_transform(features)
transaction_df = pd.DataFrame(features_scaled)

# isolation forest 모델 생성
model = IsolationForest(n_estimators=500, contamination=0.05, max_samples='auto',
                        max_features=0.8, random_state=42)

# 모델 학습
transaction_df['Fraud_score'] = model.fit_predict(features_scaled)

# 이상치 결과 해석 후 분류 표시
transaction_df['Fraud_predicted'] = transaction_df['Fraud_score'].apply(lambda x: 0 if x == 1 else 1)

# 보고서 출력
print(classification_report(data['Class'], transaction_df['Fraud_predicted']))