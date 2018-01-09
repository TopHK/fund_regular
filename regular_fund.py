# -*-: encoding: utf-8 -*-
from common import *


def get_nsfc_data():
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select code from nsfc")
    db.commit()
    nsfc_no_list = set()
    for row in cur.fetchall():
        if row[0] and len(row[0]) == 8:
            nsfc_no_list.add(row[0])
    db.close()
    return nsfc_no_list


def regular_nsfc_by_fundno():
    nsfc_fund_no_list = get_nsfc_data()
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select * from fund_2016_nsfc")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        # fund_name = row[1]
        fund_no = row[2].strip()

        fund_no_list = fund_no.split(',')
        for current_fund_no in fund_no_list:
            current_fund_no = current_fund_no.strip()
            if current_fund_no in nsfc_fund_no_list:
                count += 1
                cur.execute("update fund_2016_nsfc set a_prop2_nsfc='G' where ID='%d'" % ID)
                db.commit()
                break
    print(count)
    db.close()


def regular_nsfc_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select ID,fund_name from fund_2016_nsfc where a_prop2_nsfc is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1].strip()

        keyword_list = ["national nature science fund", "national natural science", "natural science foundation", "national natural fund", "national natural foundation",
                        "national natural scientific", "national nature science foundation", "national nature scientific"]
        keyword_list2 = ["nsfc", "nsfc of china", "nsfc china", "national nsfc"]
        if str_contains_one_keyword(fund_name, keyword_list) or str_equals_one_keyword(fund_name, keyword_list2):
            count += 1
            cur.execute("update fund_2016_nsfc set a_prop2_nsfc='G' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_nsfc_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='G'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_nsfc is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_nsfc='G' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print(count)
    print(count)
    db.close()


def check_nsfc_by_fundno():
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select * from fund_2016_nsfc")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        fund_no = row[2].strip()
        a_prop2_nsfc = row[3]
        if a_prop2_nsfc != 'G':
            fund_no_list = fund_no.split(',')
            for current_fund_no in fund_no_list:
                current_fund_no = current_fund_no.strip()
                if current_fund_no.isdigit() and len(current_fund_no) == 8:
                    print(current_fund_no)
                    count += 1
                    break
    print(count)
    db.close()


def regular_973_by_fundno():
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select ID,fund_no,fund_name from fund_2016_973")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_no = row[1].strip()
        fund_name = row[2].strip()

        fund_no_list = fund_no.split(',')
        for current_fund_no in fund_no_list:
            current_fund_no = current_fund_no.strip()
            if len(current_fund_no) == 12 and current_fund_no[4:6] == "CB" and current_fund_no[:2] == "20":
                count += 1
                # print(fund_name)
                cur.execute("update fund_2016_973 set a_prop2_973='973' where ID='%d'" % ID)
                db.commit()
                break
    print(count)
    db.close()


def regular_973_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select ID,fund_name from fund_2016_973 where a_prop2_973 is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1].strip()

        keyword_list = ["national basic research program of china",
                        "973 program",
                        "973 project",
                        "major state basic research projects",
                        "national key basic research",
                        "nkbrpc",
                        "major state basic research development",
                        "national basic research",
                        "national key project for basic research",
                        "973"]
        # keyword_list2 = ["nsfc", "nsfc of china", "nsfc china", "national nsfc"]
        if str_contains_one_keyword(fund_name, keyword_list):
            count += 1
            cur.execute("update fund_2016_973 set a_prop2_973='973' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_973_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='973'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_973 is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_973='973' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print(count)
    print(count)
    db.close()


def regular_863_by_fundno():
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select ID,fund_no,fund_name from fund_2016_863")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_no = row[1].strip()
        fund_name = row[2].strip()

        fund_no_list = fund_no.split(',')
        for current_fund_no in fund_no_list:
            current_fund_no = current_fund_no.strip()
            if len(current_fund_no) == 12 and current_fund_no[4:6] == "AA" and current_fund_no[:2] == "20":
                count += 1
                # print(fund_name)
                cur.execute("update fund_2016_863 set a_prop2_863='863' where ID='%d'" % ID)
                db.commit()
                break
    print(count)
    db.close()


def regular_863_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "root", "fund1014")
    cur.execute("select ID,fund_name from fund_2016_863 where a_prop2_863 is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1].strip()

        keyword_list = ["863 program",
                        "863 project",
                        "863",
                        "national high technology research",
                        "high technology research and development",
                        "national hi-tech research and development",
                        "national high technology development",
                        "national high-tech",
                        "china high-tech development",
                        "high-tech research and development",
                        "national high tech",
                        "national high-tech r&d"
                        ]
        # keyword_list2 = ["nsfc", "nsfc of china", "nsfc china", "national nsfc"]
        if str_contains_one_keyword(fund_name, keyword_list):
            count += 1
            cur.execute("update fund_2016_863 set a_prop2_863='863' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_863_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='863'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_863 is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_863='863' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print(count)
    print(count)
    db.close()


def regular_zky_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    cur.execute("select ID,fund_name from fund_2016_zky where a_prop2_zky is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1].strip()

        keyword_list = ["chinese academy of sciences",
                        "cas innovation program",
                        "foundation of cas",
                        "kunming institute of zoology",
                        "chinese academy of science",
                        " cas "
                        ]
        keyword_list2 = ["cas"]
        keyword_list3 = ["cas "]
        keyword_list4 = [" cas"]
        if str_contains_one_keyword(fund_name, keyword_list) or str_equals_one_keyword(fund_name, keyword_list2) \
                or str_starts_one_keyword(fund_name, keyword_list3) \
                or str_ends_one_keyword(fund_name, keyword_list4):
            count += 1
            cur.execute("update fund_2016_zky set a_prop2_zky='ZKY' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_zky_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='ZKY'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_zky is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_zky='ZKY' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print(count)
    print(count)
    db.close()


def regular_pla_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_pla is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1].strip()

        keyword_list = ["of pla ",
                        "chinese pla ",
                        "department of pla ",
                        "military twelfth",
                        "military medical",
                        "military science",
                        "liberation army",
                        "military scientific",
                        "army technology",
                        "military healthcare",
                        "beijing 302",
                        "military medicine",
                        "army foundation",
                        "309 hospital"
                        ]
        keyword_list2 = [
            "office of naval research",
            "office of china naval research",
            "military foundation",
            "pla",
        ]
        keyword_list3 = [
            "pla "
        ]
        keyword_list4 = [
            "department of pla",
            " pla"
        ]
        if str_contains_one_keyword(fund_name, keyword_list) or str_equals_one_keyword(fund_name, keyword_list2) \
                or str_starts_one_keyword(fund_name, keyword_list3) \
                or str_ends_one_keyword(fund_name, keyword_list4):
            count += 1
            cur.execute("update fund_2016_pla set a_prop2_pla='JFJ' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_pla_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='JFJ'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_pla is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_pla='JFJ' where ID='%d'" % ID)
            db.commit()
            if count % 20 == 0:
                print(count)
    print(count)
    db.close()


def regular_hk_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_hk is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        keyword_list = [
            "hong kong",
            "li ka shing",
            "li ka-shing",
            "wong education",
            "zheng ge ru",
            "sun chieh yeh",
            "hksar",
            "hkrgc",
            "hk rgc"
        ]
        keyword_list2 = [
            "hku",
            "hkust",
            "hkrgc"
        ]
        keyword_list3 = [
            "hku "
        ]
        keyword_list4 = [
            " hku"
        ]
        if str_contains_one_keyword(fund_name, keyword_list) or str_equals_one_keyword(fund_name, keyword_list2) \
                or str_starts_one_keyword(fund_name, keyword_list3) \
                or str_ends_one_keyword(fund_name, keyword_list4):
            count += 1
            cur.execute("update fund_2016_pla set a_prop2_hk='HK' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_hk_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='HK'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_hk is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_hk='HK' where ID='%d'" % ID)
            db.commit()
            if count % 20 == 0:
                print(count)
    print(count)
    db.close()


def regular_jyb_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='JYB' and fund_name like '%university%'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_jyb is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_jyb='JYB' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_jyb_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='JYB'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_jyb is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_jyb='JYB' where ID='%d'" % ID)
            db.commit()
    print(count)
    db.close()


def regular_S_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='S'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_s is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_s='S' where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print(count)
    print(count)
    db.close()


def regular_S_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get country list
    cur.execute("select province_en from province_list")
    db.commit()
    province_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 3:
            province_name_list.append(row[0].strip().lower())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_s is NULL and a_prop2_jyb is NULL"
                " and a_prop2_hk is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, province_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_s='S' where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print("S:%d" % count)
    print(count)
    db.close()


def regular_S_by_keywords3():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    province_name_list = ["wuhan", "zhengzhou", "changsha", "jinan", "taiyuan", "shijiazhuang", "chengdu", "lanzhou",
                          "hefei", "fuzhou", "guangzhou"]


    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_s is NULL and a_prop2_jyb is NULL"
                " and a_prop2_hk is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, province_name_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_s='S' where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print("S:%d" % count)
    print(count)
    db.close()


def regular_S_by_keywords4():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    province_name_list = ["taiwan"]

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_s is not NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, province_name_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_s=null where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print("TW:%d" % count)
    print(count)
    db.close()


def regular_pd_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='PD'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_pd is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_pd='PD' where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print(count)
    print(count)
    db.close()


def regular_rsb_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='RSB-DOC'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_rsb is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_rsb='RSB-DOC' where ID='%d'" % ID)
            db.commit()
            if count % 20 == 0:
                print(count)
    print(count)
    db.close()


def regular_bw_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='BW'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_bw is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_bw='BW' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print(count)
    print(count)
    db.close()


def regular_bwkj_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='BW-KJ'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_bw_kj is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_bw_kj='BW-KJ' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print(count)
    print(count)
    db.close()


def regular_w_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='W'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_w is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_w='W' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("W:%d" % count)
    print(count)
    db.close()


def regular_w_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get country list
    cur.execute("select country_en from country_list where state=0")
    db.commit()
    country_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 3:
            country_name_list.append(row[0].strip().lower())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_w is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, country_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_w='W' where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print("W:%d" % count)
    print(count)
    db.close()


def regular_w_by_keywords3():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get country list
    cur.execute("select state_en from america_list where state=0")
    db.commit()
    country_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 3:
            country_name_list.append(row[0].strip().lower())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_w is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, country_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_w='W' where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print("W:%d" % count)
    print(count)
    db.close()


def regular_w_by_keywords4():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    keyword_list = [
        "usa"
    ]
    keyword_lists2 = [
        "usa)", " usa ", "u.k.", " us "
    ]
    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_w is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_ends_one_keyword(fund_name, keyword_list) or str_contains_one_keyword(fund_name, keyword_lists2):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_w='W' where ID='%d'" % ID)
            db.commit()
            if count % 100 == 0:
                print("W:%d" % count)
    print(count)
    db.close()


def regular_c_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='C'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_c is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_c='C' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("C:%d" % count)
    print(count)
    db.close()


def regular_c_by_keywords2():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    keyword_list = [
        "inc.", " inc ", "ltd."
    ]
    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_c is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, keyword_list):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_c='C' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("C:%d" % count)
    print(count)
    db.close()


def regular_c_by_keywords3():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    keyword_lists = [
        "company", "huawei", "baidu", "tencent", "corporation"
    ]
    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_c is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_contains_one_keyword(fund_name, keyword_lists) or str_ends_one_keyword(fund_name, [' inc']):
            count += 1
            print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_c='C' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("C:%d" % count)
    print(count)
    db.close()


def regular_labk_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='LAB-K'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_labk is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_labk='LAB-K' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("LAB-K:%d" % count)
    print(count)
    db.close()


def regular_labz_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='LAB-Z'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_labz is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_labz='LAB-Z' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("LAB-Z:%d" % count)
    print(count)
    db.close()


def regular_tw_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='TW'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_tw is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_tw='TW' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("TW:%d" % count)
    print(count)
    db.close()


def regular_ma_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='MA'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_ma is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_ma='MA' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("MA:%d" % count)
    print(count)
    db.close()


def regular_sk_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='SK'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_sk is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_sk='SK' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("SK:%d" % count)
    print(count)
    db.close()


def regular_lh_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='LH'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_lh is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_lh='LH' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("LH:%d" % count)
    print(count)
    db.close()


def regular_yjy_by_keywords():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    # get jyb fund name in table sci_gf_fund_1015
    cur.execute("select fund_name from sci_gf_fund_1015 where a_prop2='YJY'")
    db.commit()
    fund_name_list = list()
    for row in cur.fetchall():
        temp_str = row[0].strip()
        if temp_str and len(temp_str) >= 2:
            fund_name_list.append(row[0].strip())

    cur.execute("select ID,fund_name from fund_2016_pla where a_prop2_yjy is NULL")
    db.commit()

    count = 0
    for row in cur.fetchall():
        ID = row[0]
        fund_name = row[1]
        if fund_name is None:
            continue
        fund_name = fund_name.strip()

        if str_equals_one_keyword(fund_name, fund_name_list):
            count += 1
            # print(fund_name)
            cur.execute("update fund_2016_pla set a_prop2_yjy='YJY' where ID='%d'" % ID)
            db.commit()
            if count % 50 == 0:
                print("YJY:%d" % count)
    print(count)
    db.close()


def regular_combine():
    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    cur.execute("select ID,a_prop2_nsfc,a_prop2_973,a_prop2_863,a_prop2_zky,a_prop2_pla,a_prop2_hk,"
                "a_prop2_jyb,a_prop2_s,a_prop2_pd,a_prop2_rsb,a_prop2_bw,a_prop2_bw_kj,a_prop2_w,"
                "a_prop2_c,a_prop2_labk,a_prop2_labz,a_prop2_tw,a_prop2_ma,a_prop2_sk,a_prop2_lh,a_prop2_yjy"
                " from fund_2016_pla")
    db.commit()

    count = 0
    for row in cur.fetchall():
        combine_result = list()
        ID = row[0]
        a_prop2_nsfc = row[1]
        a_prop2_973 = row[2]
        a_prop2_863 = row[3]
        a_prop2_zky = row[4]
        a_prop2_pla = row[5]
        a_prop2_hk = row[6]
        a_prop2_jyb = row[7]
        a_prop2_s = row[8]
        a_prop2_pd = row[9]
        a_prop2_rsb = row[10]
        a_prop2_bw = row[11]
        a_prop2_bw_kj = row[12]
        a_prop2_w = row[13]
        a_prop2_c = row[14]
        a_prop2_labk = row[15]
        a_prop2_labz = row[16]
        a_prop2_tw = row[17]
        a_prop2_ma = row[18]
        a_prop2_sk = row[19]
        a_prop2_lh = row[20]
        a_prop2_yjy = row[21]

        if a_prop2_lh is not None:
            combine_result.append(a_prop2_lh)
        if a_prop2_yjy is not None:
            combine_result.append(a_prop2_yjy)
        if a_prop2_pd is not None:
            combine_result.append(a_prop2_pd)
        if a_prop2_w is not None:
            combine_result.append(a_prop2_w)
        if a_prop2_c is not None:
            combine_result.append(a_prop2_c)
        if a_prop2_rsb is not None:
            combine_result.append(a_prop2_rsb)
        if a_prop2_bw is not None:
            combine_result.append(a_prop2_bw)
        if a_prop2_bw_kj is not None:
            combine_result.append(a_prop2_bw_kj)
        if a_prop2_labk is not None:
            combine_result.append(a_prop2_labk)
        if a_prop2_labz is not None:
            combine_result.append(a_prop2_labz)
        if a_prop2_sk is not None:
            combine_result.append(a_prop2_sk)
        if a_prop2_zky is not None:
            combine_result.append(a_prop2_zky)
        if a_prop2_tw is not None:
            combine_result.append(a_prop2_tw)
        if a_prop2_ma is not None:
            combine_result.append(a_prop2_ma)
        if a_prop2_hk is not None:
            combine_result.append(a_prop2_hk)
        if a_prop2_s is not None:
            combine_result.append(a_prop2_s)
        if a_prop2_jyb is not None:
            combine_result.append(a_prop2_jyb)
        if a_prop2_pla is not None:
            combine_result.append(a_prop2_pla)
        if a_prop2_973 is not None:
            combine_result.append(a_prop2_973)
        if a_prop2_863 is not None:
            combine_result.append(a_prop2_863)
        if a_prop2_nsfc is not None:
            combine_result.append(a_prop2_nsfc)

        count += 1
        if len(combine_result) >= 1:
            combine_result_str = ";".join(combine_result)
            final_result = combine_result[0]
            cur.execute("update fund_2016_pla set a_prop2_combine='%s',a_prop2='%s' where ID='%d'"
                        % (combine_result_str, final_result, ID))
            db.commit()
        if count % 500 == 0:
            print(count)
    print(count)
    db.close()


def regular_compare():
    import xlwt
    wb_w = xlwt.Workbook()
    sheet_w = wb_w.add_sheet("Sheet1")
    row_id = 0

    [db, cur] = MySQLdb_Connect("localhost", "root", "12345", "fund_2015")
    my_fund_dict = dict()
    cur.execute("select fund_name,a_prop2 from fund_2016_pla where a_prop2 is not NULL")
    db.commit()
    for row in cur.fetchall():
        my_fund_dict[row[0].strip().lower()] = row[1].strip()

    cur.execute("select FUND_NAME,A_PROP2 from sci_fund_2016_gf_copy")
    db.commit()
    fund_name_count = 0
    compare_count = 0
    total_count = 0
    for row in cur.fetchall():
        fund_name = row[0]
        a_prop2 = row[1]
        if a_prop2 is None or fund_name is None:
            continue
        fund_name_ori = fund_name.strip()
        fund_name = fund_name.strip().lower()
        a_prop2 = a_prop2.strip()
        if fund_name in my_fund_dict:
            fund_name_count += 1
            if my_fund_dict[fund_name] == a_prop2:
                compare_count += 1
            else:
                sheet_w.write(row_id, 0, fund_name_ori)
                sheet_w.write(row_id, 1, a_prop2)
                sheet_w.write(row_id, 2, my_fund_dict[fund_name])
                row_id += 1
        total_count += 1
    print(total_count)
    print(fund_name_count)
    print(compare_count)
    print(compare_count / float(fund_name_count))
    db.close()
    wb_w.save("fund_missing.xls")


def main():
    # get_country_name_list()
    # get_province_name_list()
    # get_america_state_list()

    # regular_nsfc_by_fundno()
    # regular_nsfc_by_keywords()
    # check_nsfc_by_fundno()

    # regular_973_by_fundno()
    # regular_973_by_keywords()

    # regular_863_by_fundno()
    # regular_863_by_keywords()

    # regular_zky_by_keywords()
    # regular_pla_by_keywords()

    # regular_hk_by_keywords()
    # regular_hk_by_keywords2()

    # regular_jyb_by_keywords()
    # regular_jyb_by_keywords2()
    # regular_jyb_by_keywords3()

    # regular_S_by_keywords()
    # regular_S_by_keywords2()
    # regular_S_by_keywords3()
    # regular_S_by_keywords4()

    # regular_pd_by_keywords()

    # regular_rsb_by_keywords()

    # regular_bw_by_keywords()

    # regular_bwkj_by_keywords()

    # ready: 973
    # regular_973_by_keywords2()

    # # ready: 863
    # regular_863_by_keywords2()

    # # ready: nsfc
    # regular_nsfc_by_keywords2()

    # # ready: zky
    # regular_zky_by_keywords2()

    # regular_c_by_keywords()
    # regular_c_by_keywords2()
    # regular_c_by_keywords3()

    # regular_w_by_keywords()
    # regular_w_by_keywords2()
    # regular_w_by_keywords3()
    # regular_w_by_keywords4()

    # regular_labk_by_keywords()
    # regular_labz_by_keywords()

    # regular_tw_by_keywords()
    # regular_ma_by_keywords()
    # regular_sk_by_keywords()
    # regular_lh_by_keywords()
    # regular_yjy_by_keywords()
    regular_combine()
    regular_compare()



if __name__ == '__main__':
    main()
