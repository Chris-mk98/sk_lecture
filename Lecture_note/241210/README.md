## 1. 클라우드 데이터 센터
### 1.1 Cloud 란
- 데이터 센터
데이터센터는 기업이 다양한 네트워크 형식의 컴퓨팅 및 스토리지 인프라를 수용하는데 사용하는 물리적 시설

### 1.2 데이터 센터 아키텍처
- Physical Server
	-랙, 유닛, 클러스터 스위치
    ![](https://velog.velcdn.com/images/chris-mk/post/ccbdff7d-fcb0-4c1b-853d-79e51e9cc63f/image.png)

PUE 는 데이터 센터 인프라의 효율성과 역상관의 관계를 가진다.

[데이터센터 Tier 기준](https://blog.daouidc.com/blog/data-center-redundnancy-tier)
    
### 1,3 클라우드 데이터센터
AWS
AZURE
Goolge
Alibaba
salesforce
IBM Cloud
Oracle
Tencent

### 1.4 Region Availability Zone
>WS 리전은 더 높은 가용성, 확장성, 내결함성을 위해서 다중의 가용역역으로 구성된다. 어프릴케이션과 데이터는 다른 가용영역 간에 실시간 복제가 되며 일관성을 가진다.

>리전은 AWS가 전 세계에서 데이터센터를 클러스터링하는 물리적 위치다.

>가용역역은 AWS 리전의 중복 전력, 네트워킹 및 연결이 제공되는 하나 이상의 개별 데이터 센터로 구성된다.

>AZ 설계
= 완전히 격리된 하나 이상의 데이터 센터
- 충분한 물리적 거리
- 자가 전력 인프라
- 수십만 대 규모의 서버
- 완전히 격리된 다중 metro fiber

>AWS network design
![](https://velog.velcdn.com/images/chris-mk/post/c485a88d-c0da-4bfb-8a1f-709d4c5e7616/image.png)


>서울 리전 : AP-NORTHEAST-2 - 네 개의 AZ - 데이터센터- 랙 - 호스트


### 1.5 Cloud Compute


>인스턴스 유형
- M5d.xlarge
	- M : 인스턴스 패밀리
	- 5 : 인스턴스 세대
	- d : 추가기능
	- xlarge : 인스턴스 크기
    
    
>인스턴스 크기
xlarge 8시간 운영비용 = 8xlarge 1시간 운영비용



## 2. Cloud Native Microservice
> Cloud Miration
Pay as you go

landscape.cncf.info
>**선택 가이드**
쿠버네티스, 컨테이너 => CNCF
Bigdata => Apache

### 2.1 Microservices
> 전통적인 APP vs Microservice
Traditional : 모든 기능을 하나의 소스를 통해 동기식으로 구현 / Cost Efficiency low
Microservice : 각 기능을 비동기식으로 구현 / Cost Efficiency high/ Easier Updates

기존 서비스는 모듈화를 통해 Microservices를 만든다. 이는 Distributed Computing 과 같은 구조를 갖는다.(= Network of Services)

> Netfkix 서비스 흐름도
![](https://velog.velcdn.com/images/chris-mk/post/dc37a384-20c3-47fe-8e00-782846643c4a/image.png)

>**Service Discovery**
서비스 클라이언트가 서비스 레지스트리에 마이크로서비스의 IP를 질의하고 답변을 통해 Microservice를 호출한다.
-Failure of a Service : Microservice에서 장애가 일어나면, 장애는 전파될 수 있다. 이를 막기 위해, 일정한 조건에서 default response를 하는 것으로 설정한다.

>**Service Auto-Scaling** : 서비스의 동적인 생성, 추가, 


### 2.2 Container / Kubernetes
>**가상화**
![](https://velog.velcdn.com/images/chris-mk/post/100eaed4-3d7e-4ce9-878c-e3225ed27326/image.png)

>**컨테이너**
![](https://velog.velcdn.com/images/chris-mk/post/111b9439-fc97-485e-ac6f-20851d571917/image.png)
Host OS 관점에서 컨테이너는 프로세스로 다뤄진다.(VM보다 가볍다)

>장점
- 표준화된 환경
- 배포 용이성
- 자동화 환경(CI/CD)
- 이미지 의존성 자동관리

>**descriptor**
![](https://velog.velcdn.com/images/chris-mk/post/85ca5992-0d59-4856-af9f-7f71c95a9246/image.png)


> **kubernetes (=k8s)**
![](https://velog.velcdn.com/images/chris-mk/post/2e9a7962-8ae3-4c37-a094-93c80dde0693/image.png)
![](https://velog.velcdn.com/images/chris-mk/post/c06ba590-87a1-45e3-a695-0eea8243fe28/image.png)



## 3. 생성형 AI의 트렌드 및 보안 위협
### 3.1 Sora
>오픈AI는 텍스트와 이미지, 비디오를 '소라'에 더 쉽게 입력할 수 있도록 새로운 인터페이스를 개발했다. 자신만의 자산을 가져와 확장, 리믹스, 블렌딩하거나 텍스트에서 완전히 새로운 콘텐츠를 만들 수 있다.

### 3.2 인공지능이란?
> 인간의 학습, 추론, 지각 능력을 인공적으로 구현하려는 컴퓨터과학의 세부 분야 중 하나.

### 3.3 인공지능과 하드웨어
> CPU와 달리 GPU는 ALU 구성비가 매우 높다. 
- High compute density
- High Computations per Memory Access
- Built for parallel operations

### 3.4 학습방법
1. 지도 학습: 문제와 정답을 모두 알려주고 공부시키는 방법 => 예측, 분류
2. 비지도 학습: 답을 가르쳐주지 않고 공부시키는 방법 => 연관 규칙, 군집
3. 강화 학습: 보상을 통해 행위를 가오하하는 학습 => 보상

### 3.5 자연어 처리(Natural Language Processing, NLP)
>인공지능의 하위 분야로, 컴퓨터가인간의 언어를 알아들을 수 있게 만드는 학문분야다. 

>**자연어처리 과정**
![](https://velog.velcdn.com/images/chris-mk/post/2cf5e976-cd7a-4f01-bdee-7c196a3a80d2/image.png)

>**LM과 LLM**
- **언어모델(LM)**은 입력값을 기반으로 통계학적으로 가장 적절한 출력값을 출력하도록 학습된 모델이다. GPT는 언어 모델을 가리키는 말이다. chatGPT는 이 언어모델을 활용한 서비스를 가리키는 말이다.
- **LLM(Large Language Model)**은 이를 확장한 모델이다.

>**Lamda**
- 구글에서 개발한 인공지능 언어 모델
- Transformer 알고리즘을 사용하지만 대화문을 학습하여 대화에 특화된 것이 특징

>**Gemini**
LaMDA와 PaLM을 기반으로하는 인공지능 검색 엔진 서비스

>**ClovaX**
Hyper Clova 언어모델을 사용하는 대화형 AI 서비스

>**LLaMA**
LLaMA는 메타의 오픈소스 언어모델

>**sLLM**
sLLM은 특정 분야에 한정하여 깊이 있는 데이터를 학습할 수 있다는 점이 장점

>**GAI(생성형 인공지능)**
대규모 데이터를 가지고 학습하여 명령어에 따라
![](https://velog.velcdn.com/images/chris-mk/post/6866a13f-12d3-4da7-9d08-419b9f327bf8/image.png)

- self attention
- VAE(Variational Autoencoder)
- GAN(Generative Adversarial Network)
- Diffusion
	- stable diffusion
- ClIP

Attention is All you need 논문

프롬프트 엔지니어링: 질문을 할 때, 구체적인 배경을 함께 제시해주어야 함.
GPTs : "GPT를 특정 목적에 맞게 사용한다."

### 3.6 생성형 인공지능 툴
>**예시**
LilysAI
Gamma ***
Canva
Claude(대화형 AI 언어 모델): Anthropic에서 개발한 ChaGPT와 유사한 기능/ RAG 기법 사용
Perplexity : 인공지능 기반의 검색 엔진, 세부적인 연구에 적합
뤼튼(wrtn): 
Padlet
DeepL: 번역
NoteGPT
Playground
Artbreeder
NotebookLM: 구글 무로 솔루션. 소스를 직접 추가

### 3.7 생성형 AI의 보안 위협
>**LLM의 문제점**
- 전기소모
- **보안이슈**


>**주요 사례**
- 피싱 메일 및 악성코드 생성
- 양면적 측면에서의 취약점 분석
- AI에 의해 생성된 소스코드는 최신의 보안 조치가 적용되지 않음.

>- Enumeration
- Foothold: 공격자가 내부 시스템에 거점/발판을 설치하는것
- Reconnaissance: 정찰
- Polymorphic code: 원래 알고리즘의 기능을 유지하면서 다형성 엥ㄴ진을 사용하여 스스로를 변경할 수 있는 코드 유형. 셸코드 생성에 활용/ 다형성 멀웨어 생성에 활용 가능하고 탐지를 회피할 수 있다.

>- Auto-GPT : 자연어로 됨 목표를 받아 하위 작업으로 나누고 인터넷과 기타 ㄱ도구를 자동으로 활용하여 달성하려는 AI 에이전트
CVE-2023-37275
CVE-2023-37273
CVE-2023-37274


### 3.8 메타버스 정보보호
>메타 레이벤-CES 2024
보안 이슈 : I-XRAY



## 4. 주요 랜섬웨어 Trend
### 4.1 랜섬웨어 패러다임
> **코로나 19 이후 랜섬웨어 트렌드 변화**
-  비대면 활동으로 보안 사각지대 위협 증가
	- 원격근무 환경을 노린 공격
    - 취약한 VPN, RDP 등 원격 근무 환경을 통한 기업 네트워크 침투
    - 악성 웹사이트, 처부파일을 포함한 이메ㅐ일 공격
    - 국가 지원 해킹 그룹의 공격과 위협 대상 확대 및 다양화
- 랜섬웨어 타겟 변경(개인 -> 기업)

> **서비스형 랜섬웨어 주도**
- 사이버 범죄 조직화/분업화
    - 개발자, 유표자, 공격자, 협상가를 룬 조직적인 시스템
    - 암호화폐를 통한 익명성 보장
    - RaaS 제작자는 일정액의 수수료 혹은 범죄 수익을 배분받음
    - 표적 공격과 결하보딘 RaaS의 위협 확대
- 랜섬웨어 협박 고도화
    - 비협상: 다크웹을 통한 데이터 판매, 재공격 등
    - 협상: 파일복호화(1차) > 데이터 협박(2차) > 취약점 제공(3차)
  
> **침해사고 동향** 
- 정보유출
   - 22년: Lapsus$
   - 23년: IAB 활동, 국내 제조 피해
- 악성코드
   - 22년: 서비스형 랜섬웨어, 국내 기업 타깃형 랜섬웨어
   - 23년: 대규모 랜섬웨어 공격, 디페이스 공격
- 피싱/스캠
   - 22년: 사회적 이슈 악용
   - 23년: 생성형 AI, 피싱 코인
- 기타

>IAB: Initial Access Broker의 약자, 초기 침투에 대한 경로를 제공하거나 수행하는 브로커,
믹싱 서비스: 암호화폐 거래 내역을 숨기기 위해 송/수신 트랜잭션을 난독화하는 기술

### 4.2 24년 유형별 주요 침해사고

랜섬웨어 동향
비대칭키를 활용한 파일 암호화로 인해, 완전한 데이터복구가 불가능해짐

>**24년 동향**
- 취약점
   - 네트워크 장비 취약점 악용
   - 클라우드/서버 설정 미흡
- 멀웨어
   - LotL 기법(Living off the Land)
   - RMM 도구(Remote Monitoring and Management)
- 사회공학
   - AI활용 딥페이크, 딥페이스
   - 크리덴셜 스터핑
- 기타
   - 서드파티, 렵력업체 공격 사례 증가
   - 내부자 소행으로 인한 정보 유출
   - SW 대상 공급망 공격 발생
   
21년 이래로 24년까지 점점 Time to Exploit은 감소해왔다.(768H->114H)
취약점 공개 관련 페이지: https://www.exploit-db.com/


## 5. 보안 대책 상세
### 5.1 랜섬웨어 위협 사전점검 서비스
>1. 데이터 백업, 보안 Qiuick-Win 점검
2. 랜섬웨어 모의훈련 서비스
3. 모의해킹 기반 대응 수준 평가
4. 랜섬웨어 위협 진단 Tool

### 5.2 랜섬웨어 탐지 서비스
>**주요 솔루션**
- MDR(Managed Detection & Response)
- EDR(Endpoint Detection & Response)
- XDR(eXtended Detection * Response)
- XMDR ... 

### 5.3 랜섬웨어 대음 및 복구 서비스
> **대응 및 복구 서비스**
1. 데이터 보안 백업 서비스
2. 랜섬웨어 Top-CERT 서비스
3. 랜섬웨어 협상 서비스
4. 랜섬웨어 복구 서비스
5. 다트웹 정보 유출 탐지 서비스
6. 사이버 보험

## 6. AI 보안
관련 해외자료: OWASP TOP 10 for LLM Application

>1. 프롬프트 인젝션
- 악의적인 입력을 통해 LLM을 조작하여 목적에 벗어난 답변을 유도하는 취약점
- 취약점 발생 지점에 따라 Direct Injection과 Indirect Injection으로 분류
- 공격 방식은 크게 목표 경쟁과 난독화로 나룰 수 있음

>프롬프트 인젝션 공격 방식
1. 목표경쟁: 접두사 주입, 스타일 주입, 상황극
2. 난독화: 특수 인코딩, 문자 변환, 단어 변환


>2. 불완전한 출력처리
- LLM이 생성한 출력에 대한 유효성 검저ㅡㅇ이 부족하여 발생
- 출력이 검증 없이 사용되면 XSS, SSRF, RCE 등의 취약점 발생

>3. 학습 데이터 중독
- 사전 학습 데이터 또는 파인튜닝/임베딩 과정에서 데이터를 조작하여 백도어 또는 편견을 주입하여 모델 자체를 손상시키는 공격

>4. 모델 서비스 거부
- 많은 자원을 사용하게 만드는 요청을 통해 LLM에 과부하를 일으켜 서비스 장애를 유발하거나 과도한 리소스 비용을 초래하는 공격

>5. 공급망 취약점
- LLM 애플리케이션 개발 과정에서 취약한 구성 요소를 사용하여 발생하는 취약점
- 검증되지 않은 모델이나 외부 데이터 셋을 사용할 경우 취약 가능성 존재

>6. 민감 정보 노출
- LLM 애플리케이션 응답을 통해 개인 정보 및 내부 정보와 같은 민감 저옵가 노출되는 취약점

>7. 부적절한 플러그인 설계

>8. 과도한 에이전시
- 자율적으로 플러그인을 실랳ㅇ하는 에이전트 구성 시 과도한 기능을 부여하여 발생

>9. 과도한 의존
- LLM이 생성한 콘텐츠에 과도하게 의존해서 생기는 문제

>10. 모델 탈취
- LLM 모델에 대한 무단 접근, 복사, 유출 등에 관한 위협

> 안전한 AI 활용 방안
1. 안전한 AI 서비스 구성
2. 프롬프트 보안 솔루션
3. 데이터 정제 솔루션

관련하여 참고하면 좋은 사이트: https://skshieldus.com/eng/business/insight.do
