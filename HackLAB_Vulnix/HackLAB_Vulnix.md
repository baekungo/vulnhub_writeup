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

![7](https://user-images.githubusercontent.com/51134298/63092952-61ea6500-bf9e-11e9-8c14-91c99750c727.png)

얻은 유저 정보로 패스워드를 무작위 대입해보았다. 

![8](https://user-images.githubusercontent.com/51134298/63092953-61ea6500-bf9e-11e9-8c65-3b6d2028ca2a.png)

운이 좋게도 user의 패스워드를 알 수 있었다.

![9](https://user-images.githubusercontent.com/51134298/63092954-61ea6500-bf9e-11e9-826e-a890e5cedc70.png)

user로 접속한 모습이다.

user로 접속한 뒤 힌트가 될만한 것을 찾아보았지만 딱히 없었다.

![10](https://user-images.githubusercontent.com/51134298/63092955-61ea6500-bf9e-11e9-85b4-a8833a60d2d3.png)

모든 사용자 목록을 보았다. vulnix 라는 아이디를 가진 사용자가 있다.

이 아이디로 접속을 해야 무언가가 있을 것 같다.

다시 포트를 보았다.

![11](https://user-images.githubusercontent.com/51134298/63092948-6151ce80-bf9e-11e9-96cd-113c59eeba7e.png)

여기에 nfs 서비스가 존재한다. 

(nfs: 서버 리소스를 클라이언트에서 자신의 리소스를 사용하는 것처럼 만들어주는 서비스)

![12](https://user-images.githubusercontent.com/51134298/63092949-6151ce80-bf9e-11e9-8e5f-a23c0ea8e42d.png)

(옵션 -e : Show the NFS server's export list.)

nfs 서버에 vulnix라는 디렉토리가 공유되고 있다. 

![13](https://user-images.githubusercontent.com/51134298/63092950-6151ce80-bf9e-11e9-9bc5-2d40f72a6846.png)

마운트를 하고 접근해보려 했지만 불가능했다. 

root-squash 때문에 root로 접근하지 못했다. 

(root-squash : root 자격으로 파일시스템 접근 시 anonymous uid/gid로 바꿔서 허가)

아까 확인했던 vulnix의 uid와 gid로 계정을 생성해야한다.

![14](https://user-images.githubusercontent.com/51134298/63092951-6151ce80-bf9e-11e9-813a-2b49e0a106d3.png)

vulnix 계정을 만들었다. ID는 머신과 동일하게 2008로 설정했다.





~~잠시 문제가 있어서 중단하고 다음에 할 예정~~







