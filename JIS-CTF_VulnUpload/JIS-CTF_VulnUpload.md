# JIS-CTF_VulnUpload

------

<https://www.vulnhub.com/entry/jis-ctf-vulnupload,228/>

이 머신에는 5개의 플래그가 있고 한시간 반동안 모든 플래그를 찾으라고 설명되어있다.

![1559554073634](https://user-images.githubusercontent.com/51134298/58801969-fd7a6380-8646-11e9-8065-c3a95a7b8445.png)

nmap을 통해 ip주소를 확인해본 결과 ~.105가 해당 시스템의 ip였다.

![1559554193192](https://user-images.githubusercontent.com/51134298/58801970-fd7a6380-8646-11e9-8514-7de9ea389089.png)

포트를 확인해본 결과 22번 포트와 80번 포트가 열려있다. 

![1559554544848](https://user-images.githubusercontent.com/51134298/58801971-fd7a6380-8646-11e9-87dd-7f364786ce2c.png)

nikto를 통해 웹 취약점을 스캔해보았다. 

robots.txt 파일을 통해 디렉토리들을 확인할 수 있다고 나온다.  

![1559554946609](https://user-images.githubusercontent.com/51134298/58801973-fe12fa00-8646-11e9-85af-6860f09a111b.png)

첫 화면이다. Username과 Password 입력 창이 있다. robots.txt 로 들어가본다. 

![1559555033006](https://user-images.githubusercontent.com/51134298/58801974-feab9080-8646-11e9-96c5-97c7353ef7f2.png)

힌트가 될만한 디렉토리들이 많이 보인다. 일단 flag에 들어가본다.

![1559555099560](https://user-images.githubusercontent.com/51134298/58801976-feab9080-8646-11e9-86fa-f96d3541e3f7.png)

첫번째 플래그가 나온다. 다음, admin에 들어가본다. 

![1559555157989](https://user-images.githubusercontent.com/51134298/58801978-feab9080-8646-11e9-9ad0-c965b95dc035.png)

안들어가진다. admin_area에 들어가본다.

![1559555194641](https://user-images.githubusercontent.com/51134298/58801980-feab9080-8646-11e9-9b53-43e0c0ac9ca5.png)

Not Found가 아니라서 소스보기를 해보았다.

![1559555330417](https://user-images.githubusercontent.com/51134298/58801981-ff442700-8646-11e9-9958-0ead662d9788.png)

두번째 플래그가 있다. 이 아이디와 비밀번호로 로그인을 했다.

![1559555388537](https://user-images.githubusercontent.com/51134298/58801982-ff442700-8646-11e9-8cb3-f74cdcff75a9.png)

File Upload Center라고 되어있고, 파일을 업로드 할 수 있는 창이 나온다. 뭔지 몰라서 아무거나 넣어보았다. 

![1559555483019](https://user-images.githubusercontent.com/51134298/58801983-ff442700-8646-11e9-9fcf-ec54ed7e6a6c.png)

텍스트 파일을 아무거나 넣었는데 Success라고 뜬다. 아까 본 디렉토리 중에 uploaded_file이 있었기 때문에 들어가본다.

![1559555830736](https://user-images.githubusercontent.com/51134298/58801985-ff442700-8646-11e9-8a2a-0dfc14e9d22a.png)

uploaded_file 디렉토리에서 올린 파일의 이름으로 들어가보니, 파일의 내용이 나오는 것을 알 수 있었다. 

PHP 코드를 삽입해 작동하는지 확인해본다.

![1559556838658](https://user-images.githubusercontent.com/51134298/58801986-ffdcbd80-8646-11e9-8cec-27a2ea343b9c.png)

오른쪽과 같은 코드를 올렸더니 제대로 작동하는 것을 확인할 수 있다. 이제 쉘코드를 올려본다.

![1559557533502](https://user-images.githubusercontent.com/51134298/58801987-ffdcbd80-8646-11e9-8716-039ba263ff35.png)

Metasploit으로 쉘코드를 만들고 업로드 한다. 

![1559557698217](https://user-images.githubusercontent.com/51134298/58801988-ffdcbd80-8646-11e9-9d9a-7ca6b8d62ca7.png)

핸들러를 생성한 후 192.168.56.105/uploaded_files/shell.php 로 접속한다

![1559558864693](https://user-images.githubusercontent.com/51134298/58801990-ffdcbd80-8646-11e9-92af-7b55affa690d.png)

연결이 되었고, id를 보니 www-data였다. 

![1559559018377](https://user-images.githubusercontent.com/51134298/58801991-00755400-8647-11e9-9011-b0f9bec72f72.png)

/var/www/html 디렉토리에 flag.txt와 hint.txt가 있다. 

flag.txt는 접근이 안되었고 hint.txt의 내용을 보니 플래그가 있었다.

힌트의 내용은 flag.txt를 읽기 위해서는 technawi 유저의 패스워드를 숨겨진 파일에서 찾으라고 되어있다. 

![1559564454595](https://user-images.githubusercontent.com/51134298/58801992-00755400-8647-11e9-8ffa-50a164e6a062.png)

technawi 라는 문자열이 들어간 내용을 가진 파일을 검색해보았다. 

위에서 두번째에 있는 파일 /etc/mysql/conf.d/credentials.txt 의 내용을 확인해본다. 

![1559564611801](https://user-images.githubusercontent.com/51134298/58801994-00755400-8647-11e9-8a1f-0bb8f624ebdc.png)

네번째 플래그와 함께 technawi의 password가 들어있다. 

이 비밀번호를 갖고 ssh로 접속을 할 수 있을 것이다.

![1559564729713](https://user-images.githubusercontent.com/51134298/58801995-00755400-8647-11e9-9088-ac5cde139e09.png)

접속을 한 모습이다. 이제 flag.txt를 열어 마지막 플래그를 찾아본다.

![1559564937374](https://user-images.githubusercontent.com/51134298/58801996-010dea80-8647-11e9-83b5-bb67515b8e98.png)















