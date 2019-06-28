# Tr0ll: 2

------

<https://www.vulnhub.com/entry/tr0ll-2,107/>

이번 문제는 Tr0ll: 2 이다. 

![1](https://user-images.githubusercontent.com/51134298/60311818-de47cb00-9993-11e9-8fc6-5a079c55484f.png)

ip는 ~109이고 열려있는 포트를 확인해보았다. 

![2](https://user-images.githubusercontent.com/51134298/60311819-de47cb00-9993-11e9-87c2-3fe4ea6260c6.png)

사이트를 들어갔더니 아무것도 없다고한다..

![3](https://user-images.githubusercontent.com/51134298/60311820-dee06180-9993-11e9-96ad-068e074c0ed3.png)

dirb를 사용해 디렉토리와 파일을 검색해보았다. 

![4](https://user-images.githubusercontent.com/51134298/60311821-dee06180-9993-11e9-84d1-b2982d06e522.png)

robots에 들어갔더니 많은 디렉토리들이 있었다. 

![5](https://user-images.githubusercontent.com/51134298/60311822-dee06180-9993-11e9-8505-0c533a83f567.png)

모두 접속을 시도해보니 아예 안들어가지거나 위에 사진이 나오는 경우가 있었다. 

이미지 소스 이름이 힌트인가싶어서 다운로드를 받아보았다. 

![6](https://user-images.githubusercontent.com/51134298/60311823-dee06180-9993-11e9-88d0-991b93604e6e.png)

다운을 받고 cat 으로 내용을 보았다.

![7](https://user-images.githubusercontent.com/51134298/60311824-df78f800-9993-11e9-8080-44b3abae5b6d.png)

마지막쯤에 Look Deep within y0ur_self for the answer 이라고 적혀있다. 

y0ur_self 를 보면 될 것 같다. 

![8](https://user-images.githubusercontent.com/51134298/60311826-df78f800-9993-11e9-99b7-13dc9cbaed92.png)

y0ur_self 디렉토리에 들어온 모습이다. answer.txt가 있다. 

![9](https://user-images.githubusercontent.com/51134298/60311827-df78f800-9993-11e9-8944-da9587956292.png)

알 수 없는 문자열이 매우 많이 나온다. =을 보니 base64로 인코딩된 느낌이다. 

이 txt를 다운받아 base64 -d(디코딩) 명령어를 통해 원래 문자열을 보았다. 

![10](https://user-images.githubusercontent.com/51134298/60311828-df78f800-9993-11e9-85e7-b5a7a557db2a.png)

문자열을 찾았다. 이게 password인지, id인지는 확실하지 않다.

일단 아까 포트를 보았을 때 ftp, ssh가 있었으므로 둘 다 접속을 시도해본다. 

![11](https://user-images.githubusercontent.com/51134298/60311798-dbe57100-9993-11e9-84d8-fb00f7cbd66f.png)

ftp로 접속을 했다. id와 password는 Tr0ll 이었다. Welcome to .. 에 써있는 것과 일치해서 알기 쉬웠다.

![12](https://user-images.githubusercontent.com/51134298/60311799-dbe57100-9993-11e9-9e0c-d6b820fb1dc1.png)

lmao.zip 이라는 파일이 있다. 다른 명령어들은 먹히질 않는다. 

![13](https://user-images.githubusercontent.com/51134298/60311800-dbe57100-9993-11e9-8118-e1cc5a8c24b1.png)

그래서 칼리에서 다운을 받았다. user와 password는 옵션에 입력해준다. 

unzip으로 풀려고보니 패스워드가 걸려있다. 

![14](https://user-images.githubusercontent.com/51134298/60311801-dc7e0780-9993-11e9-83e8-a6dacb917555.png)

아까 base64 디코딩한 파일에 패스워드가 될만한 문자열이 있을 것 같아서 시도해보았다.

fcrackzip을 사용해 패스워드를 찾았더니 바로 쉽게 패스워드를 찾아낼 수 있었다.

(-D는 사전사용, -u는 unzip 사용, -p는 초기 암호로 문자열 사용)

![15](https://user-images.githubusercontent.com/51134298/60311802-dc7e0780-9993-11e9-8a0d-5dcbec59c36b.png)

암호를 풀고 파일을 읽어보았다. 파일 이름은 noob이고 내용에는 RSA 개인키가 있다.

권한이나 내용을 봤을 때 SSH Key인 것 같아 noob으로 접속을 시도했다.

![16](https://user-images.githubusercontent.com/51134298/60311804-dc7e0780-9993-11e9-950c-bd2f7bb6ba35.png)

i 옵션으로 개인키를 지정해주고 로그인을 시도했지만 실패했다. 놀리는 글만 나온다. 

![17](https://user-images.githubusercontent.com/51134298/60311805-dc7e0780-9993-11e9-947c-1e945ebe1047.png)

방법을 찾아보다가 shell shock 취약점이 존재하는 것을 알았고 바로 시도했다.

```
ssh -i noob noob@192.168.56.109 '() { :;}; echo test'
test
TRY HARDER LOL!
```

() {:;}; 뒤에 있는 명령어가 실행이 되면 취약점이 존재하는 것이다

![18](https://user-images.githubusercontent.com/51134298/60311806-dc7e0780-9993-11e9-87b3-ef54da8de77a.png)

root 권한을 얻을만한 것을 찾아보던 중 의심스러운 곳을 발견했다. 

door1부터 door3까지 있고 현명하게 고르라고한다. 

![19](https://user-images.githubusercontent.com/51134298/60311807-dd169e00-9993-11e9-8e6f-15eae7f47a59.png)

door1로 들어가서 r00t라는 파일을 실행했다. 속았다. 다시 접속해서 door2로 가본다.

![20](https://user-images.githubusercontent.com/51134298/60311808-dd169e00-9993-11e9-99ca-b9052ecb6619.png)

여기도 아니다. 심지어 2분동안 ls 명령어가 안 된다.

몇 번을 시도한 결과, 문 3개에는 각각 다른 기능이 존재하는데 이는 시간이 지남에 따라 순서가 바뀐다.

강제종료하는 것, ls 명령어를 막는 것, 그리고 나머지 1개가 있다.

![21](https://user-images.githubusercontent.com/51134298/60311809-dd169e00-9993-11e9-9fdc-04b4c6ebed2a.png)

나머지 1개는 이렇게 출력이 된다. input을 넣어야한다. 

![22](https://user-images.githubusercontent.com/51134298/60311811-dd169e00-9993-11e9-8ac2-8ba5cc00b024.png)

아무 값이나 넣어봤더니 입력한 값을 그대로 출력하기만 한다. 버퍼오버플로우 느낌이 온다. 

![23](https://user-images.githubusercontent.com/51134298/60311812-ddaf3480-9993-11e9-8c2e-c94a37642338.png)

gdb로 들여다보았다. strcpy 부분에서 버퍼 오버플로우 취약점이 존재한다.

![24](https://user-images.githubusercontent.com/51134298/60311813-ddaf3480-9993-11e9-813b-80f074e6e5f6.png)

인자로 입력한 값이 0xbffffb90에 들어있다. 그리고 ebp는 0xbffffc98에 위치한다. 

sfp까지 덮으려면 총 0x10c 바이트가 필요하다. 그 다음 ret을 덮으면 된다. 

ret에는 system 함수를 덮고 인자로 /bin/bash를 줄 것이다. 그러면 이 프로그램이 끝나고 쉘을 얻을 수 있다.

페이로드는 dummy(10c) + RET(system) + dummy(4) + /bin/sh addr  이렇게 될 것이다.

일단 system의 주소를 구해야한다. 

![25](https://user-images.githubusercontent.com/51134298/60311814-ddaf3480-9993-11e9-976f-411ccc283ffb.png)

0xb7e6b060 이다. /bin/sh 주소를 구해본다. 아래는 그 코드이다.

```
int main(int argc, char **argv)
{
        long addr= 0xb7e6b060; 
        while(memcmp((void*)addr,"/bin/sh",8)) 
                addr++;
        printf("%8x\n",addr);
}
```

![26](https://user-images.githubusercontent.com/51134298/60311815-ddaf3480-9993-11e9-9ae2-6cefe1458a52.png)

결과이다. /bin/sh의 주소는 0xb7f8db78 이다.

이제 페이로드를 짜면 끝난다.

 ![27](https://user-images.githubusercontent.com/51134298/60311816-de47cb00-9993-11e9-83f9-e56323c1cd75.png) 

성공했다. 이제 플래그를 찾으면 된다.

![28](https://user-images.githubusercontent.com/51134298/60311817-de47cb00-9993-11e9-9642-8c5aebf19880.png)

root 디렉토리의 Proof.txt에 플래그가 있었다.



