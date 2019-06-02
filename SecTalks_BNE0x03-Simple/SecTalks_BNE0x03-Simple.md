# SecTalks_BNE0x03-Simple

------

<https://www.vulnhub.com/entry/sectalks-bne0x03-simple,141/>

이번에 풀어 볼 문제이다.

문제 설명에는 웹 기반 해킹의 기본에 중점을 둔 CTF라고 나온다.

![1559407750641](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559407750641.png)

nmap의 -sn 옵션은 Ping Scan 용도이다. 호스트를 찾을 수 있다. 

여기서 ~.104 가 문제 시스템의 주소이다. 

![1559407896713](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559407896713.png)

nmap의 -sV 옵션은 열린 포트를 보여준다. 이를 통해 서비스, 버전 정보를 확인할 수 있다.

여기서는 웹 서버가 실행되고 있는 것을 알 수 있다.

![1559408177824](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559408177824.png)

웹 사이트에 접속해보았다. 

로그인 창과 "CuteNews v.2.0.3"를 볼 수 있다. 

![1559410190908](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559410190908.png)

exploit-db에 검색 결과 "Arbitary File Upload"라는 제목의 취약점이 존재한다. 

```txt
 1 - Sign up for New User
 2 - Log In 
 3 - Go to Personal options http://www.target.com/cutenews/index.php?mod=main&opt=personal
 4 - Select Upload Avatar Example: Evil.jpg
 5 - use tamper data  & Rename File Evil.jpg to Evil.php
```

방법은 위와 같다.

![1559481767054](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559481767054.png)

php 리버스 쉘코드를 만들기 위해 msfvenom을 이용하였다.

회원가입을 하고 로그인을 한 후 Personal options 창으로 이동한다. (1~3)

![1559482079559](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559482079559.png)

Avatar 파일 선택을 해서 php 쉘코드를 jpg로 확장자를 변경해준 후 파일을 올린다. (4)

![1559482302670](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559482302670.png)

Burp Suite를 실행해 Avatar 변경 요청을 인터셉트해 확장자를 다시 php로 바꿔준다. (5)

![1559482721415](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559482721415.png)

Exploit을 설정해주기 위해 metasploit 콘솔 창을 열어준다. 

핸들러를 사용하기 위해 payload를 설정해주고 option을 모두 설정한다. 

http://192.168.56.104/uploads/avatar_test_Evil.php 로 접속한다 (shell이 있는 주소)

![1559483138174](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559483138174.png)

세션이 연결되고, 명령을 할 수 있는 상태가 된다.

![1559483295675](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559483295675.png)

현재 id를 확인해보니 www-data 로 되어있다.

![1559483721048](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559483721048.png)

sudo 명령어를 이용해 root 의 디렉토리로 가서 flag를 볼 수 있다.

![1559483807917](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1559483807917.png)



