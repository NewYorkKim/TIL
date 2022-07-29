# GitHub 특강

> 2022/01/12 ~ 2022/01/14



## 1. Why Git and GitHub?

##### (분산) 버전 관리 프로그램

- 변경사항 
- 백업
- 협업
- Who/When/What/Why



##### 포트폴리오 관리

- GitHub



## 2. Git Bash

##### GUI vs. CUI

1. GUI (Graphic User Interface) : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
2. CLI (Command Line Interface) : 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

> __Interface (인터페이스)__
>
> 인터페이스란 원래 서로 다른 개체끼리 맞닿아 있는 면
>
> 사용자와 컴퓨터가 서로 소통하는 접점



##### 경로

1. 절대 경로 : 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
   - `C:/Users/NewYorkKim/Desktop` : 윈도우 바탕 화면
2. 상대 경로 : 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
   - `./` : 현재 작업하고 있는 폴더
   - `../` : 현재 작업하고 있는 폴더의 상위 폴더



| 명령어              | 역할                                              |                  |
| :------------------ | :------------------------------------------------ | ---------------- |
| `mkdir <폴더 이름>` | 폴더 생성                                         | make directory   |
| `touch <파일 이름>` | 파일 생성                                         |                  |
| `cat <파일 이름>`   | 파일 내용 불러오기                                |                  |
| `cd <경로>`         | 경로 변경                                         | change directory |
| `ls`                | 현재 작업 중인 디렉토리의 폴더/파일 목록 불러오기 | list segments    |
| `-a`                | 옵션; 숨김 파일까지 모두 확인 가능                | all              |
| `-l`                | 옵션; 파일 정보를 자세히 확인 가능                | long             |
| `rm <폴더 이름>`    | 파일 제거                                         | remove           |
| `rm -r <파일 이름>` | 폴더 제거                                         | recursive        |



## 3. Vscode

##### 터미널

- 기본 터널 Git Bash로 변경



## 4. Markdown

| 문법                          | 역할           |
| ----------------------------- | -------------- |
| `#`                           | 제목 [1, 6]    |
| `- * +`                       | 순서 없는 목록 |
| `1. 2. 3.`                    | 순서 있는 목록 |
| `*글자*` `_글자_`             | *기울이기*     |
| `**글자**` `__글자__`         | **굵게**       |
| `~~글자~~`                    | ~~취소선~~     |
| ```code` ``                   | 인라인 코드    |
| ````code`                     | 블록 코드      |
| `---` `***` `___`             | 수평선         |
| `>`                           | 인용           |
| `![대체 텍스트](이미지 주소)` | 이미지 삽입    |
| `[텍스트](url)`               | 링크 삽입      |



## 5. Git & GitHub

##### 초기 설정

```bash
$ git config --global user.name <name>
$ git config --global user.email <email>

$ git config --global --list #설정 확인
```



##### 로컬 저장소

![로컬 저장소](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7142d992-3d01-481c-9d4e-e818c6e185d8%2FUntitled.png?table=block&id=62cab391-ee2f-48a6-95b6-834697312d0d&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2000&userId=&cache=v2)

- Working Directory (= Working Tree) : 사용자의 일반적인 작업이 일어나는 곳
- Staging Area (= Index) : 커밋을 위한 파일 및 폴더가 추가되는 곳
- Repository : Staging Area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 곳
- Git은 **Working Directory ➡ Staging Area ➡ Repository** 의 과정으로 버전 관리 수행



| 명령어                        | 역할                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| `git init`                    | 현재 작업 중인 디렉토리를 Git으로 관리                       |
| `git status`                  | Working Directory와 Staging Area에 있는 파일의 현재 상태     |
| `git add <파일 이름>`         | Working Directory에 있는 파일을 Staging Area로 올림          |
| `git commit -m "커밋 메시지"` | Staging Area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장 |
| `git log`                     | 커밋의 내역 조회                                             |
| `--oneline`                   | 옵션; 한 줄로 축약                                           |
| `-p`                          | 옵션; 파일의 변경 내용도 확인 가능                           |



##### 로컬 저장소와 원격 저장소 연결

- git remote
  - 원격 저장소 등록 : `git remote add <이름> <url>`
  - 원격 저장소 조회 : `git remote -v`
  - 원격 저장소 연결 삭제 : `git remte rm <이름>` `git remote remove <이름>`



##### 원격 저장소에 업로드

- git push

  - `git push <저장소 이름> <브랜치 이름>`

  - `git push -u origin master` : 두 번째 커밋부터 저장소 이름, 브랜치 이름 생략 가능



##### 원격 저장소 가져오기

- git clone
  - `git clone <원격 저장소 주소>`
  - `git init`과 `git remote add` 이미 수행
  
- git push
  - `git pull <저장소 이름> <브랜치 이름>`
  
  1. 다른 파일을 수정한 경우
  2. 같은 파일의 다른 라인을 수정한 경우
  3. 같은 파일의 같은 라인을 수정한 경우 ➡ **Conflict!**



##### 예전 버전으로 돌아가기

- git reset

  - `git reset [옵션] <커밋 ID>`
    - 돌아가려는 커밋으로 되돌아가고,

  1. `--soft` : 이후의 commit된 파일들을 **Staging Area**로 돌려놓음
  2. `--mixed` : 이후의 commit된 파일들을 **Working Directory**로 돌려놓음
  3. `--hard` : 이후의 commit된 파일들을 모두 Working Directory에서 **삭제**
     - 단, Untracked 파일은 Untracked로 남음
     - `git reflog` : 이미 삭제한 커밋으로 돌아가고 싶을 때 사용

- git revert
  - `git revert <커밋 ID>`
  - 이전 커밋을 취소한다는 새로운 커밋을 만듦



##### 브랜치

![branch](https://hphk.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd6378065-5864-4832-8122-0fde3eb4f6ec%2FUntitled.png?table=block&id=cce3230f-cede-4591-9225-ed375ed22a2e&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=930&userId=&cache=v2)

- 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 **독립적으로 작업**할 수 있도록 도와주는 Git의 도구

- git branch 

  | 명령어                               | 역할                             |
  | ------------------------------------ | -------------------------------- |
  | `git branch`                         | 브랜치 목록 확인                 |
  | `git branch -r`                      | 원격 저장소의 브랜치 목록 확인   |
  | `git branch <브랜치 이름>`           | 새로운 브랜치 생성               |
  | `git branch <브랜치 이름> <커밋 ID>` | 특정 커밋을 기준으로 브랜치 생성 |
  | `git branch -d <브랜치 이름>`        | 특정 브랜치 삭제                 |
  | `git branch -D <브랜치 이름>`        | 특정 브랜치 삭제; 강제 삭제      |

- git switch		

  - `git switch <다른 브랜치 이름>` : 다른 브랜치로 이동
  - `git switch -c <브랜치 이름>` : 브랜치를 새로 생성 + 이동
  - `git switch -c <브랜치 이름> <커밋 ID>` : 특정 커밋 기준으로 브랜치 생성 + 이동
  - 모든 Working Directory의 파일이 버전 관리가 되고 있는지 확인

- git merge

  - 분기된 브랜치들을 하나로 합치는 명령어
  - `git merge <합칠 브랜치 이름>`

  1. Fast-Forward
  2. 3-way Merge
  3. Merge Conflict



# 6. GitHub Pages

##### 템플릿 사이트

- [startbootstrap](https://startbootstrap.com/)
- [html5up](https://html5up.net/)



##### 웹사이트 배포

- GitHub ➡ Settings ➡ Pages
- 브랜치 선택 후 저장
- **.nojekyll** 파일 생성
- [About GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#static-site-generators)

