import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup


def get_taobao_gate():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

    url = "https://shopsearch.taobao.com/search?app=shopsearch"
    # url任务将会保存到这个列表
    url_list = list()
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    # 设置浏览器头
    desired_capabilities["phantomjs.page.settings.userAgent"] = headers
    # 不载入图片
    desired_capabilities["phantomjs.page.settings.loadImages"] = False
    # proxy.add_to_capabilities(desired_capabilities)
    # 打开带配置信息的phantomJS浏览器
    driver = webdriver.PhantomJS(
        executable_path="E:\\phantomjs\\bin\\phantomjs.exe",
        desired_capabilities=desired_capabilities
        # service_args=['--ssl-protocol=any']
    )
    driver.start_session(desired_capabilities)
    # 隐式等待5秒
    driver.implicitly_wait(5)
    # 设置10秒超时返回
    driver.set_page_load_timeout(20)
    # 设置10秒脚本超时时间
    driver.set_script_timeout(20)
    try:
        driver.get(url)
        print("get分类列表成功")
    except:
        print("页面请求失败")
    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    soup_sort = soup.find_all("ul", class_="level-two-cat-list")
    cate_name = re.findall(r"q=(.*?)&amp;tracelog=shopsearchnoqcat", str(soup_sort))
    for i in cate_name:
        # 解码为中文
        # cname = urllib.parse.unquote(i, encoding='gb2312')
        # print(cname)
        url_list.append(i)
        # print(i)
    driver.close()
    return url_list

get_taobao_gate()