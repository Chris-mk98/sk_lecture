## 1. 클래스
### 1.1 정의
>**클래스**
Class 란 사용자가 객체를 생성하기 위해 정의한 일종의 템플릿으로서, 원할한 관리와 사용을 위해 데이터와 함수를 묶은 것을 이른다.
**객체**
객체는 데이터와 그 데이터를 조작하기 위한 함수를 함꼐 포함하고 있는 변수다.

```
class ThisIsClass:
	def __this_is_method__(self, ...):
    	statement1
        statement2
        ...
    
```

>- **메서드**는 클래스에서 정의된 함수를 의미한다.
- 메서드 정의시, 관습적으로 `self`를 첫 번째 매개변수로 설정하며, 해당 메서드를 호출하는 객체 자신을 자동으로 매개변수로 전달한다.

### 1.2 생성자
생성자(Constructor)는 객체가 생성될 때 자동으로 호출되는 메서드다. 메서드 명은 `__init__`이다. 객체의 초기 값을 설정할 때에는 생성자를 구현하는 것이 가장 안전한 방법이며, 객체 생성시 생성자의 매개면수에 해당하는 값을 전달해야한다.
```
class ThisIsClass:
	def __init__(self, param1, param2)
    	self.param1 = param1
        self.param2 = param2
```

### 1.3 상속과 오버라이딩
#### 1.3.1 상속
상속(Inheritance)는 클래스 선언시, 다른 클래스의 기능을 물려받을 수 있게 만드는 것을 의미한다.
```
class Child(Parent):
	pass
```
#### 1.3.2 오버라이딩
부모 클래스에 있는 메서드를 다시 동일한 이름으로 정의하면, 정의가 이뤄진 자식클래스에서 다른 기능으로 사용할 수 있다.


## 2. 모듈/패키지
### 2.1 모듈
모듈은 함수나 변수 또는 클래스를 모아놓은 파일. 혹은 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든 파이썬 파일이라고도 한다.

### 2.2 모듈 불러오기
`import`는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해 주는 명령어다.
```
import modul1
from modul2 import function_in_module
```
`,`를 통해 여러 함수를 불러오거나, `*`로 전부를 불러올 수 있다.

> `if __name__ == "__main__"`은 `__name__` 변수가 `__main__`을 값으로 가지고 있음을 검사한다. 파이썬 파일이 실행 될 때, 해당 파일이 최상위 모듈인 경우에 `__name__`에는 `__main__`이 저장된다.


## 3. 라이브러리
### 3.1 datetime.date
- `time.time()`
- `time.localtime()`
- `time.asctime()`
- `time.ctime()`
- `time.strftime()`
- `time.sleep()`

### 3.2 random
- `random.random()`
- `random.sample()`
- `random.choice()`
- `random.randint()`

### 3.3 os
- `os.environ[]`
- `os.chdir()`
- `os.getcwd()`
- `os.system()`
- `os.popen()`
- `os.mdkir()/rmdir()`
- `os.remove()`
- `os.rename()`

### 3.4 json
- `json.dump(data, <file>)` : 딕셔너리 자료형을 JSON 형태로 생성, 파이썬 자료형을 JSON 문자열로 생성할 때 사용
- `json.loads(json_data)` : JSON 문자열을 딕셔너리로 변환
- 리스트, 튜플같은 다른 자료형도 JSON 문자열로 변경 가능하다.
> JSON 문자열을 보기좋게 정렬하는 법
```
print(json.dumps(d, indent = ..., ensure_ascii=False))

```

## 4. 넘파이(Numpy)
### 4.1 Overview
>- 넘파이는 수치 계산에 특화된 라이브러리다.
- 다차원 배열 객체인 ndarray를 중심으로 작동한다. 고성능 다차원 배열 객체를 제공하고 요소의 데이터 타입을 통일시킨다.
- 다양한 함수를 지원하여 다양한 수학적 기능을 제공한다.(배열 연산, 선형 대수, 푸리에 변환, 난수 생성 등)

### 4.2 주요 기능과 문법
- 배열 생성
- 배열 연산
- 배열 변형
- 브로드캐스팅

### 4.3 기본문법
#### 4.3.1. `np.array`: 파이썬 리스트를 배열로 변환한다.
```
arr1 = np.array([1, 2, 3, 4])
arr2 = np,array([[1, 2]], [3, 4]])
```
#### 4.3.2. 배열의 속성을 확인하는 메서드
   - `np.shape` : 배열의 크기(행, 열)을 튜플로 반환
   - `np.ndim` : 해당 배열의 차원 반환
   - `np.size` : 해당 배열의 크기, 총 원소 개수를 반환
   - `np.dtype` : 배열 원소의 데이터 타입

#### 4.3.3. 배열의 인덱싱과 슬라이싱 
```
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0]) # 1행
print(arr[0,1]) # 1행 2열

print(arr[:1, ::2]) # 첫 두 행에서 2열씩 건너뛰기
```
#### 4.3.4. 배열의 연산
   - 배열의 연산은 요소별로 수행한다.
   - 크기가 다른 배열간의 연산을 브로드캐스팅이라고 한다.(스칼라 연산)

#### 4.3.5. 배열의 형태 변경
   - reshape(n, m) : n행 m열 형태로 배열 형태 변경
   - flatten(): 다차원 배열을 1차원 배열로 변환
   
#### 4.3.6. 통계 함수

#### 4.3.7. 난수 생성
   - `np.random.rand(3)` : 0과 1 사이의 랜덤 값
   - `np.random.rnaint(1, 10, size(2, 3))` : 정수 난수 생성

### 4.4 인공지능에서의 활용
>- 배열 생성
- 벡터화 연산
- 활성화 함수
- 난수 생성
- 행렬 연산
- 손실 함수 계산
- 배열 변환


## 5. 판다스(Pandas)
### 5.1 Overview
판다스는 데이터 분석과 조작에 특화된 라이브러리로서
> - 구조화된 데이터를 처리하는데 유용
- 다양한 데이터 소스 지원
- 편리한 데이터 조작

### 5.2 기본 문법
#### 5.2.1 데이터 구조(Series, DataFrame)
- Series: 1차원 데이터 구조, value와 index로 구성된다.
```
s = pd.Series([10, 20, 30], index['A', 'B', 'C']])

print(s)
print(s['A'])
print(s.index)
print(s.values)
```

- DataFrame: 2차원 데이터 구조
```
data = {
	'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35]
    'Score' : [90, 85, 95]
}
df = pd.DataFrame(data)
print(df)
```

#### 5.2.2 데이터 확인
- `head()` : 상위 5개 행 출력
- `tail(n)` : 하위 n개 행 출력
- `shape` : 행/열 개수 
- `info()` : 데이터 타입 및 결측 값 확인
- `describe()` : 수치형 데이터 요약 및 통계

#### 5.2.3 행/열 선택
```
df['Name', 'Score'] # Name, Score 열 


df.loc[0]  # 첫 번째 행
df.loc[:, 'Name'] # 모든 행에서 `Name` 열 
df.iloc[1] # 두 번째 행
df.iloc[:, 1] # 모든 행에서 두 번쨰 열

df[df['Score'] > = 90] # 특정 조건 충족하는 행
```

#### 5.2.4 데이터 조작
```
df['Passed'] = df['Score'] >= 90 # 열 추가

## 새로운 행 추가
new_row {'Name': 'David`,
		 ...,
         'Passed' : False
}
df = df.append(new_row, ignore_index=True)

# 특정 값 수정
df.loc[0, 'Score'] = 95

# 열 전체 수정
df['Passed'] = df['Score'] >= 90
```

#### 5.2.5 결측 값 처리
결측값은 `None`을 집어넣음으로써 생성할 수 있다.
- `df.isnull()` : True는 결측 값을 의미
- `df['Score'] = df['Score'].fillna(0)` : 결측값 채우기
- `df = df.dropna()` : 결측값 제거

#### 5.2.6 데이터 정렬
- `df.sort_values(by='Score')` : 오름차순 정렬
- `df.sort_values(by='Score', ascending=False)` :내림차순 정렬

#### 5.2.7 데이터 그룹화
- `df.groupby('<group>')[<Column>].mean` : 그룹별 특정 열 평균 계산

#### 5.2.8 데이터 입출력
- `pd.DataFrame(<data>)` : csv등 다양한 파일을 읽어올 수 있다.
- `df.to_csv('output.csv', index=False)` : 가공한 데이터를 파일로 저장

### 5.3 판다스와 인공지능
#### 5.3.1 핵심 개념
> - 데이터 구조: Series와 DataFrame
- 데이터 조작 기능 : 데이터 필터링, 그룹화, 결합, 결측 값 처리, 정렬 등
- 데이터 입출력: CSV, SQL, JSON 등 다양한 파일 형식 지원

#### 5.3.2 활용
>- 데이터 탐색
- 데이터 전처리
- 특징 엔지니어링
- 훈련 데이터 준비

