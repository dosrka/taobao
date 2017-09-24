import pymysql
import traceback

def connect_rule():
    """
    定义需要链接的数据库
    :return:
    """
    conn = pymysql.connect(host="192.168.2.137",
                           port=3306,
                           user="root",
                           passwd="123456",
                           db="taobao",
                           charset="utf8")
    return conn


def insert_sql(content):
    """
    将传入的列表插入数据库
    :param s:
    :return:
    """
    conn = connect_rule()
    cursor = conn.cursor()
    sql = "INSERT INTO taobao1 (tradename , nick, totalsold, procnt, goodratepercent) VALUES (%s, %s, %s, %s, %s)"
    defeated = []
    for key in content:
        try:
            cursor.execute(sql, key)
        except:
            print("插入失败"+str(key))
            print(traceback.print_exc())
            defeated.append(key)
    if len(defeated) >= 1:
        print(defeated)
    conn.commit()
    cursor.close()
    conn.close()
