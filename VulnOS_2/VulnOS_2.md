# VulnOS: 2

------

<https://www.vulnhub.com/entry/vulnos-2,147/>

이번 문제는 회사 웹사이트를 침투해서 루트 권한을 따내는 것이 목적이다.

일단 nmap을 통해 ip를 알아냈다. 

![1](https://user-images.githubusercontent.com/51134298/61045443-d5d0a500-a415-11e9-9777-e1a5cc5ae77d.png)

~.104가 해당 머신의 ip이다. 

![2](https://user-images.githubusercontent.com/51134298/61045445-d5d0a500-a415-11e9-9af3-f0d351e370db.png)

포트를 확인해보았다. 22번 포트와 80번 포트가 열려있다. 일단 웹으로 접근해보았다.

![3](https://user-images.githubusercontent.com/51134298/61045446-d5d0a500-a415-11e9-9342-943282966f03.png)

사이트를 들어간 모습이다. 밑에 링크를 타고 들어가보았다. 

![4](https://user-images.githubusercontent.com/51134298/61045447-d6693b80-a415-11e9-9215-d83c936510f0.png)

해당 사이트의 주소는 http://<ip>/jabc/ 이다. 웹페이지를 여기저기 뒤져보았지만 별다른 것을 찾지 못해 헤메던 와중에 Documentation에 들어가니 아무런 말이 쓰여있지 않았다. 

![5](https://user-images.githubusercontent.com/51134298/61045424-d36e4b00-a415-11e9-855e-9bfe14294313.png)

드래그를 해보니 저런 말이 쓰여있었다. /jabcd0cs/ 에 방문하라고 한다.

![6](https://user-images.githubusercontent.com/51134298/61045425-d36e4b00-a415-11e9-9f07-f34e66d3f7e4.png)

바로 들어가보았다. OpenDocMan v1.2.7으로 만들어진 것 같다. 

![7](https://user-images.githubusercontent.com/51134298/61045427-d406e180-a415-11e9-87f2-05153569ae47.png)

searchsploit으로 opendocman 1.2.7을 검색해보았더니 하나가 나온다. 

내용을 보니 SQL Injection 취약점이 존재한다고 한다. 

예시로 들어준 주소는 "http://192.168.56.104/jabcd0cs/ajax_udf.php?q=1&add_value=odm_user%20UNION%20SELECT%201,version%28%29,3,4,5,6,7,8,9" 이다. 

![8](https://user-images.githubusercontent.com/51134298/61045428-d406e180-a415-11e9-9b26-0200d78479d8.png)

sqlmap을 통해 데이터베이스를 알아보기로 했다.

![9](https://user-images.githubusercontent.com/51134298/61045429-d406e180-a415-11e9-9195-c9b2d556f933.png)

결과는 이렇게 나왔다. 

![10](https://user-images.githubusercontent.com/51134298/61045430-d406e180-a415-11e9-8bd8-c5da46dcd400.png)

이번엔 jabcd0cs에 있는 테이블들을 알아보았다. 

![11](https://user-images.githubusercontent.com/51134298/61045431-d49f7800-a415-11e9-9238-e21facdd1ade.png)

결과는 이렇게 나왔다. odm_user에 user 정보들이 담겨있지 않을까해서 odm_user의 내용을 확인해보았다.

![12](https://user-images.githubusercontent.com/51134298/61045432-d49f7800-a415-11e9-8045-9407735d317a.png)

webmin의 password 해시값을 알 수 있다. sqlmap에서 사전공격으로 알아내려고 했지만 실패하여 다른 사이트를 통해 원래의 패스워드를 알아보았다. 

![13](https://user-images.githubusercontent.com/51134298/61045433-d49f7800-a415-11e9-8d61-b523984f42d1.png)

[http://www.md5decrypt.org](http://www.md5decrypt.org/) 이 사이트에서 복호화를 할 수 있었다.

webmin의 패스워드는 webmin1980 이었다. 같은 패스워드를 사용할 수 있으니 ssh로 로그인해보았다.

![14](https://user-images.githubusercontent.com/51134298/61045434-d49f7800-a415-11e9-9490-b3bf79c8017b.png)

운이 좋게도 성공했다. 이제 권한 상승을 할 차례이다. 

![15](https://user-images.githubusercontent.com/51134298/61045435-d5380e80-a415-11e9-8fd7-17b34d20729e.png)

일단 입력하기 편하게 터미널을 생성해주었다.

![16](https://user-images.githubusercontent.com/51134298/61045436-d5380e80-a415-11e9-8ca9-1990565c846f.png)

시스템 정보를 확인해보았다. Linux 3.13.0-24-generic 이라고 되어있다. 

![17](https://user-images.githubusercontent.com/51134298/61045439-d5380e80-a415-11e9-8516-663802069fcb.png)

검색 결과 몇개의 Exploit이 존재햇는데 두 번째 코드를 쓰기로 했다.

![18](https://user-images.githubusercontent.com/51134298/61045440-d5380e80-a415-11e9-938f-bbed8f28f95a.png)

코드를 컴파일한 후 실행시켰더니 금방 root 권한을 얻을 수 있었다.

![19](https://user-images.githubusercontent.com/51134298/61045442-d5d0a500-a415-11e9-8c7b-d094437cd043.png)

root 디렉토리로 가서 flag를 얻을 수 있었다. 