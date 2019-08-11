# Brainpan: 1

------

<https://www.vulnhub.com/entry/brainpan-1,51/>

해당 machine의 root 권한을 얻어내는 것이 목표이다. 

![1](https://user-images.githubusercontent.com/51134298/61598790-68b2e000-ac5d-11e9-857b-9e7f9e9e4e57.png)

ip를 확인해보았다. ~.111이 해당 machine의 ip이다.

![2](https://user-images.githubusercontent.com/51134298/61598791-68b2e000-ac5d-11e9-9249-0a84c52274f1.png)

포트를 확인해보았다. 9999번 포트와 10000번 포트가 열려있다.

일단 웹으로 들어가보았다.

![3](https://user-images.githubusercontent.com/51134298/61598792-68b2e000-ac5d-11e9-9c25-efde19899e0e.png)

이런 사진이 나온다. 재밌어서 읽어보긴 했지만 딱히 힌트가 될만한건 없다. 

![4](https://user-images.githubusercontent.com/51134298/61598794-68b2e000-ac5d-11e9-9963-cf2101216614.png)

nikto로 살펴보았다. /bin 디렉토리로 가보면 무언가가 있을 것 같다.

![5](https://user-images.githubusercontent.com/51134298/61598795-694b7680-ac5d-11e9-9525-34778bd329f1.png)

brainpan.exe 파일이 존재한다. 

일단 열어보았다. 

![6](https://user-images.githubusercontent.com/51134298/61598796-694b7680-ac5d-11e9-82a7-adbf81d09f7c.png)

9999번 포트로 접근이 가능한 것 같다. 

칼리에서 다운을 받아보았다. 

![7](https://user-images.githubusercontent.com/51134298/61598797-694b7680-ac5d-11e9-8467-684eef5bc451.png)

wine을 사용해 열어놓고 접속해보았다.

(wine은 리눅스에서 윈도우 프로그램을 열기 위한 프로그램이다.)

++ wine을 찾아보다가 이름이 Wine Is Not an Emulator 의 줄임말이란 사실을 알게됐다...

![8](https://user-images.githubusercontent.com/51134298/61598798-694b7680-ac5d-11e9-851a-2cad32cfed28.png)

접속해보았더니 패스워드를 입력하라고 나온다. 

막 쳐보면 ACCESS DENIED라고 나온다. 

![9](https://user-images.githubusercontent.com/51134298/61598799-69e40d00-ac5d-11e9-8cdd-6ae9d7980a06.png)

올리디버거로 패스워드가 뭔지 알아보았다.

strcmp 함수를 찾아 들어가보니 스택에 shitstorm을 넣는 것을 확인할 수 있다.

따라서 입력한 값과 shitstorm을 비교해 ACCESS를 시켜주는 것 같다.

![10](https://user-images.githubusercontent.com/51134298/61598800-69e40d00-ac5d-11e9-8e72-81d5d6f6aea9.png)

입력해서 ACCESS GRANTED라고 출력된다. 근데 아무일도 일어나지 않는다.

이후로 헤매던 중에 버퍼 오버플로우가 떠올랐다. 

![11](https://user-images.githubusercontent.com/51134298/61598801-69e40d00-ac5d-11e9-9bba-9137fd6b26b4.png)

다시 올리디버거로 가서 aaaa를 입력한 후 메모리 주소를 보았다.

현재 입력한 값이 EAX에 들어가있고 위치는 0043f650 이다. 그리고 EBP의 값은 0043F868 이다. 입력한 값이 들어가는 주소에서 EBP까지의 거리는 520바이트이다. 

![12](https://user-images.githubusercontent.com/51134298/61598802-69e40d00-ac5d-11e9-8ab8-c716ac52a345.png)

테스트를 해보았다. A를 524개, RET자리에 B를 4개, 그 뒤로 C를 300개 채웠다.

EIP에는 B 4개가 들어가있고 스택포인트에는 그 뒤에 오는 C들이 있다. 

이제 C자리에 쉘코드를 넣고 RET자리에는 JMP ESP의 주소를 덮어주면 ESP에 있는 쉘코드가 실행될 것이다. 

![13](https://user-images.githubusercontent.com/51134298/61598803-6a7ca380-ac5d-11e9-815d-cea62e075f97.png)

jmp esp의 주소는 311712f3 이다.

![14](https://user-images.githubusercontent.com/51134298/61598804-6a7ca380-ac5d-11e9-8ab6-0217ca4832dc.png)

msfvenom으로 쉘코드를 만들어준다. 

![15](https://user-images.githubusercontent.com/51134298/61598806-6a7ca380-ac5d-11e9-83d9-1fb8f549a98a.png)

이제 핸들러를 설정하고 위 코드를 실행시키면 리버스쉘을 얻을 수 있다. 

![16](https://user-images.githubusercontent.com/51134298/61598807-6a7ca380-ac5d-11e9-8014-ba82df4ac2a4.png)

연결이 성공적으로 되었다. 

![17](https://user-images.githubusercontent.com/51134298/61598808-6b153a00-ac5d-11e9-9643-5e45fc7fd898.png)

현재 puck으로 로그인되어있다. 이제 root로 권한상승을 해야한다.

![18](https://user-images.githubusercontent.com/51134298/61598809-6b153a00-ac5d-11e9-8bd5-5647fd9e4586.png)

sudo -l을 해보았다. /home/anansi/bin/anansi_util 파일이 sudo로 실행이 가능했다.

실행을 해보니 파라미터 3개 중 하나를 선택해야한다. 

![19](https://user-images.githubusercontent.com/51134298/61598810-6b153a00-ac5d-11e9-9e0a-0c7efa5e07d6.png)

manual 명령어는 man 명령어와 같은 역할을 하는 것 같다.

man 명령어를 실행하니 경고가 출력된다. (less, more를 사용하기 때문이다.)

![20](https://user-images.githubusercontent.com/51134298/61598811-6b153a00-ac5d-11e9-80ab-ca074089f45c.png)

여기서 엔터를 누르면 메뉴얼이 나온다. 

하지만 여기서 ! 를 하고 명령어를 입력하면 명령이 실행된다.

![21](https://user-images.githubusercontent.com/51134298/61598788-681a4980-ac5d-11e9-863a-6ce567f2ad58.png)

이렇게 root 권한을 얻을 수 있다. 

![22](https://user-images.githubusercontent.com/51134298/61598789-681a4980-ac5d-11e9-9774-f044d356f9af.png)





++

다른 풀이와 비교해보았는데 풀이 방법이 다양했다. 버퍼 오버플로우를 할 때 프로그램을 실행해서 오프셋을 찾는 방법도 있었다. 권한 상승에서도 여러가지 방법이 존재했다. 처음 보는 방법도 있었는데 그 부분은 따로 공부해보아야겠다. 