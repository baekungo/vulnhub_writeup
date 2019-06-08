# Bulldog: 1

------

<https://www.vulnhub.com/entry/bulldog-1,211/>

설명을 보면 목표는 루트 디렉토리에서 축하 메시지(?)를 보면 된다고 한다. 

![1](https://user-images.githubusercontent.com/51134298/59153298-d67dc080-8a90-11e9-80b5-844a39f7bc0e.png)

실행하면 이렇게 뜬다.

![2](https://user-images.githubusercontent.com/51134298/59153299-d67dc080-8a90-11e9-83cb-4203dd00edf1.png)

웹페이지에 접속한 모습이다. 여러 설명들이 있다.

![3](https://user-images.githubusercontent.com/51134298/59153300-d67dc080-8a90-11e9-919e-aef1a72aa1c7.png)

Dirb를 사용해 디렉토리를 검색해보았다. Dirb는 커맨드 기반의 웹 디렉토리 검색 도구이다.

Nikto로도 검색을 해봤는데, dev가 눈에 띄고 admin 페이지를 통해 로그인할 수 있을 것 같다. 

일단 dev 페이지로 가본다. 

![4](https://user-images.githubusercontent.com/51134298/59153301-d67dc080-8a90-11e9-97de-f88d2d63da95.png)

Web-Shell 이라고 되어있다. 

![5](https://user-images.githubusercontent.com/51134298/59153302-d7165700-8a90-11e9-82a6-4b2199b1045d.png)

하지만 로그인을 하지 않으면 쓸 수 없는 것 같다.

어떻게 로그인을 하는지 찾아보다가 dev 페이지 소스보기에 실마리가 있었다.

![6](https://user-images.githubusercontent.com/51134298/59153303-d7165700-8a90-11e9-9930-c0a1a318c421.png)

40자리인 것을 보니 SHA1 해시인 것 같다. 

![7](https://user-images.githubusercontent.com/51134298/59153304-d7165700-8a90-11e9-9c8e-76b839955322.png)

해시값들을 확인해보았는데 위에 4개는 나오지 않고 밑에 2개는 각각 bulldog, bulldoglover 라는 값이 나왔다. 

해당 암호를 가지고 로그인을 할 수 있을 것 같다. 

![9](https://user-images.githubusercontent.com/51134298/59153287-d4b3fd00-8a90-11e9-9cbf-b3f9d0e48762.png)

admin으로 가서 로그인을 했다. 로그인이 성공했으니 다시 dev로 가서 webshell을 들어가본다.

![10](https://user-images.githubusercontent.com/51134298/59153288-d4b3fd00-8a90-11e9-8394-71f46d12caa8.png)

Webshell 페이지를 그림과 같이 나오고, 사용 가능하게 정해준 명령어들 밖에 쓰지 못한다고 한다. 

![11](https://user-images.githubusercontent.com/51134298/59153289-d4b3fd00-8a90-11e9-81af-0f0ee4d3251a.png)

파이프로 명령어 목록 이외의 명령어를 해보니 가능했다.

그럼 wget으로 쉘코드가 담긴 파일을 여기에 업로드 시킨 후 실행시키면 편하게 컨트롤 할 수 있을 것이다.

![12](https://user-images.githubusercontent.com/51134298/59153290-d54c9380-8a90-11e9-9d6b-d868a15852d1.png)

칼리에서 80번 포트를 열어주고 wget을 통해 미리 만들어둔 python 쉘코드를 다운로드한다. 

![13](https://user-images.githubusercontent.com/51134298/59153291-d54c9380-8a90-11e9-90ad-831b9dbaf111.png)

이제 칼리에서 핸들러를 실행하고 웹쉘에서 payload.py를 실행해준다.

![14](https://user-images.githubusercontent.com/51134298/59153292-d54c9380-8a90-11e9-9d74-ce91a4536087.png)

현재 id는 django로 되어있다. 권한 상승이 필요할 것 같으니 힌트를 찾아본다. 

![15](https://user-images.githubusercontent.com/51134298/59153293-d54c9380-8a90-11e9-86a3-469a2ea7a644.png)

.hiddenadmindirectory 라는 이름이 너무 수상해보이는 디렉토리를 발견했다. 

![16](https://user-images.githubusercontent.com/51134298/59153294-d5e52a00-8a90-11e9-9334-6165789fed3c.png)

note 라는 파일의 내용을 보니 app을 실행시키고 패스워드를 얻으라고 한다. 

그 뒤에도 여러 말이 있지만 핵심은 app을 실행시켜야 할 것 같다. 하지만 실행권한이 없다. 

파일에는 패스워드를 알려주는 내용이 있을 것이라 추측되고, 이는 파일의 문자열만 읽어서 알 수 있을 것 같다.

![17](https://user-images.githubusercontent.com/51134298/59153295-d5e52a00-8a90-11e9-8ead-24f4df879b88.png)

일부를 캡처한 내용이다. SUPERultH, imatePASH, SWORDyouH ... 등의 이상한 문자열이 존재한다.

이어붙이니 이상한 말이 된다. 매끄러운 단어가 될 것 같으면서도 이상하게 안 이어지는데 원인을 찾아보았다.

뒤에 H를 떼고 붙여보면 "SUPERultimatePASSWORDyouCANTget" 가 된다.

이러면 단어가 끊키지 않고 문장스러워진다. 

![18](https://user-images.githubusercontent.com/51134298/59153296-d5e52a00-8a90-11e9-8238-28b4db926996.png)

비밀번호가 맞으면 root 권한을 얻게된다. root 디렉토리로 가면 축하 메시지가 있다. 

![19](https://user-images.githubusercontent.com/51134298/59153297-d5e52a00-8a90-11e9-8161-28b3fe420b2f.png)





