# -*-: encoding: utf-8 -*-
import requests
import json
import MySQLdb
from bs4 import BeautifulSoup

def requests_post(url, data, headers=None):
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Connection': 'keep-alive',
                'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Host': 'steamspy.com',
                # 'Origin': 'http://steamspy.com',
                'Proxy-Connection': 'keep-alive',
                # 'Referer': 'http://steamspy.com/app/578080',
                # 'X-Requested-With': 'XMLHttpRequest'
               }
    try:
        response = requests.post(url, data=data, headers=headers)
        return response.content
    except:
        return None

def parse_json(content):
    result = dict()
    try:
        result = json.loads(content)
    except:
        pass
    return result


def get_beautifulsoup_object(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    headers = {'User-Agent': user_agent}
    request_session = requests.Session()
    response = request_session.get(url, headers=headers)
    try:
        # print(response.encoding)
        response.encoding = 'gbk'
        page_response = response.text
        bs_obj = BeautifulSoup(page_response.encode(response.encoding).decode('utf-8'), 'html.parser')
    except:
        bs_obj = BeautifulSoup(page_response, 'html.parser')
    return bs_obj


def MySQLdb_Connect(host, user, passwd, db):
    db = MySQLdb.connect(host=host,    # your host, usually localhost
                         user=user,         # your username
                         passwd=passwd,           # 数据库密码
                         db=db,      # 选择数据库的名字
                         charset= "utf8")     # 数据库编码方式
    cur = db.cursor()
    return [db, cur]


def str_contains_one_keyword(test_str, keyword_list):
    for keyword in keyword_list:
        if keyword in test_str:
            # print("word:%s" % keyword)
            return True
    return False


def str_contains_all_keywords(test_str, keyword_list):
    for keyword in keyword_list:
        if keyword not in test_str:
            return False
    return True


def str_equals_one_keyword(test_str, keyword_list):
    for keyword in keyword_list:
        if keyword == test_str:
            return True
    return False


def str_starts_one_keyword(test_str, keyword_list):
    for keyword in keyword_list:
        if test_str.startswith(keyword):
            return True
    return False


def str_ends_one_keyword(test_str, keyword_list):
    for keyword in keyword_list:
        if test_str.endswith(keyword):
            return True
    return False

def get_country_name_list():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    baidu_url = u"https://baike.baidu.com/item/%E4%B8%AD%E8%8B%B1%E6%96%87%E5%9B%BD%E5%AE%B6%E5%AF%B9%E7%85%A7%E8%A1%A8/341490?fr=aladdin"
    page_obj = get_beautifulsoup_object(baidu_url)
    # print(page_obj.prettify())
    table_elem = page_obj.find(class_='table-view log-set-param')
    tr_elems = table_elem.find_all('tr')
    for tr_elem in tr_elems:
        td_elems = tr_elem.find_all('td')
        if td_elems and len(td_elems) == 3:
            country_name_en = td_elems[0].text.strip()
            country_name_abb = td_elems[1].text.strip()
            country_name_ch = td_elems[2].text.strip()
            # print(country_name_en)
            # print(country_name_abb)
            try:
                country_name_en = country_name_en.replace("'", "\\'")
                country_name_ch = country_name_ch.replace("'", "\\'")
                sql_str = "insert into country_list" \
                          "(country_en, country_en_abbre, country_ch)" \
                          "values('%s', '%s', '%s');" \
                          % (country_name_en, country_name_abb, country_name_ch)
                cur.execute(sql_str)
                cur.connection.commit()
            except Exception as e:
                print(str(e))


def get_province_name_list():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    file_stream = open("province.txt", 'r')
    for line in file_stream.readlines():
        line_list = line.strip().split()
        province_name_en = line_list[0]
        province_name_ch = line_list[-1]
        try:
            sql_str = "insert into province_list" \
                      "(province_en, province_ch, state)" \
                      "values('%s', '%s', '%d');" \
                      % (province_name_en, province_name_ch, 0)
            cur.execute(sql_str)
            cur.connection.commit()
        except Exception as e:
            print(str(e))


def get_america_state_list():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    baidu_url = u"http://114.xixik.com/usa-stats/"
    page_obj = get_beautifulsoup_object(baidu_url)
    # print(page_obj.prettify())
    table_elem = page_obj.find('table')
    tr_elems = table_elem.find_all('tr')
    for tr_elem in tr_elems:
        td_elems = tr_elem.find_all('td')
        if td_elems and len(td_elems) == 5:
            state_name_en = td_elems[1].text.strip()
            state_name_abb = td_elems[2].text.strip()
            state_name_ch = td_elems[0].text.strip()
            # print(state_name_en)
            # print(state_name_ch)
            try:
                state_name_en = state_name_en.replace("'", "\\'")
                state_name_ch = state_name_ch.replace("'", "\\'")
                sql_str = "insert into america_list" \
                          "(state_en, state_en_abbre, state_ch)" \
                          "values('%s', '%s', '%s');" \
                          % (state_name_en, state_name_abb, state_name_ch)
                cur.execute(sql_str)
                cur.connection.commit()
            except Exception as e:
                print(str(e))