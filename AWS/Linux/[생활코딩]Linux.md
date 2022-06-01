# \Linux 기초

> 2022/05/27 ~ ing



## 0. 준비

- [생활코딩-블로그](https://opentutorials.org/module/2538/14160)
- [생활코딩-강의](https://youtu.be/DsG-JWrFJTc)
- `AWS Cloud9` 이용



## 1. 기초

| 명령어              | 역할                                                         |                         |
| ------------------- | ------------------------------------------------------------ | ----------------------- |
| `ls`                | 현재 작업 중인 디렉토리의 폴더/파일 목록 불러오기            | list segments           |
| `-a`                | 옵션; 숨김 파일까지 모두 확인 가능                           | all                     |
| `-l`                | 옵션; 파일 정보를 자세히 확인 가능                           | long                    |
| `-S`                | 옵션; 파일 크기별로 정렬 (내림차순)                          | sort                    |
| `pwd`               | 현재 작업 중인 디렉토리 표시                                 | print working directory |
| `mkdir <폴더 이름>` | 폴더 생성                                                    | make directory          |
| `touch <파일 이름>` | 파일 생성                                                    |                         |
| `cd <경로>`         | 경로 변경                                                    | change directory        |
| `clear`             | 터미널 화면 지우기<br />스크롤바를 올리면 이전 내용 확인 가능 |                         |
| `rm <파일 이름`     | 파일 삭제                                                    | remove                  |
| `rm -r <폴더 이름>` | 폴더 삭제                                                    | recursive               |
| `<명령어> --help`   | 명령어 사용 방법 확인 (1)                                    |                         |
| `man <명령어>`      | 명령어 사용 방법 확인 (2)<br />전용 페이지로 이동            | manual                  |
| `sudo <명령어>`     | root 권한을 빌려 명령 실행                                   | super user do           |



##### nano

![image-20220528211409701]([생활코딩]Linux.assets/image-20220528211409701.png)

![image-20220528211802578]([생활코딩]Linux.assets/image-20220528211802578.png)

![image-20220529190439159]([생활코딩]Linux.assets/image-20220529190439159.png)



##### Package manager

- `apt`
  - `sudo apt-get update`: 최신 소프트웨어 목록 업데이트
  - `sudo apt-get upgrade`: 설치된 소프트웨어를 최신 버전으로 업그레이드
  - `sudo apt-cache search <프로그램 이름>`: 관련 프로그램 검색
  - `sudo apt-get install <프로그램 이름>`: 프로그램 설치
  - `sudo apt-get upgrade <프로그램 이름>`: 프로그램 업그레이드
  - `sudo apt-get remove <프로그램 이름>`: 프로그램 삭제
- `yum`: On Amazaon Linux use `yum` instead of `apt-get`
  - `sudo yum update`
  - `sudo yum upgrade`
  - `sudo yum search <프로그램 이름>`
  - `sudo yum install <프로그램 이름>`
  - `sudo yum upgrade <프로그램 이름>`
  - `sudo yum remove <프로그램 이름>`



##### wget & git

- `wget <옵션> <URL>`
  - `wget <URL>`
  - `wget -O <파일 이름> <URL>`
- git
  - `sudo yum install git`: git 설치
  - `git clone <URL> <DIR>`: 해당 디렉토리에 Git 저장소 복제



##### Sequence execution 

- semicolon `;`

  ![image-20220601233621513]([생활코딩]Linux.assets/image-20220601233621513.png)



##### pipeline

- `grep`

  - `grep <옵션 > <검색어> <파일 이름>`

    ![image-20220601234903298]([생활코딩]Linux.assets/image-20220601234903298.png)

- pipeline `|`

  ![image-20220601235218328]([생활코딩]Linux.assets/image-20220601235218328.png)

  

  ![image-20220601235402621]([생활코딩]Linux.assets/image-20220601235402621.png)

