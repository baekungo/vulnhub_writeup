# HackLAB: Vulnix

------

루트 권한을 따내는 것이 목표이다.

![1565621625063](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1565621625063.png)

ip 부터 찾아보았다. ~130이 이번 머신의 ip이다.

![1565706253810](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1565706253810.png)

여러 개의 포트를 찾았다. 

하나하나씩 취약점을 찾아보면 될 것 같다. 

![1565706304201](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1565706304201.png)

22번 포트부터 시작해보았다. 

OpenSSH 버전의 취약점은 따로 없고 다른 포트부터 봐야할 것 같다.

![1565707097084](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1565707097084.png)

25번 포트가 열려있다. 

smtp-user-enum 프로그램을 사용해보았다.













