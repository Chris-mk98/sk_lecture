## 1. 파이썬이란

### 1.1 파이썬의 특징

> - Guido Van Rossum이 개발한 인터프리터 언어
>   ㄴ 인터프리터 언어는 코드를 한 줄씩 실행하는 것이 특징이다.

- 인스타그램, 넷플릭스, 아마존 등에서 사용
- 공동 작업과 유지 보수가 매우 쉽고 편리함
- 문법이 쉬워 상대적으로 빠르게 배울 수 있다.
- 무료지만 강력하다.
  ㄴ 속도가 필요한 부분은 C로 코드를 작성하여 파이썬 내에 포함시킬 수 있음 속도가 필요한 부분은 C로 코드를 작성하여 파이썬 내에 포함시킬 수 있음

### 1.2 파이썬으로 할 수 있는 일

> - 웹 프로그래밍

- 인공지능/머신러닝
- 수치 연산 프로그래밍
- 데이터 분석, 데이터베이스 프로그래밍
- 시스템 유틸리티 제작하기
- GUI 프로그래밍
- IOT

### 1.3 파이썬으로 할 수 없는 일

> - 시스템과 밀접한 프로그래밍 영역

- 모바일 프로그래밍

## 2. 파이썬 시작하기

### 2.0 환경 설정

> - 파이썬 설치

- vscode 설치
- extension 설치
  - python
  - jupyter
  - 그 밖에 본인이 필요한 것들...

### 2.1 편리한 Tool: Jupyter notebook

> ![](https://velog.velcdn.com/images/chris-mk/post/00470efd-5b44-4a46-8377-00a86fb3e758/image.png)
> 위의 사진처럼 `.ipynb` 파일을 통해 jupyternotebook을 사용할 수 있다.
> ![](https://velog.velcdn.com/images/chris-mk/post/ef070925-0a01-4fb9-973c-1ea243d28ee1/image.png)
> ![](https://velog.velcdn.com/images/chris-mk/post/934f08da-8304-453e-b987-e92a7f3a41c1/image.png)
> `+code` 버튼을 누르면 '셀'이 추가되며 셀에 들어간 코드별로 실행할 수 있다.

> **Jupyter notebook Cheat sheat**
> `contorl` + `return` : 해당 셀만 실행
> `alt` + `return` : 해당 셀 실행 후 새로운 셀 추가

## 3. 변수

### 3.1 변수란?

파이썬에서 '변수'는 '객체'를 가리키는 것이다.
쉽게 풀어서 설명해보자면, '객체'란 객관적인 지위에서 지칭의 대상이 될 수 있는 것이라고 말할 수 있다.

> `num=10`

- 10 데이터를 **메모리 공간**에 저장하고, 해당 **메모리 공간의 주소**를 `num`이라는 메모리 공간에 저장한다.
- 실제로 `10`은 '객체'로서 `10`과 관련된 여러 속성들과 함께 메모리공간에 저장된다.
- 즉 위의 선언(declare)은 객체를 위한 메모리공간, 객체의 메모리 주소를 담는 메모리공간 두 개를 할당하게 된다.

### 3.2 자료형의 종류

**자료형**: 프로그램에서 나타낼 수 있는 데이터의 종류다. 아래는 파이썬의 자료형이다.
**동적 타이핑**: 컴파일 언어와 다르게 파이썬에서는 프로그램이 실행되는 시점에서 메모리의 타입을 결정하게 된다.

> - bool

- string
- number
- list
- set
- dictionary
- tuple
- None

### 3.3 변수명 명명규칙

> - 문자와 숫자 그리고 `_`는 사용 가능하다.

- 변수명은 대소문자를 구분한다.
- 변수명은 의미 있는 단어로 사용하는 것이 좋음
- 변수명이 숫자로 시작하면 할 수 없음
- 변수명에는 공백이 포함될 수 없음
- 예약어를 변수명으로 사용할 수 없음

### 3.4 복사

`b` 변수에 `a` 변수를 할당하면 `b`는 `a`의 주소값을 가지게 된다. 이는 `id()`함수로 쉽게 확인할수 있다.
![](https://velog.velcdn.com/images/chris-mk/post/9c2435cb-e268-4ce5-8d3b-ca76af16e9e8/image.png)

### 3.5 선언방법

> - Bool
>   `a = True`

- number
  `a = 10`
- string
  `a = 'python`
- list
  `a = [1, 2, 3]`
- tuple
  `(a, b) = 'python', 'life'` or `a, b = ('python', 'life')`
  ... ...

`a, b = b, a`를 통해 두 값을 바꿀 수도 있다.

### 3.6 숫자형

| 항목   | 파이썬 예시             |
| ------ | ----------------------- |
| 정수   | 123, -345, 0            |
| 실수   | 123.45, -1234.5, 3.4e10 |
| 8진수  | 0o34                    |
| 15진수 | 0xFF                    |

- 정수형: 정수를 뜻하는 자료형
- 실수형: 소수점이 포함된 숫자.

#### 3.6.1 숫자형 연산

- 사칙연산(+,0,\*,/)
- 제곱: \*\*
- 나머지 연산: %
- 나머지 몫: //

### 3.7 문자열 자료형

**문자열** 이란 문자, 단어 등으로 구성된 문자들의 집합, **sequence**라고도 함. 문자열은 `""`.이나 `''`으로 감싸서 표현한다.

>

```
"""
따옴표 세 개는
문자열 형식 그대로를 나타내준다.
"""
'''
작은 따옴표도
마찬가지다.
'''
```

#### 3.7.1 문자열 연산

문자열은 서로 더할 수 있으며(+)
숫자와 함께 곱할 수 있다.(`'a'*9`)
`len()` 함수를 통해 문자열의 길이를 알 수 있다.

#### 3.7.2 문자열 인덱싱과 슬라이싱

- 문자열 인덱싱
  index는 0부터 n-1까지 존재한다.
  `a[index]`는 문자열 안의 특정 값을 뽑는다. `-`(마이너스)는 뒤에서부터 인덱스를 센다.(이때 -1부터 시작한다.)

- 문자열 슬라이싱
  `a[start:end]`: start 부터 end-1번 인덱스의 문자를 뽑아냄.

#### 3.7.3 문자열 포매팅

| 코드 | 설명        |
| ---- | ----------- |
| %s   | 문자열      |
| %c   | 문자 1개    |
| %d   | 정수        |
| %f   | 부동소수    |
| %o   | 8진수       |
| %x   | 16진수      |
| %%   | 문자 % 자체 |

> `%<문자열에 쓸 칸수><소수점이하 자리수><문자열 코드>`

- `%10s`: 최소 10칸을 문자열을 표현하는데 사용함(음수면 좌측정렬)
- `%10.4f`: 10칸을 차지하는 소수점이하 4자리로 표현하는 부동소수

> **문자열 포매팅 사용 예시**

- `%10.4f' % 3.1415926483`
- `'I eat {1} apples and {0} bananas'.format(number, 5) `

> **정렬**
> `{0:<10}` 좌측정렬
> `{0:>10}` 우측정렬
> `{0:^10}` 가운데 정렬

> ** f 문자열 포매팅(.format 메소드)**
> `f'나의 이름은 {name}입니다. 나이는 {age}세 입니다.'`
> `'{<출력할 객체><:><공백을 채울 문자><정렬방향><츌력에 사용할 칸 수>.<소수점 이하 자리수><포매팅 첨자>}'`
> ![](https://velog.velcdn.com/images/chris-mk/post/a58974df-7d82-4e9f-860c-73f5ea0d8778/image.png)

#### 3.7.4 문자열 메소드

> - count

- join: 문자열 삽입(ex: `".".('abcd')`
- find: 찾는 문자열이 처음 나온 ㅜ이치 반환 없으면 -1 반환
- index: `find`와 같지만 없으면 오류를 뱉는다.
- upper, lower: 대문자, 소문자 변환
- lstrip, rstrip, strip: 좌우 공백 지우기, 모든 공백 지우기
- replace: 문자열 바꾸기(ex:`a.replace('바꾸기 전','바꾼 후')`)
- split: 문자열 나누기(ex: `a.split(':')`)
  ㄴ 이 경우 공백 또는 특정 문자열을 기준으로 분리하여 리스트로 반환한다.

### 3.8 불(bool) 자료형

참과 거짓을 나타내는 자료형이다.
`bool()` 함수는 자료형의 참/거짓을 식별하는 내장함수다.

### 3.9 연산자

> - 산술연산자

- 관계연산자: 대소 비교, 일치 여부
- 논리연산자: `and`, `or`, `not`
- 대입 연산자: `=`. `+=`, `**=` ...
- 멤버 연산자: `in`, `not in`
- 식별 연산자: `is`, `is not`(논리연산자와 다르게, 메모리 위치를 비교한다.)

### 3.10 리스트

- 자료형의 집합을 표현할 수 있는 자료형이다.
- 리스트는 문자열과 마찬가지로 인덱스를 활요할 수 있다.
- 리스트는 어떤 자료형도 포함 할 수 있다.

#### 3.10.1 리스트 연산

> - `+`는 리스트를 합치는 기능이다.

- `*`는 리스트의 반복을 의미한다.
- `len()` 함수는 리스트의 길이도 구해준다. 튜플, 딕셔너리에서도 사용할 수 있다.

#### 3.10.2 리스트 수정 및 삭제

> - `del` 키워드를 통해 리스트 요소 삭제가 가능하다.(ex: `del a[2:]`)

- `append` 메서드를 통해 리스트의 맨 마지막에 요소를 추가한다.
- `sort`: 리스트의 요소를 순서대로 정렬한다.
- `reverse`: 리스트를 역순으로 뒤집어준다.
- `index`: 요소를 검색하여 위치 값을 반환한다.
- `insert(a,b)`: a번째 위치에 b를 삽입한다.
- `remove(x)`: 처음으로 나오는 `x`를 삭제한다.(인덱스를 search하는 것이 아니다.)
- `pop(x)`: `x` 번째 요소를 반환하고 해당 요소 삭제.(`x`가 없으면 맨 마지막 요소)
- `count(x)`: `x`의 리스트 내 개수.
- `extend`: 리스트에 리스트를 더하는 메서드.

### 3.11 튜플

튜플이란 리스트와 유사한 자료형이나 `()`로 둘러싼다는 점, 1개의 요소만을 가질 때에도 쉼표를 뒤에 붙여주어야한다는 점, 소괄호`()`를 생략해도 된다는 점, 수정 변경이 불가능하다는 점에서 차이점을 가진다.

### 3.12 딕셔너리

딕셔너리는 `{Key: Value}` 쌍으로 구성되어 있다.

#### 3.12.1 딕셔너리 쌍 추가 및 삭제

> - 추가
>   `a['name'] = 'chris'`

- 삭제
  `del` 키워드 사용(`del a['name']`)

#### 3.12.2 주의사항

> - 딕셔너리에는 동일한 Key가 중복으로 존재할 수 없음

- Key에는 변할 수 있는 객체를 쓸 수 없다. 하지만 Value는 변할 수 있는 객체를 넣을 수 있다.

#### 3.12.4 딕셔너리 메서드

> - `keys`: 딕셔너리의 Key들을 `dict_keys` 객체로 반환한다. 리스트처럼 사용하능하나 리스트 메서드를 사용하기 위해서는 별도의 객체를 생성해주어야 한다.

- `values`: 딕셔너리의 Value만을 모아 `dict_values` 객체를 반환한다.
- `items`: 딕셔너리의 쌍을 튜플로 묶어 `dict_items` 객체를 반환한다.
- `clear`: 딕셔너리 내의 모든 요소 삭제
- `in`을 통해 Key가 딕셔너리 안에 존재하는지 알 수 있다.
- `get`

### 9. QnA

> Q1) 리스트 내의 값들도 객체면 리스트는 객체를 포함하는 객체인데 그러면 리스트는 원소들의 주소값을 담고 있는 객체인가?
> A1) 그렇다. `a=[1,2,3,4,5]`에서 `a`는 `[1,2,3,4,5]`의 주소값을 가리키고. `[1.2.3.4.5]`는 `1`~`5`의 각 주소값을 담고 있다. `id()`함수를 쓰면 해당 변수의 메모리 주소를 알 수 있다.

> Q2) `a=10`, `b=a`라고 선언하면 `a`와 `b`는 같은 주소를 가리키는데, `a+=1`을 실행하면 `a`는 `b`와 다른 값이 저장된 주소를 가리키게 되나요?
> A2) 그렇다. 아래 사진을 보면 메모리 주소가 달라짐을 알 수 있다.
> ![](https://velog.velcdn.com/images/chris-mk/post/91a1b7d2-27e4-4817-82df-fb164f27fcab/image.png) 후에 해당 객체를 아무도 참조하지 않는다면 가비지 컬렉터에 의해 메모리에서 삭제된다.
