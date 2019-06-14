# FristiLeaks_1.3

------

FristLeaks: 1.3 <https://www.vulnhub.com/entry/fristileaks-13,133/>

![1](https://user-images.githubusercontent.com/51134298/59495341-16e2a180-8eca-11e9-98c4-c554beb216a8.png)

root 권한을 획득 후 플래그를 찾는 문제이다. 

![2](https://user-images.githubusercontent.com/51134298/59495342-16e2a180-8eca-11e9-92a9-87e55d3e0e36.png)

nikto를 이용해 검사해봤다.

robots.txt, /cola, /sisi, /beer 파일이 있다. 또 /icons/, /images/ 디렉토리도 존재한다. 일단 홈페이지에 접속해보았다.

![4](https://user-images.githubusercontent.com/51134298/59495344-16e2a180-8eca-11e9-84b2-79f48f01b4df.png)

분홍색 바탕의 화면이 나온다. 다른 특이한 점은 보이지 않아서 /robots.txt에 들어가보니 /sisi, /beer, /cola가 disallow 되어있고 이를 접속해보았다.

![3](https://user-images.githubusercontent.com/51134298/59495343-16e2a180-8eca-11e9-9cb3-d4f8f11ff4c2.png)

셋 다 이 화면이 나온다. 아무것도 얻은 게 없다. image 디렉토리로 가보았다. 

![5](https://user-images.githubusercontent.com/51134298/59495347-177b3800-8eca-11e9-87d5-5cc559a84d87.png)

당황스럽게도 힌트를 못 찾았다. 오랜 시간을 삽질했고 결국에 /sisi, /cola, /beer가 있는 이유에 대해 생각해보았다.

홈페이지에 있는 문구인 "KEEP CALM AND DRINK FRISTI"를 보면 FRISTI는 분명히 음료수일 것이다. 

cola, beer 또한 마시는 것이다. (sisi는 뭔지 몰랐지만 검색해보니 음료수였다.)

그럼 /sisi, /cola, /beer가 있으니 /fristi도 있지 않을까? 라는 생각에 /fristi를 접속해보았다.

![6](https://user-images.githubusercontent.com/51134298/59495348-177b3800-8eca-11e9-8ddd-fa6fbb9500d1.png)

드디어 로그인 페이지를 찾아냈다. 하지만 Username도 모르고 Password도 모른다. 

소스코드를 보니 주석에 난잡한 암호문이 있었다. 

![7](https://user-images.githubusercontent.com/51134298/59495349-177b3800-8eca-11e9-8524-edf6f167942a.png)

=으로 끝나는 것을 보니 Base64 인코딩이 되어있는 것 같다.

![8](https://user-images.githubusercontent.com/51134298/59495351-177b3800-8eca-11e9-9511-de003fcb3346.png)

PNG라고 써있는 것을 보니 다운로드 받고 .png로 바꿔서 열어보아야 할 것 같다.

![9](https://user-images.githubusercontent.com/51134298/59495352-1813ce80-8eca-11e9-8f64-ad2a155b9396.png)

파일을 열어보니 이렇게 써있다. Password인 것 같다. Username이 무엇일까 생각해보았다.

소스코드 위쪽을 보니 Username은 왠지 주석을 달아주신 eezeepz님이라고 생각된다.

![10](https://user-images.githubusercontent.com/51134298/59495354-1813ce80-8eca-11e9-983c-93213718bccf.png)

![11](https://user-images.githubusercontent.com/51134298/59495355-1813ce80-8eca-11e9-9368-9ed93d62e746.png)

로그인이 성공했다. upload file이라고 되어있다,

![12](https://user-images.githubusercontent.com/51134298/59495356-1813ce80-8eca-11e9-92aa-4cc336e43e2c.png)

php reverse shell 코드를 Upload 하려고 했지만 Image만 가능하다고 한다. 

![13](https://user-images.githubusercontent.com/51134298/59495357-18ac6500-8eca-11e9-87d8-b5c762f481e7.png)

그냥 파일 이름의 끝에 .jpg를 붙이고 업로드했다. 

![14](https://user-images.githubusercontent.com/51134298/59495358-18ac6500-8eca-11e9-9ba7-9fca06cf1b02.png)

칼리에서 연결 준비를 해주고 업로드된 파일을 실행시켰더니 연결이 성공적으로 되었다. 

![15](https://user-images.githubusercontent.com/51134298/59495359-18ac6500-8eca-11e9-812a-78c10c14e3c1.png)

home 디렉토리의 eezeepz를 가보니 notes.txt가 있었고 내용은 위와 같다.

runthis라는 파일에 명령어를 쓰면 admin 권한으로 명령이 실행될 수 있다는 내용인 것 같다.

![16](https://user-images.githubusercontent.com/51134298/59495360-18ac6500-8eca-11e9-93f6-827b30b12229.png)

/home/admin 권한을 바꾸는 명령어를 runthis에 입력해준다. 

admin 디렉토리의 권한이 바뀌어있는 것을 확인할 수 있다.

![17](https://user-images.githubusercontent.com/51134298/59495362-1944fb80-8eca-11e9-9d70-d115ed78e642.png)

admin 디렉토리 내부이다. cryptedpass.txt와 whoisyourgodnow.txt를 읽어보았다. 

decoding을 해야할 것 같은 문자열이 있다. 마침 cryptpass.py라는 이름의 파일이 있다. 이를 자세히 봐야겠다.

![18](https://user-images.githubusercontent.com/51134298/59495364-1944fb80-8eca-11e9-96df-8bfe37f93c12.png)

이 파일은 암호를 encoding 하는 파일인 것 같다. 소스코드를 확인해보았다.

![19](https://user-images.githubusercontent.com/51134298/59495366-1944fb80-8eca-11e9-8034-76891dd0b557.png)

소스코드를 보니 패스워드를 이 파일로 encoding을 한 결과가 "mVGZ3O3omkJLmy2pcuTq"로 나오는 것 같다. 

그러면 encoding을 한 순서와 반대로 decoding을 해주면 원래의 패스워드가 나올 것이다.

```
import base64,codecs,sys

def decodeString(str):
    s = codecs.decode(str[::-1], 'rot13')
    return base64.b64decode(s)

cryptoResult=decodeString(sys.argv[1])
print (cryptoResult)
```

이렇게 코드를 바꾸고나서 실행을 시켜보니

mVGZ3O3omkJLmy2pcuTq => thisisalsopw123

=RFn0AKnlMHMPIzpyuTI0ITG => LetThereBeFristi!

패스워드를 알 수 있었다. 

![20](https://user-images.githubusercontent.com/51134298/59495331-1518de00-8eca-11e9-831e-8fec5227d6e6.png)

admin이 되었다. 딱히 할 것을 못찾아서 그냥 fristigod으로 바꾸었다. 

![21](https://user-images.githubusercontent.com/51134298/59495332-1518de00-8eca-11e9-8d98-835326d94493.png)

fristigod으로 접속한 상태이다. 무엇이 있나 찾아보기 위해 홈 디렉토리로 갔다.

![22](https://user-images.githubusercontent.com/51134298/59495333-15b17480-8eca-11e9-93cd-525bd20c3a86.png)

.secret_admin_stuff 라는 디렉토리가 존재했고 이름만 봐도 수상하다. 안에는 doCom이라는 파일이 있다.

![23](https://user-images.githubusercontent.com/51134298/59495335-15b17480-8eca-11e9-8c8a-17c274f933ac.png)

root로만 실행이 되는 파일이었다. .bash_history를 읽어보았다.

![25](https://user-images.githubusercontent.com/51134298/59495337-15b17480-8eca-11e9-852e-52642f2c3127.png)

![24](https://user-images.githubusercontent.com/51134298/59495336-15b17480-8eca-11e9-99b1-3a0e0bb731d2.png)

sudo -l 을 해보니 설명이 나와있다. fristigod으로 doCom을 실행할 수 있다고 한다. 

여기서 /bin/bash를 실행하면 root 권한으로 명령을 할 수 있을 것이다. 

![26](https://user-images.githubusercontent.com/51134298/59495338-164a0b00-8eca-11e9-9e28-30d1aebca955.png)

이제 flag를 찾으면 끝난다.

![27](https://user-images.githubusercontent.com/51134298/59495339-164a0b00-8eca-11e9-98c7-5ec8fa0d77d1.png)

















