# Kioptrix: 2014 (#5)

------

ip부터 알아보았다.

![1](https://user-images.githubusercontent.com/51134298/62832601-f76ab980-bc6b-11e9-87df-9adecc3db1a8.png)

~.132가 ip이다. 

![2](https://user-images.githubusercontent.com/51134298/62832602-f76ab980-bc6b-11e9-943a-6f46ef5bf8bb.png)

포트를 보았다. 80번 포트와 8080번 포트가 열려있다.

![3](https://user-images.githubusercontent.com/51134298/62832603-f76ab980-bc6b-11e9-9d01-89340476106b.png)

웹으로 접속해보았다. 

사진과 같이 It works! 라고만 출력되고 아무것도 없다. 

주석에 URL=pChart2.1.3/index.php 라고 되어있다. 

![4](https://user-images.githubusercontent.com/51134298/62832604-f8035000-bc6b-11e9-95b5-318f06dcd061.png)

pChart는 차트나 그림을 만드는 데에 도움을 주는 PHP 라이브러리라고 한다. 

![5](https://user-images.githubusercontent.com/51134298/62832605-f8035000-bc6b-11e9-86a6-6f3820362b38.png)

취약점을 검색해보았다. 

![6](https://user-images.githubusercontent.com/51134298/62832606-f8035000-bc6b-11e9-85cf-04b667efc948.png)

읽고 따라해보니 passwd 파일을 읽을 수 있었다. 

이것과 같은 방식으로 httpd.conf도 읽어보았다.

![7](https://user-images.githubusercontent.com/51134298/62832591-f5a0f600-bc6b-11e9-9edd-a62f440deb33.png)

여기서 8080번 포트에 접속하려면 Mozilla4 브라우저여야만 한다는 것을 알 수 있었다.

![8](https://user-images.githubusercontent.com/51134298/62832592-f6398c80-bc6b-11e9-8f49-7a8654c9985e.png)

헤더를 설정하기 위해 H 옵션을 주었다. User Agent를 설정하고 보니 디렉토리가 나온다.

phptax로 이동할 수 있다.

![9](https://user-images.githubusercontent.com/51134298/62832593-f6398c80-bc6b-11e9-828f-656d18f4d2cf.png)

들어가보니 별거 없는 것 같다. 

![10](https://user-images.githubusercontent.com/51134298/62832594-f6398c80-bc6b-11e9-9395-e4f74086db23.png)

취약점을 검색해보았다.

랭크가 높은 모듈이 있기 때문에 바로 사용했다.

![11](https://user-images.githubusercontent.com/51134298/62832595-f6398c80-bc6b-11e9-9631-9d18b3db1d39.png)

실행을 시켜보았다.

![12](https://user-images.githubusercontent.com/51134298/62832596-f6d22300-bc6b-11e9-8842-058d0fe80c0f.png)

쉘을 얻을 수 있었다.

이제 root 권한을 얻으면 된다.

![13](https://user-images.githubusercontent.com/51134298/62832597-f6d22300-bc6b-11e9-8158-0bc80c2a755f.png)

시스템 정보를 확인해보았다. 

![14](https://user-images.githubusercontent.com/51134298/62832598-f6d22300-bc6b-11e9-8027-fe72e95c686e.png)

exploit-db에서 적당한 권한상승 익스플로잇을 찾았다.

![15](https://user-images.githubusercontent.com/51134298/62832599-f6d22300-bc6b-11e9-93d3-b7fec0d2b8f2.png)

컴파일을 하고 실행을 하니 바로 root를 얻었다.

![16](https://user-images.githubusercontent.com/51134298/62832600-f76ab980-bc6b-11e9-9cd6-d67996136b97.png)

root 디렉터리로 가니 congrats.txt가 있었다. 

이렇게 마무리했다.



