## 1. 데이터 수집/HTTP 요청
### 1.1 데이터 수집 방법 개요
>- 데이터 수집은 데이터를 효율적으로 모으고 활용하기 위해 중요한 단계
- 데이터 수집의 목적과 환경에 따라 적합한 방법을 선택해야 함.

### 1.2 데이터 수집 방법
>1. 웹 스크래핑: HTML 파싱
2. API 활용: JSON 데이터 가져오기
3. 데이터베이스: 저장된 데이터 가져오기
4. 공개 데이터셋 활용: Kaggle 등에서 다운로드
5. IoT 또는 센서 데이터 수집: 실시간 데이터 수집
6. 소셜 미디어 데이터 수집: 트위터 API 활용

### 1.3 requests 모듈
>설치 명령어
`pip install requests`

#### 1.3.1 주요 메서드

```
import requests

url = 'https://...'
response = requests.get(url)

if response.status_code == 200:
	print("데이터 가져오기 성공")
    print(response.txt[:500])
else:
	print(f"오류 발생: {response.status_code}")
```
#### 1.3.2 응답 데이터 처리
- response.txt : 응답 본문 문자열 반환
- response.json() : JSON 형식 응답 딕셔너리로 반환
- response.status_code : HTTP 상태 코드 반환

#### 1.3.3 쿼리 파라미터 활용
```
...
prarams = {'userId' : 1}
response = requests.get(url, params=params)
```

## 2. 웹 스크래핑 기초
### 2.1 HTML 구조의 이해
#### 2.1.1 HTML 이란?
>- HTML은 웹 페이지의 구조를 정의하는 마크업 언어
- HTML 문서는 브라우저가 읽어서 화면에 표시하는 기본 구조를 제공
- 태그로 요소를 정의하고, 각 요소는 속성과 콘텐츠를 포함한다.

#### 2.1.1 태그(Tags)
>- 태그는 HTML 요소를 정의하며 다음과 같은 형식을 가진다.
<태그이름 속성='값'>내용(contents)</태그이름>
- ex)`<p>Hello, World!</p>`

#### 2.1.2 속성(Attributes)
>- 속성은 태그에 추가 정보를 제공한다.
- 속성은 시작 태그에만 추가한다.(아래는 예시다)
   - id : 요소의 고유 식별자
   - class : CSS 스타일링이나 자바스크립트 제어를 위한 클래스 이름
   - href : 링크를 나타냄(`<a>` 태그에서 사용)
   - src : 이미지나 외부 리소스의 경로(`<src>`에서 사용)

#### 2.1.3 DOM(Document Object Model)
>- DOM은 브라우저가 HTML 문서를 파싱하여 생성한객체 모델
- HTML 문서를 트리 구조로 표현하며, 각 요소는 노드(Node)로 구성
- DOMd의 구성요소
   - HTML 요소(Element Nodes)
   - 속성(Attribute Nodes)
   - 태그(Text Nodes)
   
   
### 2.2 BeautifulSoup
>- Python에서 HTML과 XML 문서를 파싱하고 원하는 데이터를 추출할 때 사용하는 라이브러리
- 설치: `pip install beautifulsoup4`

```
from bs4 import BeautifulSoup
...
# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')

# 태그 탐색
print(soup.title.string)
print(soup.h1.string)
print(soup.a['href'])
```
#### 2.2.1 주요기능: 특정 태그 찾기
>- 태그 이름으로 요소를 쉽게 찾을 수 있음
`soup.p['class']` : `<p>` 태그 찾기

#### 2.2.2 주요기능: 여러 태그 찾기
>`links = soup.find_all('a')` : 특정 태그를 모두 찾아서 반환

#### 2.2.3 주요기능: CSS 선택자 활용
>`select()`를 사용해 CSS 선택자를 기반으로 요소를 찾을 수 있음


## 3. 동적 웹 페이지 데이터 수집
### 3.1 Selenium
#### 3.1.1 Overview: Selenium
>- selenium은 웹 브라우저를 자동으로 제어할 수 있ㄱ데 해주는 라이브러리
- 주로 웹 애플리케이션 테스트에 사용
- 동적 웹 페이지에서 데이터를 수집하는 데이도 활용
- Python을 포함한 여러 프로그래밍 언어에서 사용
- 실제 프라우저를 통해 페이지를 로드하고 JavaScript 실행 결과까지 확인할 수 있음
- 동적 웹 페이지는 JavaScript로 콘텐츠를 생성하므로 일반적인 웹 스크래핑 도구로는 데이터 수집이 어려움

#### 3.1.2 selenium의 기본 구성 요소
>- Web Driver: 브라우저를 제어하는 핵심 도구
- Browser: WebDriver가 제어할 브라우저
- Python 라이브러리

### 3.2 브라우저 자동화 및 요소 조작
#### 3.2.1 브라우저 자동화
```
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com')
driver.quit()
```
#### 3.2.2 요소 조작
>- 웹 페이지에서 특정 요소를 찾아 사용자가 수행할 동작을 자동화하는 것을 의미
- 요소 찾는 법
   - 웹요소 식별 주요 메서드: `find_element`, `find_elements`
   - 주요 Locator: `By.ID`, `By.NAME`, `By.CSS_SELECTOR`, ...

## 4. API 활용 데이터 수집
### 4.1 REST API의 이해
#### 4.1.1 Overview: REST API
>- REST(Reoresentational State Transfer)
웹 서비스와 클라이언트 간의 통신을 설계하는 아키텍처 스타일이다. REST API는 REST 원칙을 따르는 API다. 클라이언트와 서버간 데이터 통신에 사용된다.

>**REST API 설계 원칙**
1. URI는 정보의 리소스를 표현해야한다.
2. 리소스에 대한 행위는 HTTP Method로 표현한다.
3. 슬래시 구분자(/)는 계층 관계를 나타내는데 사용한다.
4. URI 마지막 문자로 슬래시를 포함하지 않는다.
5. 하이픈(-)은 URI 가독성을 높이는데 사용할 수 있다.
6. 언더바(_)는 URI에 사용하지 않는다.
7. URI 경로에는 소문자를 사용한다.
8. 파일 확장자는 URI에 포함시키지 않는다.

#### 4.1.2 URL과 HTTP 메서드
- [URL](https://velog.io/@chris-mk/%EC%9B%B9%ED%95%B4%ED%82%B9-Background-Web-Browser#2-url)
- [HTTP 메서드](https://kmkunk.tistory.com/139)

### 4.2 공공 데이터 포털 또는 오픈 API 활용
```
import requests
import pandas as pd

API_KEY = 'Your_API_Key'
Base =
'http://~'

params = {
	...
}

response = requests.get(BASE_URL, params=params)
data = response.json()

bus_data = pd.DataFrame(data['response']['body']...)
```

## 5. 데이터 저장 및 관리
### 5.1 CSV, Excel, JSON 파일 데이터 저장
#### 5.1.1 CSV
```
import csv

data = ...

# 데이터 저장
with open(...) as file:
	writer = csv.writer(file)
    writer.writerows(data)

# 데이터 읽기
data = pd.read_csv(file)

# open()으로 읽기
with open('file.csv', 'r') as file:
	for line in file:
    	print(line.strip()) # 줄바꿈 제거 후 출력
```

#### 5.1.2 Excel
**openpyxl** 또는 **pandas**를 주로 사용한다.

#### 5.1.3 JSON
>- 키-값 쌍으로 데이터를 저장
- API와 데이터 교환에서 주로 사용
- 계층적 구조를 표현할 수 있어 XML 대안으로 자주 사용
- Python에서 JSON 파일 저장: `json.dump()` `indent=4`로 가독성 높일 수 있음
- `json.load()` json 파일을 딕셔너리로 변환.

### 5.2 SQLite
#### 5.2.1 Overview
>- 가벼운 RDBMS
- 서버 설치가 필요 없고, Python 내장 모듈로 쉽게 사용 가능
- 데이터 저장, 조회, 관리 등을 SQLite를 활용

#### 5.2.2 기능
```
import sqlite3

# 데이터베이스 연결
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# SQL 명령어로 테이블 생성
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
city TEXT
)
""")
print("테이블이 생성되었습니다!")

# 데이터 삽입
cursor.execute("INSERT INTO users (name, age, city)
VALUES (?, ?, ?)",
("Alice", 30, "New York"))

# 여러 데이터 삽입
data = [
("Bob", 25, "Los Angeles"),
("Charlie", 35, "Chicago"),
("Diana", 28, "Houston")
]
cursor.executemany("INSERT INTO users (name, age, city)
VALUES (?, ?, ?)", data)
# 변경사항 저장
connection.commit()
print("데이터가 삽입되었습니다!")

# 데이터 조회
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
# 조회된 데이터 출력
for row in rows:
print(row)

# 데이터 수정
cursor.execute("UPDATE users SET age = ? WHERE
name = ?", (31, "Alice"))
# 변경사항 저장
connection.commit()
print("데이터가 수정되었습니다!")

# 데이터 삭제
cursor.execute("DELETE FROM users WHERE name = ?",
("Bob",))
# 변경사항 저장
connection.commit()
print("데이터가 삭제되었습니다!")


# 연결 닫기
connection.close()
```

## 6. 데이터 시각화
### 6.1 Matplotlib
>- matplotlib은 Python에서 데이터를 시각화하기 위한 가장 기본적인 라이브러리다.

### 6.2 선형 그래프
>- 선형 그래프는 데이터 점을 선으로 연결하여 값으 변화 추이를 시각화 하는 그래프다.
- 주로 시계열 분석이나, 연속적인 데이터 비교에 사용한다.
- 그래프 생성 옵션
   - `plt,plot`: 선형 그래프를 생성하는 함수.
   - `marker`: 각 데이터 포인트를 나타내는 기호
   - `color` : 선 색상
   - `plt.grid` : 배경에 격자를 추가하여 가독성 향상

```
import matplotlib as plt
...

plt.plot(x, y, ...)
...

plt.title("...")
plt.xlabel("...")
plt.ylabel("...")
plt.legend()

plt.grit(True) # 격자 추가
plt.show()
```

### 6.3 막대 그래프
>- 막대 그래프는 카테고리형 데이터를 시각화
- 각 막대의 높이 또는 길이가 해당 데이터 값의 크기를 나타냄
- 그래프 생성 옵션
   - `plt.bar` : 막대 그래프를 생성하는 함수
   - `color` : 색상
   - `edgecolor` : 막대 테두리 색상

```
categories = [...]
values = [...]

plt.bar(categories, values, ...)
#plt.barh <= 수평 그래프
...
```

### 6.4 히스토그램
>- 데이터를 구간별로 나누어 빈도를 시각화 하는 그래프
- 주로 데이터 분포를 파악할 때 사용
- 그래프 생성 옵션 
   - `plt.hist` : 히스토그램을 생성하는 함수
   - `bins` : 데이터를 나눌 구간 수
   - `alpha` : 막대 투명도 설정(0.0 - 1.0)
   
 
## 7. 데이터 시각화 - 고급
### 7.1 Seaborn
#### 7.1.1 Overview
>- Seaborn은 데이터 시각화를 위해 설계된 Python 라이브러리
- 복잡한 데이터를 쉽게 이해할 수 있도록 다양한 플롯을 제공한다.

```
import seaborn as sns
import matplolib.pyplot as plt
import numpy as np

data = np.random.rand(10,10) # 예제 데이터 생성, 
mask = np.triu(np.ones_like(data, dtype=bool)) # 상단 삼각형 마스킹
```


### 7.2 히트맵(Heatmap)
>- 데이터의 관계를 행과 열로 나열하고 값의 크기를 색상으로 표현
- 변수 간 상관 관계, 범주형 데이터의 빈도 시각화에서 활용
- 그래프 생성 옵션
   - `annot` : 셀에 숫자를 표시
   - `cmap` : 색상 팔레트 
   - `mask` : 특정 영역 숨기기
   
```

sns.heatmap(data, annot=True, mask=mask, cmap='coolwarm')

plt.title("Heatmap Example")
plt.show()
```
### 7.3 박스 플롯
>- 데이터의 분포를 한눈에 보여주는 플롯
- 중앙값, 사분위 범위, 이상치를 확인하는 데 사용
- 그래프 생성 옵션
   - `box` : 데이터의 중앙값과 1, 3 사분위수를 나타냄
   - `Whiskers` : 데이터의 최소/최대 값을 표시
   - `Point` : 이상치를 나타냄

```
tips = sns.load_dataset("tips")

sns.boxplot(x='day', y='total_bill', data=tips, palette='Set2')
plt.title(...)
plt.show()
```
### 7.4 바이올린 플롯
>- 팝ㄱ스플롯의 기능을 포함하면서 데이터 분포 밀도를 보여줌
- 데이터의 대칭성과 분포 패턴을 확인하는 데 유용하다.

```
sns.vioilnplot(..., palette='muted', split=True)
```
