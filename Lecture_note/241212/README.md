## 1. if 문
if문은 다음과 같이 사용한다.
```
if  {condition}:
	statement1
    statement2
    ...
elif {condition}:
	statement1
    statement3
    ...
else:
	statement1
    statement4

```

> **주의점**
- 콜론(`:`)을 붙이는 것을 잊지마라
- 들여쓰기(indentation)에 주의하라.(관련 익스텐션을 활용하면 이 실수를 방지할 수 있다.)

C 언어를 다루는 [이 문서](https://velog.io/@chris-mk/C-%EC%84%A0%ED%83%9D%EB%AC%B8)에서 선택문과 관련된 Insight를 참고할 수 있다.


## 2. 반복문
반목문과 관련된 Insight는, C언어를 다룬 [이 문서](https://velog.io/@chris-mk/C-%EB%B0%98%EB%B3%B5%EB%AC%B8)에서 참고할 수 있다.

### 2.1 while 문
while 문의 구조는 다음과 같다.
```
while {condition}:
	statement1
    statement2
    statement3
    ...
```
- 강제로 while 문을 빠져나가야 하는 경우 `break` 문을 사용하면 된다.
- while 문의 처음(`condition`)으로 돌아가기 위해선 `continue`를 사용한다.

### 2.2 for 문
for 문의 구조는 다음과 같다.
```
for {variables} in {iterable object} 
	statement1
    statement2
    statement3
    ...
    
```
>**`range`** 함수
`range(a,b,c)`
- a: 시작지점을 말한다. (생략된 경우 0이 기본값이다.)
- b: 탈출 지점
- c: 방향(생략가능)
`range` 함수는 range 클래스의 객체를 반환하며 이 객체는 iterable하다.

>**list comprehension**
예제를 보는게 이해가 빠르다.
`[num for num in a if num%2 == 0]`
if문은 생략이 가능하고, for문은 반복 가능하다.


## 3. 함수(function)
### 3.1 개요
```
def function_name(parameters):
	statement1
    statement2
    ...

```
`return` : 함수의 결과 값을 돌려주는 명령어.
(해당 명령어가 없으면 함수는 `None`을 반환한다.)

### 3.2 매개변수
>parameter와 argument는 다르다. 전자는 매개변수, 후자는 인수라고 불린다. 후자는 함수 호출시 전달하는 값이고 전자는 이 값을 저장해두기 위한 변수다.

>함수 호출 시, 매개변수의 값을 순서와 상관없이 지정할 수도 있으며, 함수를 정의할 때에 디폴트값을 정의할 수 있다.(주의: 이는 항상 뒤쪽에 놓아야 한다.)

### 3.3 다양한 매개변수
>입력값의 갯수를 정의하지 않기 위해서, `*`를 매개변수 앞에 붙여줄 수 있다. 이 경우, 인수들은 튜플로 전달된다.(이거도 뒤쪽에 놓아야한다.)

>**kwargs**
매개변수 앞에 `**`를 붙여주면 튜플이 아닌 딕셔너리 형태로 인수를 전달할 수 있다.

### 3,4 전역변수
>**global**
함수 바깥에서 정의된 변수는 함수 내에서 `global {variable}` 명령어를 써서 사용할 수 있다. 하지만 함수의 독립성을 위해 이는 지양되어야 한다.

### 3.5 lamda 예약어
>- 함수를 생성할 때 사용하는 예약어로 함수를 한 줄로 간결하게 만들 때 사용한다. 
- 함수를 매개변수로 받아서 처리하는 함수에서 주로 사용한다.
```
## lamda 예시
add = lamda a, b: a+b
result = add(3, 4)
```

### 3.6 파이썬 내장함수
- `abs(x)`
- `all(x)`: `x`가 모두 참이면 True
- `any(x)`: `x`중 하나라도 참이면 True
- `chr(i)`: 유니코드 숫자를 문자로 리턴
- `dir(x)`: 객체가 사용가능한 메서드
- `divmod(a,b)`: 몫과 나머지를 튜플로 리턴
- `enumerate(x)`: 인덱스와 값을 enumerate 객체로 리턴
- `hex(x)`: 정수 값을 16진수로 변환
- `id(object)`: 객체가 참조하는 메모리 주소 반환
- `filter(f, iterable)`: 함수에 전달하면 참을 출력하는 시퀀스 데이터를 리턴한다.
- `map(f, iterable)`: `filter`와 다르게 입력값에 대응하는 출력값을 리스트로 반환한다.
...(그 밖에 필요한 내장함수는 그때마다 서치해보자)


## 4. 파이썬 입출력
### 4.1 사용자 입출력
```
number = input('put your number: ')
print('your number is ', number)
```

### 4.2 파일 입출력
```
f = open("{file}", {mode})
...
f.close
```
|모드|설명|
|-|-|
|r|읽기모드|
|w|쓰기모드(기존 데이터를 덮어쓴다. 해당 파일이 없으면 새로운 파일이 생성된다.)|
|a|추가모드|

- `write` 메서드를 사용하면 파일에 직접 써서 출력할 수 있다.
- `readline`: 메서드를 통해 라인 단위로 읽어들일 수 있다. `readlines`는 각 줄을 요소로 하여 리스트를 리턴한다.
- `read`: 파일 내용 전체를 문자열로 리턴

>```
with open("foo.txt", "w") as f:
	f.write(...)
  
 ### 4.3 try 문
 #### 4.3.1 -except, -finally, -else문
 try-except문은 다음과 같이 사용한다.
 ```
 try:
 	...
 except {error} as {error variable}
 	...
 ```
 - except문은 여러개를 사용할 수 있다. 동등하게 다루기 위해서는 괄호로 함께 묶어 처리해야한다.
 
 - `finally`를 `except`대신 사용하기도 하는데, `finally`절은 예외 발생 여부와 상관없이 항상 수행된다.
 - `else`문도 사용할 수 있다. `try`문에서 오류가 없을 경우에만 수행하는 절이다.
 - 특정 오류가 발생할 경우 `pass`를 `except`절 안에 넣음으로써 통과시킬 수 있다.

#### 4.3.2 예외 정의
- `raise MyError()`, `raise NotImplementedError()`는 강제로 오류를 발생시킨다.

파이썬 내장 클래스인 `Exception` 클래스를 상속하여 사용자 정의 예외를 생성할 수 있다.
```
class MyError(Exception):
	pass
```


 
 
 