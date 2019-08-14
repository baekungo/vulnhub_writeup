# HackLAB: Vulnix

------

루트 권한을 따내는 것이 목표이다.

![1](https://user-images.githubusercontent.com/51134298/63017002-0ea9e100-bed0-11e9-8084-b6b6dfca2534.png)

ip 부터 찾아보았다. ~130이 이번 머신의 ip이다.

![2](https://user-images.githubusercontent.com/51134298/63017003-0f427780-bed0-11e9-86d9-30d74f8d26f5.png)

여러 개의 포트를 찾았다. 

하나하나씩 취약점을 찾아보면 될 것 같다. 

![3](https://user-images.githubusercontent.com/51134298/63017004-0f427780-bed0-11e9-929d-7ae0856e24d0.png)

22번 포트부터 시작해보았다. 

OpenSSH 버전의 취약점은 따로 없고 다른 포트부터 봐야할 것 같다.

25번 포트는 무엇때문인지 아직 잘 모르겠지만 연결이 되지 않아 잠시 넘어가도록 했다.

![4](https://user-images.githubusercontent.com/51134298/63017005-0f427780-bed0-11e9-8d12-101cedc53534.png)

다음은 79번 포트이다. 

![5](https://user-images.githubusercontent.com/51134298/63017006-0f427780-bed0-11e9-9314-4114e88954ef.png)

적당한 모듈을 찾아 사용했다. 이 모듈을 사용하면 user 목록을 받아낼 수 있을 것이다.

![6](https://user-images.githubusercontent.com/51134298/63017001-0ea9e100-bed0-11e9-8474-ba8e328c7d79.png)

위와 같이 결과가 나왔다. 











