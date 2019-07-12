# SickOs: 1.2

------

<https://www.vulnhub.com/entry/sickos-12,144/>

해당 머신의 root 권한을 얻으면 되는 문제이다.

![1](https://user-images.githubusercontent.com/51134298/61096223-c2fbb600-a491-11e9-9dff-7359f7ed6995.png)

ip를 알아보았다. ~.128이 머신의 ip인 것을 알 수 있었다.

![2](https://user-images.githubusercontent.com/51134298/61096224-c3944c80-a491-11e9-8277-3f4ad17b48ee.png)

열린 포트를 확인해보니 22번 포트와 80번 포트가 열려있다. 

일단 웹페이지를 접속해보았다. 

![3](https://user-images.githubusercontent.com/51134298/61096225-c3944c80-a491-11e9-8a97-9f2d8ebf6de5.png)

아무것도 없었다.

![4](https://user-images.githubusercontent.com/51134298/61096226-c3944c80-a491-11e9-8278-0cb085c6d3b4.png)

nikto를 사용해서 조사해보았다. lighttpd 1.4.28 서버를 사용하고 있다.

![5](https://user-images.githubusercontent.com/51134298/61096228-c3944c80-a491-11e9-9a5f-55ddc8a30085.png)

dirb를 사용해보았다. test라는 디렉토리가 발견되었다. 

![6](https://user-images.githubusercontent.com/51134298/61096229-c42ce300-a491-11e9-9533-f33191419e3f.png)

디렉토리에는 아무것도 없었다. 

여기서 lighttpd 버전의 취약점을 찾아보려 했지만 실패했고 이리저리 헤맸다.

검색을 해서 도움을 받고 HTTP Method를 점검해보았다.

![7](https://user-images.githubusercontent.com/51134298/61096230-c42ce300-a491-11e9-8aad-eb307e92e497.png)

curl -v -X OPTIONS url : 서버가 허용하는 HTTP Method 목록 확인

여기서 결과를 보니 PUT 메소드가 Allow 되어있다. 이는 곧 파일을 업로드시킬 수 있다는 말이기도 하다.

![8](https://user-images.githubusercontent.com/51134298/61096231-c42ce300-a491-11e9-976d-91c6253339df.png)

msfvenom을 사용해 리버스쉘을 만드는 파일을 생성했고 이를 업로드하려 했으나 실패했다.

 검색을 해보니 전송할 콘텐츠의 크기가 커서 그렇다고 한다. 

-H "Expect:" 를 추가해 Expect 헤더를 비워주어서 보낸다. 

![9](https://user-images.githubusercontent.com/51134298/61096232-c42ce300-a491-11e9-80b2-1cb87c29d414.png)

파일이 올라갔다. 이제 핸들러를 설정한 후 파일을 클릭하기만 하면 된다.

![10](https://user-images.githubusercontent.com/51134298/61096233-c4c57980-a491-11e9-9639-474b13e3eafa.png)

안된다..  4444번 포트로 연결을 시도했지만 되지 않았다. 

검색을 해보았더니 방화벽에 의해 막혀있을 것(?)이라는 글을 보았다. 그래서 443번 포트로 바꿔서 실행했다.

![11](https://user-images.githubusercontent.com/51134298/61096234-c4c57980-a491-11e9-9548-3d53e2dcb417.png)

shell을 얻었다. 이제 권한 상승을 시도해야한다. 

![12](https://user-images.githubusercontent.com/51134298/61096235-c4c57980-a491-11e9-97f0-f41b791cd347.png)

cron.daily 라는 디렉토리에 chkrootkit 이라는 파일이 존재한다.

chkrootkit은 루트킷을 탐지하는 파일인데, 일부 버전에 취약점이 존재한다.

![13](https://user-images.githubusercontent.com/51134298/61096216-c2631f80-a491-11e9-88b8-4dcc1c5be21a.png)

현재 버전은 0.49 라고 되어있다.

![14](https://user-images.githubusercontent.com/51134298/61096217-c2631f80-a491-11e9-904f-489778bb17d8.png)

0.49버전은 로컬에서 권한 상승을 할 수 있는 취약점이 존재하는 버전이다.

![15](https://user-images.githubusercontent.com/51134298/61096218-c2631f80-a491-11e9-8d8d-ad50c6fe6a96.png)

해당 취약점에 대한 설명이다. /tmp 디렉토리에 update라는 파일을 만들어 원하는 명령어를 집어넣으면 된다.

sudoers 파일에 현재 id를 넣는 방법도 있고, netcat으로 root로 접속하는 방법 등 여러가지가 있다.

![16](https://user-images.githubusercontent.com/51134298/61096219-c2fbb600-a491-11e9-9a40-b25b5fb9e997.png)

현재 id에 sudo 권한을 부여했다. 몇 초가 지난 후에 sudo su 명령이 패스워드 없이 실행된다. ㅊㅇ 

![17](https://user-images.githubusercontent.com/51134298/61096221-c2fbb600-a491-11e9-9346-4f0ef12313d5.png)

root 권한을 얻을 수 있다. 

![18](https://user-images.githubusercontent.com/51134298/61096222-c2fbb600-a491-11e9-9b39-c84154c645ab.png)



### (추가)

![19](https://user-images.githubusercontent.com/51134298/61096464-a1e79500-a492-11e9-8bd5-6c55a34dc70e.png)

newRule 이라는 파일도 있었는데 여기에 아까 4444번 포트가 안된 이유가 있다. 

iptables에 패킷필터링을 해놓았다. 