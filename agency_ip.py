import requests
from bs4 import BeautifulSoup


def proxies_list():
    """
    爬取ip代理，只显示响应速度一秒以下的ip
    :return:代理ip与端口A
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

    try:
        page = requests.get("http://www.xicidaili.com/wt/", headers=headers)
        bs0bj = BeautifulSoup(page.text, "lxml")

        i = 0
        b = 0
        ip_port = []

        for odd in bs0bj.find_all("tr", class_="odd"):
            speed = odd.find("div", title=True).get("title")[:-1]
            b += 1
            if float(speed) < 1:
                ip = odd.find_all("td")[1].text
                port = odd.find_all("td")[2].text
                # print(ip, port)
                ip_port.append(ip+":"+port)
                i += 1

        return ip_port
    except:
        print("ip代理获取异常")
