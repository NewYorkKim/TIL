Linux 기초

> 2022/05/27 ~ ing



## 0. 준비

- [생활코딩-블로그](https://opentutorials.org/module/2538/14160)
- [생활코딩-강의](https://youtu.be/DsG-JWrFJTc)
- `AWS Cloud9` 



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



## 3. IO Redirection

![image-20220606151114921]([생활코딩]Linux.assets/image-20220606151114921.png)

[Image Source](https://slideplayer.com/slide/5117573/)



- Standard Output `>` or `1>`![image-20220603223111754]([생활코딩]Linux.assets/image-20220603223111754.png)
- Standard Error `2>`![image-20220603223634702]([생활코딩]Linux.assets/image-20220603223634702.png)
- ![image-20220603223909100]([생활코딩]Linux.assets/image-20220603223909100.png)
- `/dev/null`	![image-20220603230008210]([생활코딩]Linux.assets/image-20220603230008210.png)



##### input

- `<`	![image-20220603224354270]([생활코딩]Linux.assets/image-20220603224354270.png)

- `head <옵션> <파일이름>`

  - Command-line Arguments

    ![image-20220603224732223]([생활코딩]Linux.assets/image-20220603224732223.png)

  - Standard Input ![image-20220603224845923]([생활코딩]Linux.assets/image-20220603224845923.png)

  - Redirection

    ![image-20220603225143301]([생활코딩]Linux.assets/image-20220603225143301-16542643495911.png)

    - IO Stream



##### append

- `>>`

  ![image-20220603225626031]([생활코딩]Linux.assets/image-20220603225626031.png)



## 4. Shell

##### bash vs. zsh

- 편의성에 따라 선택



##### Shell script

- 자동화

![image-20220605233817295]([생활코딩]Linux.assets/image-20220605233817295.png)

![image-20220605234027425]([생활코딩]Linux.assets/image-20220605234027425.png)

![image-20220605234205770]([생활코딩]Linux.assets/image-20220605234205770.png)



## Directory structure

![Linux File System Structure](https://static.thegeekstuff.com/wp-content/uploads/2010/11/filesystem-structure.png)



## Process

`ps`

- 프로세스 조회
- `ps aux`
- PID: 프로세스 ID ➡ `sudo kill <PID>`
- `top`, `htop`: 프로세스 관찰/열람



## File find

`locate <파일 이름>`

- 데이터베이스: mlocate
  - `sudo updatedb`



`find`

- 디렉토리

  - `find /`: root 디렉토리

  - `find .`: 현재 디렉토리

  - `find ~`: 홈 디렉토리

- Permission denied ➡ `sudo find`
- `-type`: 데이터 타입으로 검색
- `-name`: 데이터 이름으로 검색



`whereis`

- `$PATH`: 환경변수



## Background Execute

- `jobs`: 백그라운드 작업 목록 출력
- `fg`: 백그라운드에서 실행되고 있는 작업 ➡ 포어그라운드로 
- `<명령어> &`: 명령어 백그라운드에서 실행



## Daemon

1. `sudo yum install apache2`
2. `cd /etc/init.d/`: daemon 프로그램들이 위치하는 곳으로 이동
3. `sudo service apache2 start`: apache2의 명령어 중 start 실행
4. `ps aux | grep apahce2`: 현재 실행되는 프로세스 중 apache2을 포함하고 있는 경우만 화면에 출력

5. `sudo service apache2 stop`: apache2 실행 종료



![image-20220614170756544]([생활코딩]Linux.assets/image-20220614170756544.png)

- `rc3.d/`: 콘솔 방식으로 리눅스 구동할 경우 
- `rc5.d/`: GUI 방식으로 리눅스 구동할 경우



## Cron

- 정기적으로 작업 실행

- `crontab -e`

  ![Claus Ibsen (@davsclaus) riding the Apache Camel: Apache Camel 2.12 - Even  easier cron scheduled routes](http://2.bp.blogspot.com/--d9V7XzD9aU/UgzRLNXIgSI/AAAAAAAAAcM/cIzUHV665v0/s1600/cron.png)

  ​	![image-20220615134728209]([생활코딩]Linux.assets/image-20220615134728209.png)

  ![image-20220615135138805]([생활코딩]Linux.assets/image-20220615135138805.png)

  ![image-20220615140145864]([생활코딩]Linux.assets/image-20220615140145864.png)

  ![image-20220615135923409]([생활코딩]Linux.assets/image-20220615135923409.png)

  ![image-20220615140304451]([생활코딩]Linux.assets/image-20220615140304451.png)




## Multi user

- `id`: 내가 누구인지 확인

  ![image-20220620153924934]([생활코딩]Linux.assets/image-20220620153924934.png)

- `who`: 현재 시스템에 누가 접속해 있는지 확인



##### Root user

- super(root) user
  - 이름에 `root` 포함
  - `su - root`: super user로 전환
  - `~#` 
  - `exit`: 로그아웃
  - 몇몇 운영체제에서는 전환을 막아둠 ➡ `sudo passwd -u root`
  - 다시 막고 싶을 때 ➡ `sudo passwd -l root`
  - `/root`
- user
  - `sudo <명령어>`: 일시적으로 super user의 권한으로 명령어 실행 but 여전히 일반 user
  - `~$`
  - ⭐ 가급적이면 일반 user 상태를 유지하고 필요한 경우에는 `sudo` 사용
  - `home/user_name`



##### Add user

- `sudo useradd -m <user_name>`: <user_name>이라는 사용자 추가

  ![image-20220620155450151]([생활코딩]Linux.assets/image-20220620155450151.png)

- `sudo passwd <user_name>`: <user_name>이 사용할 비밀번호 설정

  ![image-20220620155713389]([생활코딩]Linux.assets/image-20220620155713389.png)

- `su - <user_name>`: <user_name>으로 사용자 전환

  ![image-20220620155811333]([생활코딩]Linux.assets/image-20220620155811333.png)

- `sudo usermod -a -G sudo <user_name>`: <user_name>에게 sudo를 사용할 수 있는 권한 부여



## Permission

- User ➡ File & Directory

- Read & Write & Excute

  - r, w, x

  

![image-20220625235205351]([생활코딩]Linux.assets/image-20220625235205351.png)

- type: -
- access mode: rw-rw-r--
  - owner: rw-
  - group: rw-
  - other: r--
- owner: ec2-user
- group: ec2-user



- `chmod`: 권한 변경 (change mode)

  ![image-20220625235238498]([생활코딩]Linux.assets/image-20220625235238498.png)

  - excute

  ![image-20220625235808075]([생활코딩]Linux.assets/image-20220625235808075.png)

  ![image-20220625235954136]([생활코딩]Linux.assets/image-20220625235954136.png)

  ![image-20220626000036035]([생활코딩]Linux.assets/image-20220626000036035.png)

  ![image-20220626000205302]([생활코딩]Linux.assets/image-20220626000205302.png)
  
  - directory
  
  ![image-20220701174103514]([생활코딩]Linux.assets/image-20220701174103514.png)![image-20220701174233469]([생활코딩]Linux.assets/image-20220701174233469.png)![image-20220701174302420]([생활코딩]Linux.assets/image-20220701174302420.png)![image-20220701174340209]([생활코딩]Linux.assets/image-20220701174340209.png)
  
  ![image-20220701174539000]([생활코딩]Linux.assets/image-20220701174539000.png)
  
  - Octal modes
  
    ![image-20220701175242832]([생활코딩]Linux.assets/image-20220701175242832.png)![image-20220701175454766]([생활코딩]Linux.assets/image-20220701175454766.png)
  
  - 레퍼런스![image-20220701175717872]([생활코딩]Linux.assets/image-20220701175717872.png)
  - 연산자![image-20220701175748632]([생활코딩]Linux.assets/image-20220701175748632.png)
