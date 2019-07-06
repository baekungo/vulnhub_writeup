# Stapler: 1

------

<https://www.vulnhub.com/entry/stapler-1,150/>

이번 machine은 여러가지 방법으로 root 권한을 얻어낼 수 있다고한다.

제한된 쉘을 얻는 방법은 최소 2가지, root 권한을 얻는 방법은 최소 3가지라고 설명되어있다.

최대한 많은 방법을 찾아내는 쪽으로 진행해보았다.

![1](https://user-images.githubusercontent.com/51134298/60754746-bf46da00-a020-11e9-9aa8-61281152caa5.png)

일단 ip를 찾아보았다. ~110이 ip라는 것을 알 수 있다.

![2](https://user-images.githubusercontent.com/51134298/60754747-bf46da00-a020-11e9-9bcb-e1a073760787.png)

포트를 검색해보았다. ftp, ssh 서비스를 제공하고 있고 웹 서비스도 있다. 139번 포트에는 Samba 서비스가 있다. 

666번 포트는 doom? 이라고 되어있다. 검색을 해보니 id 소프트웨어의 둠 멀티플레이어 게임이라고 하는데 뭔지는 잘 모르겠다. 

12380 포트에는 웹이 있다. 일단 시도해볼 것이 많으니 차례대로 해본다.

![3](https://user-images.githubusercontent.com/51134298/60754748-bf46da00-a020-11e9-9674-88033237ae15.png)

일단 ftp를 접속해보았다. 배너에는 Harry에게 말을 하는 문구가 있다. 그리고 로그인을 해야하는데 Id와 Password를 모르니 접속할 수가 없었다. 그래서 Anonymous FTP를 사용할 수 있는지 확인해보았고 접속할 수 있었다. 

안에는 note라는 파일이 있었고 이를 칼리로 가져와 읽어보았다. 이번에는 Elly와 John이라는 이름을 볼 수 있다.

이대로 넘어가려고 했지만 이름들이 나오는 것을 보아 Id가 될 수도 있다고 생각했다.

![4](https://user-images.githubusercontent.com/51134298/60754749-bf46da00-a020-11e9-85f8-8a35df73b858.png)

hydra를 이용해 사전 공격을 했다. Id 파일로 사용한 names에는 아까 확인했던 이름들인 elly, john, harry를 넣어놨다. -e snr 옵션(n:null/s:try login as pass/r:reversed)을 주었다. 

결국 Id: elly / Pw: ylle 를 찾아내었고 로그인해서 파일을 보았더니 수많은 파일이 있었다. 

![5](https://user-images.githubusercontent.com/51134298/60754750-bf46da00-a020-11e9-91c7-d8b55b9c4145.png)

그 중에 passwd 라는 파일이 있었고 이를 통해 사용자 목록을 볼 수 있었다. 

![6](https://user-images.githubusercontent.com/51134298/60754752-bfdf7080-a020-11e9-8b07-fc838858136f.png)

cut 명령어를 통해 이름만 남기고 저장했다. (옵션 -d: 해당 구분자를 기준으로 잘라내기, -f:  잘라낼 필드 지정)

그럼 Id를 얻었으니 역시 또 한번 사전 공격을 실행해볼만 하다.

![7](https://user-images.githubusercontent.com/51134298/60754753-bfdf7080-a020-11e9-9dff-986940047b8e.png)

다행히 찾았다. Id와 Pw 모두 SHayslett 이다. 

![8](https://user-images.githubusercontent.com/51134298/60754754-bfdf7080-a020-11e9-8240-101e41135ec4.png)

이렇게 SHayslett으로 접속할 수 있다. 

여기까지 제한된 쉘을 얻은 1가지 방법을 했다. 나머지 방법까지 하면 너무 길어질 것 같아 다른 글에서 진행하도록 하고 이 글에선 이어서 루트 권한을 얻는 것 까지 시도하려고 한다.

![9](https://user-images.githubusercontent.com/51134298/60754755-bfdf7080-a020-11e9-8b9e-745d36d228a1.png)

해당 머신의 운영체제 정보를 본다. 리눅스 4.4.0-21 ~~ 이다. 

![10](https://user-images.githubusercontent.com/51134298/60754756-c0780700-a020-11e9-9bf1-ed3433ac406d.png)

칼리에서 searchsploit으로 익스플로잇을 찾아보았다. 몇개를 시도해보았는데 왠지 모르게 안되는 것들도 있어서 결국에는 밑에서 네 번째인 39772로 시도하기로 했다. 

![11](https://user-images.githubusercontent.com/51134298/60754757-c0780700-a020-11e9-85a5-4167cf770c79.png)

칼리에서 파일을 받아놓은 후 scp를 사용해 machine으로 디렉토리를 옮겨준다. (-r : 디렉토리 복사)

![12](https://user-images.githubusercontent.com/51134298/60754758-c0780700-a020-11e9-84c8-9f3952a9d856.png)

exploit-db를 보면 사용법이 나와있다. 

![13](https://user-images.githubusercontent.com/51134298/60754759-c0780700-a020-11e9-958e-2219a69b66f5.png)

사용법 대로 compile.sh을 실행한 후 doubleput을 실행하면 조금 뒤 root 권한을 얻게된다.

해당 익스플로잇이 어떤 과정을 거쳐 root 권한을 얻는지는 따로 공부해보도록 할 예정이다.

![14](https://user-images.githubusercontent.com/51134298/60754760-c1109d80-a020-11e9-8329-c13b56c039d8.png)

최종적으로 root 디렉토리 내의 flag를 얻을 수 있다. 

다른 방법으로 푸는 것은 글을 따로 작성할 예정이다. 









