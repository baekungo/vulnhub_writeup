# SkyTower: 1

------

![1](https://user-images.githubusercontent.com/51134298/63175173-70a84900-c07e-11e9-933c-394458f8abe5.png)

포트 스캐닝을 했다. ssh는 필터가 되어있다. 

일단 80번 포트가 열려있으니 웹으로 들어가보았다.

![2](https://user-images.githubusercontent.com/51134298/63175176-71d97600-c07e-11e9-9f89-dc622a9c3a11.png)

로그인 화면이 나온다. 다른 특별한 것은 없어보인다.

![3](https://user-images.githubusercontent.com/51134298/63175177-72720c80-c07e-11e9-83e4-21e57164dc15.png)

웹 취약점을 스캔해보았다. 

별다른 것은 보이지 않는다.

로그인 화면이 있으니 SQL Injection을 시도해보고 싶어졌다.

![4](https://user-images.githubusercontent.com/51134298/63175178-72720c80-c07e-11e9-9d60-870da60072f1.png)

가장 기본적인 것을 넣어보았다. 

![5](https://user-images.githubusercontent.com/51134298/63175179-72720c80-c07e-11e9-8a9d-3b02f6b0a45c.png)

위와 같은 에러메시지를 돌려준다. 

아마 나름의 방어를 해놓은 것 같다. 여러가지 시도를 해보았다.

![6](https://user-images.githubusercontent.com/51134298/63175180-730aa300-c07e-11e9-999e-bacb796fa6a5.png)

그렇게하다가 or를 ||로 바꾸어보고 주석도 --를 #으로 바꾸어봤더니 성공했다.

![7](https://user-images.githubusercontent.com/51134298/63175181-730aa300-c07e-11e9-8253-5c0ce876b6ee.png)

사용자 아이디와 패스워드가 보인다.

![8](https://user-images.githubusercontent.com/51134298/63175182-730aa300-c07e-11e9-9b56-ce9113985765.png)

SSH로 로그인해보았다. 생각해보니 필터링되어있다. 

그럼 이제 아까 본 3128번 포트 프록시를 이용해야겠다.

![9](https://user-images.githubusercontent.com/51134298/63251013-d4618a80-c2a7-11e9-8a20-a36bac594194.png)

프록시터널을 이용하였다. 

![10](https://user-images.githubusercontent.com/51134298/63251015-d4fa2100-c2a7-11e9-9107-b32aa12f91b7.png)

로그인을 할 수 있었지만 바로 종료가 되버린다. 

그래서 설정을 다시 해주었다.

![11](https://user-images.githubusercontent.com/51134298/63251016-d4fa2100-c2a7-11e9-89f7-d42bcdc1a09c.png)

로그인에 성공했다.

![12](https://user-images.githubusercontent.com/51134298/63251017-d4fa2100-c2a7-11e9-80e2-35165da5cf29.png)

/var/www 디렉터리에 있는 login.php 파일이다.

여기를 보면 DB의 id와 pw가 나와있다. 

![13](https://user-images.githubusercontent.com/51134298/63251004-d3c8f400-c2a7-11e9-9fd8-2ae23b4e3ff9.png)

mysql DB에 로그인해보았다. SkyTech DB로 들어갔다.

![14](https://user-images.githubusercontent.com/51134298/63251005-d3c8f400-c2a7-11e9-888f-144901ee3e37.png)

login 이란 테이블이 있었고 그 내용을 보았더니 아이디와 패스워드 목록이 있다. 

![15](https://user-images.githubusercontent.com/51134298/63251007-d3c8f400-c2a7-11e9-89cd-51965a635e42.png)

sara의 id로 로그인해보았다.

![16](https://user-images.githubusercontent.com/51134298/63251009-d4618a80-c2a7-11e9-8583-bdfbe8d4b0e3.png)

sudo 권한을 보았다.

cat 명령어와 ls 명령어로 /accounts/* 를 볼 수 있는 것 같다.

그런데 accounts 디렉터리는 비어있었다.

하지만 root 디렉터리의 내용을 보는 방법은 있었다. 

![17](https://user-images.githubusercontent.com/51134298/63251012-d4618a80-c2a7-11e9-94b6-2bf50a1fb41f.png)

이렇게 root에 있는 flag를 읽을 수 있었다.







