# Stapler: 1 (2)

------

<https://www.vulnhub.com/entry/stapler-1,150/>

이번엔 다른 방법으로 쉘을 얻어보도록 할 것이다. 

nmap으로 포트를 확인한 것 까지는 전과 동일하다. 

![1](https://user-images.githubusercontent.com/51134298/60766561-5a55b780-a0e6-11e9-8d3c-d3aa340853ef.png)

처음에는 ftp를 통해 유저들의 정보를 알아내고 쉘을 얻었으니 이번에는 다른 포트를 활용해보았다.

80번 포트에 웹이 있으니 접속을 시도해보았다. 하지만 접속이 안되었다. nikto를 사용해 스캔해보았지만 아무것도 찾을 수 없었다.

다음으로 넘어가서 139번 포트가 있다. netbios-ssn이 서비스 중이라고 되어있다. 그래서 공유자원이 있는지 알아보도록 했다. 

![2](https://user-images.githubusercontent.com/51134298/60766562-5aee4e00-a0e6-11e9-9b7e-9ed72789ba97.png)

위와 같이 나왔다. kathy와 tmp라는 이름으로 공유되고 있는 공유 폴더가 존재한다. 

![3](https://user-images.githubusercontent.com/51134298/60766563-5aee4e00-a0e6-11e9-9144-0467b8e62ddc.png)

접속을 했더니 안에 몇몇 파일이 존재했다. 일단 그냥 다 가져왔다.

![4](https://user-images.githubusercontent.com/51134298/60766564-5aee4e00-a0e6-11e9-98de-40956774972d.png)

todo-list라는 텍스트 파일에는 저 문구가 쓰여있었고, 압축이 되어있는 wordpress 파일의 압축을 푸니 위와 같은 파일들이 있었다. 



### (잠시 다른 방법)

메타스플로잇을 통해 Samba의 취약점을  공격하는 방법도 있다.

![5](https://user-images.githubusercontent.com/51134298/60766565-5aee4e00-a0e6-11e9-8279-64aca15ce57b.png)

Samba를 검색하니 Linux Samba 익스플로잇이 나온다. 그 중 랭크가 가장 높은 is_known_pipename을 사용한다.

![6](https://user-images.githubusercontent.com/51134298/60766566-5b86e480-a0e6-11e9-9b24-d05e8a6c23d6.png)

바로 root 쉘을 얻을 수 있다. 여기에 쓰인 익스플로잇 코드도 다음에 공부해보도록 하고 일단 넘어가겠다.

(다시 돌아와서)

워드프레스가 있는 것을 보아 웹으로 접근하는 것도 좋을 것 같다. 하지만 그 전에 666포트가 거슬리기 때문에 해결하고 가기로 했다.

![7](https://user-images.githubusercontent.com/51134298/60766542-57f35d80-a0e6-11e9-8309-55bce63c391d.png)

마구 깨진 글자들이 나온다. message2.jpg 라는 글자는 보인다. 파일 이름이 드러난 것 같고 이는 압축된 파일이라는 것을 유추해볼 수 있다. 

![8](https://user-images.githubusercontent.com/51134298/60766543-57f35d80-a0e6-11e9-8ab2-e026e1f4416c.png)

그대로 test.zip 이라는 파일에 담고 unzip을 한 후 이미지를 보았다. segmentation fault가 있는 것을 보아 버퍼 오버플로우에 관련된 것인가 싶었지만 그 다음에 어떻게 해야할지는 몰라서 넘어갔다.

![9](https://user-images.githubusercontent.com/51134298/60766544-57f35d80-a0e6-11e9-95db-f33109de86f2.png)

이것은 message2.jpg의 내용을 본 것이다. 이걸 읽고 있다면 cookie를 얻을 것이라고 한다. ???

웹으로 넘어간다. 

80번 포트로는 접근이 안됐기 때문에 12380포트로 시도해보았다. 

![10](https://user-images.githubusercontent.com/51134298/60766546-588bf400-a0e6-11e9-8c74-4121ef49baf3.png)

이런 화면만 나온다. 

![11](https://user-images.githubusercontent.com/51134298/60766547-588bf400-a0e6-11e9-9d5b-08fa2e3f8362.png)

Nikto를 사용해 스캔해보았더니 robots.txt 로 들어갈 수 있고 그 안에는 admin112233, blogblog 디렉토리가 존재한다. 그리고 이 사이트는 SSL을 사용한다고 하니 https로 접근해야할 것 같다.

![12](https://user-images.githubusercontent.com/51134298/60766548-588bf400-a0e6-11e9-85c2-157a9b4721be.png)

blogblog에 들어가보니 워드프레스로 만들어졌다는 것을 알 수 있었다. 

wp-content/plugins 디렉토리를 들어가보니 접근이 가능했다.

![13](https://user-images.githubusercontent.com/51134298/60766549-588bf400-a0e6-11e9-937b-db7fd7b195c5.png)

플러그인들 중에서 취약점이 있는 것을 살펴보니 advanced-video ~ 플러그인에 취약점이 있는 것을 알았다.

<https://www.exploit-db.com/exploits/39646>

이를 통해 여러가지 시도를 할 수 있을 것 같다. 일단 wp-config.php를 얻어 내용을 보았다.

https://192.168.56.110:12380/blogblog/wp-admin/admin-ajax.php?action=ave_publishPost&title=random&short=1&term=1&thumb=../wp-config.php

이렇게 하면 wp-config.php를 https://192.168.56.110:12380/blogblog/wp-content/uploads/ 에 넣을 수 있다. 

![14](https://user-images.githubusercontent.com/51134298/60766550-59248a80-a0e6-11e9-87cf-967e75131820.png)

해당 파일을 다운받았고 내용을 확인해보았다.

![15](https://user-images.githubusercontent.com/51134298/60766551-59248a80-a0e6-11e9-825d-9bc13819df71.png)

패스워드가 plbkac 이라고 한다. mysql로 접속해본다.

![16](https://user-images.githubusercontent.com/51134298/60766552-59248a80-a0e6-11e9-90ff-8e8dd1e2a619.png)

wordpress 데이터베이스에 wp_users 라는 테이블이 있다.

![17](https://user-images.githubusercontent.com/51134298/60766553-59248a80-a0e6-11e9-88e1-59c46cab7159.png)

이 안에 이름과 패스워드들이 나와있다. 

![18](https://user-images.githubusercontent.com/51134298/60766554-59bd2100-a0e6-11e9-8f32-90b68d57450b.png)

john을 사용해 패스워드들을 알아보았다. 이 정보를 갖고 John의 아이디로 로그인해보았다.

![19](https://user-images.githubusercontent.com/51134298/60766555-59bd2100-a0e6-11e9-99d8-5ae42eeccf24.png)

플러그인을 추가하는 곳에서 msfvenom으로 만든 shell.php 파일을 업로드했다. 

![20](https://user-images.githubusercontent.com/51134298/60766556-59bd2100-a0e6-11e9-9d9f-24b713803967.png)

칼리에서 핸들러를 설정해놓고 실행시킨 후 https://192.168.56.110:12380/blogblog/wp-content/uploads/ 로 들어가서 아까 플러그인 추가에서 업로드한 shell.php를 누르면 meterpreter가 실행된다. 

![21](https://user-images.githubusercontent.com/51134298/60766557-59bd2100-a0e6-11e9-91fc-f1c339fe3d39.png)

이것저것 찾아보다가 bash_history를 보았는데 JKanode와 peter의 로그인 기록이 남아있다. 

![22](https://user-images.githubusercontent.com/51134298/60766558-5a55b780-a0e6-11e9-858f-c78a43af7bac.png)

peter로 로그인해보면 무언가 얻을 수 있을 것 같다.

![23](https://user-images.githubusercontent.com/51134298/60766559-5a55b780-a0e6-11e9-9737-d82a943863b3.png)

peter로 로그인을 하니 Z Shell 이라고 한다. 

id를 보니 굉장히 많은 그룹에 속해있었다. 그럼 sudo를 사용해서 root 권한을 얻을 수 있을 것이다.

![24](https://user-images.githubusercontent.com/51134298/60766560-5a55b780-a0e6-11e9-8d2f-270fbf58506a.png)

peter 아이디에서 sudo를 통해 root를 얻고 플래그를 알아낼 수 있었다.

다른 사람들의 write-up을 보니 수많은 풀이법이 존재했다. 그걸 모두 여기에 적자니 양이 너무 많다. 

혹시 모를 다음에 대비해서 키워드만 적어놓으려 한다.

- [ ] Cron Script (cron-logrotate.sh)
- [ ] tftp (nmap -sU <ip>  udp 포트 검색)