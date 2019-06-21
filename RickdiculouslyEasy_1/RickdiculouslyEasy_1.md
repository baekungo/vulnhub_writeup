# RickdiculouslyEasy: 1

------

<https://www.vulnhub.com/entry/rickdiculouslyeasy-1,207/>

설명을 보면 간단한 Rick and Morty 테마의 boot to root 라고 한다. 

Rick and Morty는 처음 들어봐서 검색해보니 미국의 애니메이션인 것 같다. 

총 130포인트 만큼의 플래그가 있고 이 포인트와 함께 root 권한을 획득하면 되는 문제이다. 

![1](https://user-images.githubusercontent.com/51134298/59894483-b13b6b80-941b-11e9-8a39-c20141f82511.png)

이번에도 시작은 nmap으로 해보았다. ip가 ~108인 것이 이번 문제의 서버 ip 이다. 

![2](https://user-images.githubusercontent.com/51134298/59894484-b1d40200-941b-11e9-9a26-28abc2c8a3df.png)

포트를 보았더니 뭔가 많이 열려있다. 일단 차례대로 보면, 포트는 총 7개가 열려있고, 21번, 80번 포트는 우리가 잘 알고있는 포트이다. 22번 포트는 ssh?라고 되어있고 9090번 포트는 Cockpit web service라고 써있다. 13337번, 60000번 포트는 알 수 없는 서비스이고 22222번 포트는 ssh로 사용되고 있다.  

밑을 보면 핑거프린트가 있는데 22번 포트, 13337번 포트, 60000번 포트에 대한 것이 각각 존재한다. 그 중에 13337번 포트의 핑거프린트를 보면 FLAG 10 point를 찾을 수있다. (10point)

![3](https://user-images.githubusercontent.com/51134298/59894485-b1d40200-941b-11e9-9c99-9c4126bc308d.png)

모든 포트로 접속을 시도해보았다. 22번과 13337번 포트는 핑거프린트에 있는 문구만 출력한다. 

60000번 포트에 들어가보니 쉘을 얻었다.  FLAG.txt가 있었고 그 안에는 10 point 짜리 플래그가 있었다. (20point)

그리고 다른 명령어를 수도 없이 집어넣어봤지만 죄다 막혀있어서 나갈 수 없었다. 이름이 괜히 블랙홀이 아니었다. 

![4](https://user-images.githubusercontent.com/51134298/59894486-b1d40200-941b-11e9-9b99-2c4dff643645.png)

홈페이지에 들어왔다. 딱히 눈에 띄는 것은 없었다. 일단 9090번 포트로 들어가본다. 

![5](https://user-images.githubusercontent.com/51134298/59894488-b1d40200-941b-11e9-8003-0d5305e1c2c2.png)

9090번 포트로 들어와보니 로그인 화면과 함께 플래그가 있었다. (30point)

![6](https://user-images.githubusercontent.com/51134298/59894489-b26c9880-941b-11e9-90de-9fe5f1d2abb0.png)

이번엔 21번 포트인 ftp로 접속해보았다. FLAG.txt가 있고 텍스트 파일을 열어보면

FLAG{Whoa this is unexpected} - 10 Points 라는 플래그가 있다. (40point)

![7](https://user-images.githubusercontent.com/51134298/59894490-b26c9880-941b-11e9-8378-c61aba0f5d73.png)

다시 돌아와서 이번엔 dirb를 이용해 검사해보았다. passwords라는 디렉토리가 있어서 들어가보았다.

![8](https://user-images.githubusercontent.com/51134298/59894491-b26c9880-941b-11e9-9c19-98221f4f2b58.png)

플래그를 클릭해보니  " FLAG{Yeah d- just don't do it.} - 10 Points " 라는 문구가 나온다. (50point)

![9](https://user-images.githubusercontent.com/51134298/59894492-b26c9880-941b-11e9-9416-785965783079.png)

이건 password.html 내용이다. 소스를 보면 Password는 winter라고 써있다. 다른건 없으니 cgi-bin 으로 들어가본다.

![10](https://user-images.githubusercontent.com/51134298/59894493-b3052f00-941b-11e9-883f-9b0b7f46460a.png)

robots.txt에서 본 것을 참고해서 root_shell로 들어가보니 함정이었고, tracertool을 가보았다.

![11](https://user-images.githubusercontent.com/51134298/59894463-ae407b00-941b-11e9-84ad-9b092d65b9c6.png)

ip를 입력하면 traceroute 명령이 실행된다. 쓴 값이 a라고 할 때 traceroute a 라는 명령어를 실행하는 것 같다.

그러면 세미콜론을 이용해서 다른 명령어를 추가로 쓸 수 있는지 확인해보았다. 

![12](https://user-images.githubusercontent.com/51134298/59894464-ae407b00-941b-11e9-8274-b862a83f1da9.png)

가능했다. 이제 칼리로 접속을 하면 된다.

![13](https://user-images.githubusercontent.com/51134298/59894465-ae407b00-941b-11e9-9af5-8da1f12a3246.png)

![14](https://user-images.githubusercontent.com/51134298/59894466-aed91180-941b-11e9-9b3c-e8b853cb96ab.png)

접속이 되었다. apache가 id로 되어있고 힌트가 될만한 것들을 찾아보았다. 

아까 password가 Winter라고 했으니 Id를 찾아보기 위해 /etc/passwd의 내용을 확인해봤다.

![15](https://user-images.githubusercontent.com/51134298/59894467-aed91180-941b-11e9-9f95-dd5ee7036dcf.png)

웬 동물이 그려진다. cat 명령어 내용이 진짜 고양이를 보여주는 모양이다. 내용 확인이 안되니 head나 tail 명령어로 다시 해보았다. 

![16](https://user-images.githubusercontent.com/51134298/59894468-aed91180-941b-11e9-80b4-9c4d018fdf99.png)

로그인을 전부 시도해보기에는 너무 많은 Id가 있어서 툴을 사용할까 하다가 밑에서 두번째에 있는 Summer가 눈에 띄었다.

패스워드가 winter이니까 Id가 Summer일 것 같기도 한 생각이 들어서 바로 시도했다.

![17](https://user-images.githubusercontent.com/51134298/59894469-aed91180-941b-11e9-960a-2ad009ccb10f.png)

ssh를 사용하는 22222번 포트로 Summer 계정으로 들어갈 수 있었다. 

![18](https://user-images.githubusercontent.com/51134298/59894470-af71a800-941b-11e9-8709-4d0c531cb52e.png)

홈 디렉토리에 FLAG.txt 라는 파일이 있고 안에 FLAG를 볼 수 있다. (60point)

safe 라는 파일도 있었는데, 실행을 해보면 아래와 같이 쓰여있었다.

![19](https://user-images.githubusercontent.com/51134298/59894472-af71a800-941b-11e9-95bb-2747277e2871.png)

그래서 아무거나 넣어서 시도해보았다.

![20](https://user-images.githubusercontent.com/51134298/59894473-b00a3e80-941b-11e9-9420-46b83eb5ff54.png)

정확한 인자를 넣어줘야 정상적으로 메시지를 복호화해주는 것 같다. 

그래서 더 찾아보던중, Morty라는 디렉토리에 가보았다.

![21](https://user-images.githubusercontent.com/51134298/59894474-b00a3e80-941b-11e9-8fbf-677c6069bd5b.png)

zip파일이 있었고, unzip으로 풀어보니 권한이 없어서 파일을 생성할 수 없다고 한다. 그래서 p옵션을 주었다. 

![22](https://user-images.githubusercontent.com/51134298/59894475-b00a3e80-941b-11e9-9df2-6c16afa21132.png)

131333 이라는 플래그가 있었다. (80point)

위에 내용을 보니 safe password.... 라고 되어있는데, 아까 인자를 몰라서 제대로 보지못한 safe 파일이 떠올랐다.

![23](https://user-images.githubusercontent.com/51134298/59894476-b0a2d500-941b-11e9-9319-ffdcbda8f96b.png)

제대로 복호화가 되었다! 또 플래그가 있었다. (100point)

Rick 패스워드 힌트 또한 있다. 대문자 1개, 숫자 1개, old band 이름 중에 한 단어 라고 한다. 

old band가 무슨 말인지 몰라서 검색해보았다. 

![24](https://user-images.githubusercontent.com/51134298/59894477-b0a2d500-941b-11e9-9e4d-506644a02550.png)

검색 결과이다. "The Flesh Curtains"이니까 Flesh 아니면 Curtains 인 것 같다.

결국 A0Flesh  부터 Z9Curtains 까지가 후보인데,  이 리스트를 파일에 적어야한다.

![25](https://user-images.githubusercontent.com/51134298/59894478-b0a2d500-941b-11e9-8643-49e4e47b179d.png)

maskprocessor라는 툴을 이용하였고 mp64로 실행할 수 있다. "?u"는 대문자, "?d"에 숫자가 온다. 

Flesh와 Curtains를 모두 wordlist라는 파일에 넣었다. 

![26](https://user-images.githubusercontent.com/51134298/59894479-b0a2d500-941b-11e9-889a-1b59dabd09ec.png)

hydra 툴을 사용했다.  l 옵션에는 Id를 적고 P 옵션에는 패스워드 파일, s 옵션에는 포트번호를 넣었다. 

결과로 나온 password는 P7Curtains 이다. 바로 로그인을 해보았다.

![27](https://user-images.githubusercontent.com/51134298/59894480-b13b6b80-941b-11e9-80c8-3a381de353b5.png)

홈 디렉토리이다. ThisDoesntContainAnyFlags 라는 디렉토리가 있다. 심리전을 하는 것 같다. 

들어가보았더니 진짜 아무것도 없다. 제작자에게 진 것 같다. RICKS_SAFE라는 곳을 들어가보았다. 

safe라는 파일이 있는데 아까 Summer에 있던 safe와 같은 파일이다. 힌트가 더 이상은 없었다.

![28](https://user-images.githubusercontent.com/51134298/59894481-b13b6b80-941b-11e9-8986-b9c3b80fb4d7.png)

그래서 일단 sudo를 해보았는데 root 권한을 획득할 수 있었다. 

![29](https://user-images.githubusercontent.com/51134298/59894482-b13b6b80-941b-11e9-9e12-5ad05a67eab3.png)

root의 홈 디렉토리에 FLAG가 있었다. (130point)

130 포인트를 모두 모았다!















