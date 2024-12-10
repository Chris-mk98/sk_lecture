## 1. Git과 버전관리
버전: 유의미한 변화
패치: 시급한 문제점 해결, 사소한 버전 변경

버전 관리 시스템을 이용하면, 버전관리는 물론 변경점 관리, 백업 및 복구, 협업에 큰 이점이 있다.

**버전관리**는 **변경 내역을 기억**하고, **특정 시점의 버전으로 되돌릴 수 있다**는 특징을 바탕으로 **협업과정**에서 코드를 **쉽게 나누고 개발할 수 있도록** 도와준다.
![](https://velog.velcdn.com/images/chris-mk/post/401e20d2-b4de-4ccc-a81d-8070b8b85605/image.png)


## 2. Git
### 2.1 초기 설정
- 이름 설정: `git config --global user.name <사용자이름>`
- 이메일 설정: `git config --global user.email <email>`
- 설정 확인: `git config --global --list`


### 2.2 `init`, `add`, `commit` ...
- `git init` : 현재 위치에서 git 초기화
![](https://velog.velcdn.com/images/chris-mk/post/674cbfca-e0b8-4fda-8faa-5240fea5222c/image.png)
(`.git` 폴더는  숨김 폴더이므로 `-a`옵션으로 조회해야함.)

**git bash**를 활용하면 현재 폴더가 git에 의해 관리되는지 여부를 확인 할 수 있다.
![](https://velog.velcdn.com/images/chris-mk/post/decbd207-cebf-4cc1-a84f-c6439b69c34b/image.png)
>
잘못 설정된 `git init`은 
`rm -rf .git`로 삭제해주면 된다. 아니면 탐색기에서 숨김 폴더를 수동으로 삭제할 수 있다.

- `git status`: 현재 상태 확인
![](https://velog.velcdn.com/images/chris-mk/post/3e7d6ee9-12be-4806-a908-4355bcf6757a/image.png)

- `git add <파일>`: staging `.`를 사용하면 현재 디렉토리 전체를 대상으로 한다.
![](https://velog.velcdn.com/images/chris-mk/post/c8b823ad-cf44-4a51-8359-f03f9d87b2e8/image.png)

- `git commit -m '<메시지>'`: commit (`-am`: 한번 `add`된 파일을 스테이지에 올리지 않고 바로 commit)
![](https://velog.velcdn.com/images/chris-mk/post/bc933c62-0e39-419a-b249-a9d4c1616aec/image.png)
>`git status`로 커밋이 이뤄진 것을 확인할 수 있다.

- `git log`: 커밋 log 확인 (`--oneline`: 요약하여 확인)
![](https://velog.velcdn.com/images/chris-mk/post/56f8dbf9-d9b2-4e1a-b061-b5e1e8802195/image.png)

>파일을 수정한 뒤 다시 `git staus`로 확인하면, `add` 했던 파일의 변경을 추적하고 있음을 알 수 있다.
![](https://velog.velcdn.com/images/chris-mk/post/b7a59ac3-dafd-4740-a2b1-821ccf1376b2/image.png)

- `git diff`: 변경 부분 확인
![](https://velog.velcdn.com/images/chris-mk/post/d04c91d2-2a6c-4939-a66f-d361b015b346/image.png)

다시 커밋하면
![](https://velog.velcdn.com/images/chris-mk/post/1522c8c6-f216-4bab-8931-283e89d5d481/image.png)

- `git rm --cached <파일>`
add 한 파일 스테이지에서 내리기




### 2.3 git reset
- `--soft`: 해당 커밋이후 다음 커밋 직전 staging 상태로 복구
![](https://velog.velcdn.com/images/chris-mk/post/6c7c2a8f-9445-4e65-a856-b6f5997851cd/image.png)

- `--mixed`: 해당 커밋 이후 파일 변경이 반영된 상태, 하지만 `add`는 하지 않은 상태로 복구.

- `--hard`: 해당 커밋 직후 상태로 복구(해당 커밋 이후 파일 변경은 반영 안됨)
![](https://velog.velcdn.com/images/chris-mk/post/7363fe5e-8b30-48bd-b17e-2eeddffb1618/image.png)

#### **<요약>**
![](https://velog.velcdn.com/images/chris-mk/post/6903f857-0028-4b6d-97a9-d85434db9787/image.png)

### 2.4 branch
- `git checkout <commit id>` : 해당 커밋으로 체크아웃
![](https://velog.velcdn.com/images/chris-mk/post/35d511f9-770a-4aa4-8f8d-47b0c731d5a0/image.png)
![](https://velog.velcdn.com/images/chris-mk/post/d24b39f6-73bc-45f0-a15d-cd4658ec30ea/image.png)

체크아웃 후 STACK로 새로 커밋 해보았다.
![](https://velog.velcdn.com/images/chris-mk/post/e3c05385-c5ef-4d2c-ad24-455f29a4b5b8/image.png)

- `git switch -c <이름>` : 새로운 브랜치를 생성하기
git switch `이름` : 해당 브랜치로 이동
![](https://velog.velcdn.com/images/chris-mk/post/40ba579e-436e-44d1-992d-f446eb9eb57c/image.png)

- `git branch -l` : 브랜치 리스트 확인

- `.gitignore` 파일에 추적관리 제외할 파일을 추가하여 관리할 수 있다.
![](https://velog.velcdn.com/images/chris-mk/post/8e22cec0-977a-42ab-b0e0-d28643c2727c/image.png)
>git에 의해 추적되지 않음을 볼 수 있다.

### 2.5 remote repository
> 1. 프로젝트 폴더에서 `git init` 실행
2. 코드 작성
3. github에 업로드할 파일들을 선택: `add`
4. `commit` 수행
5. github에서 프로젝트 저장소 생성하기
6. 프로젝트 폴더에 github 저장소 주소 설정: `remote add origin <주소>`, 
7. `push` 실행(처음에는 `git push -u origin main`)

![](https://velog.velcdn.com/images/chris-mk/post/5c3a4e25-12e3-471f-b2b3-4021d97858b8/image.png)
![](https://velog.velcdn.com/images/chris-mk/post/3d1c0403-cd2e-4df8-b0a1-80ca64a31860/image.png)
>로컬과 달리, 온라인 커밋 메시지를 수정하는 것은 매우 복잡하고 권장되지 않는 방법이다. 따라서 7번 과정을 수행하기 전에 주의를 기울여야한다.

>cloning을 위해 새로 폴더를 만들면 이중으로 폴더를 생성하게 된다. 참고하자


- `git pull` 로 원격저장소에서 파일을 받아올 수 있다.



![](https://velog.velcdn.com/images/chris-mk/post/ae4f81da-9343-4c47-8069-7867b33b1c04/image.png)

main에서 dev 브랜치를 생성해보았다.
![](https://velog.velcdn.com/images/chris-mk/post/81b679ef-b38f-4a15-a8e1-958ed2388eae/image.png)
>feature 브랜치를 dev에서 생성하면 feature브랜치는 dev에 merge 해야한다.


### 2.6 기타
#### 2.6.1 권장 구성
>**1. New Features**
**2. Bug Fixes**
**3. Docuentation**
**4. Dependency Upgrades**
**5. Contributors**


#### 2.6.2 commit Convention
![](https://velog.velcdn.com/images/chris-mk/post/556b0464-0347-43c5-85e7-6a363176a624/image.png)