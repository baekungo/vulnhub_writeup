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













