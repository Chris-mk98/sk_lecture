import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error


#  0.데이터 로드
data = pd.read_csv('train.csv')

# 1. 결측치 많거나, 필요없는 컬럼럼 삭제
delete_data = ['Id', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature', 'MasVnrType']

for column in delete_data:
    data = data.drop(column, axis=1)

# 2. LotFrontage 열 평균치로 대체  
data['LotFrontage'] = data['LotFrontage'].fillna(data['LotFrontage'].mean())

print(len(data.columns))

# 3. 범주형 데이터 원-핫 인코딩
# 3.1범주형 데이터
category_data = ['MSZoning', 'MSSubClass', 'Street', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType','HouseStyle',
'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating',
'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual', 'Functional', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive', 'SaleType', 'SaleCondition']

# 3.2 인코딩 수행
dummies_data_multi = pd.get_dummies(data, columns=category_data, dummy_na=True)


# 4. feature, target 분리
# 4.1 수치형 데이터 분리
numerical_data = [
    'LotFrontage', 'LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
    'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
    'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
    'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageYrBlt', 'GarageCars',
    'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch',
    'PoolArea', 'MiscVal', 'MoSold', 'YrSold'
]
numerical_columns = dummies_data_multi[numerical_data]
columns_after_74 = dummies_data_multi.iloc[:, 74:]

# 4.2 feature, target 분리 / 훈련 및 시험 데이터 분리
x = pd.concat([numerical_columns, columns_after_74], axis=1)
y = data.loc[:,'SalePrice']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 5. 모델 생성
model = DecisionTreeRegressor()


# 6. 모델 학습 수행행
model.fit(x_train, y_train)

# 7. 테스트 데이터에 대한 예측 수행
y_pred = model.predict(x_test)

# 8. MAE 측정정
mae = mean_absolute_error(y_test, y_pred) 
print(mae)
print(len(numerical_data),len(category_data))