import requests
from bs4 import BeautifulSoup
import json
from taobao import get_taobao_gate
from sql_unit import insert_sql
import datetime


def get_taobao_seller_list():
    """
    从taobao页获取到要爬取的分类的列表
    :return:
    """
    url_para = get_taobao_gate()
    return url_para


def get_taobao_seller(nums, para):
    """
    爬取店铺信息
    :param nums:页数
    :param url_para: 分类列表链接
    :return:
    """
    url = "https://shopsearch.taobao.com/search?data-key=s&data-value={0}&ajax=true&_" \
          "ksTS=1481770098290_1972&callback=jsonp602&app=shopsearch&q={1}&js=1&isb=0".format(nums, para)
    # 要保存到数据库的列表
    sql_data = []
    page = requests.get(url)
    print("正在获取店铺列表")
    wbdata = page.text[11:-2]
    data = json.loads(wbdata)
    shop_list = data['mods']['shoplist']['data']['shopItems']
    for r in shop_list:
        try:
            name = r['title']   # 店名
            nick = r['nick']    # 店主名
            totalsold = r['totalsold']  # 总销量
            procnt = r['procnt']    # 宝贝数量
            goodratepercent = r['goodratePercent']  # 好评率
            sql_data.append([name, nick, totalsold, procnt, goodratepercent])
        except:
            print("获取失败"+str(nums)+str(url_para))
    print(sql_data)
    insert_sql(sql_data)
    print("插入成功")


def task_func(url_para):
    """
    1.遍历参数列表
    2.爬取5000项
    :param url_para: 由taobao.py传入的参数列表
    :return:
    """
    sort_nums = 1
    # 记录插入条数
    a = 0
    b = 0
    for para in url_para:
        a += 1
        print("开始获取第%s个分类" % sort_nums)
        for nums in range(0, 100, 20):
            get_taobao_seller(str(nums), para)
            b += 1
        sort_nums += 1
    print("共插入数据：")
    print(a*b*20)


if __name__ == "__main__":
    starttime = datetime.datetime.now()
    url_para = get_taobao_seller_list()
    task_func(url_para)
    endtime = datetime.datetime.now()
    print("运行时间：")
    print(endtime-starttime)
