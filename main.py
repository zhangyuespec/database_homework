import re
from pymysql import *

str_mi = input("请输入数据库密码")


def judge_cust():
    # 判断用户名是否可用
    print("----------------------")
    account = input("请输入您要创建的账号:")
    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv", charset="utf8")
    cs = con.cursor()
    cs.execute("select custName from customers; ")
    stock_custName = cs.fetchall()
    for name in stock_custName:
        # print(name)
        if name[0] == account:
            cs.close()
            con.close()
            return True, None

    cs.close()
    con.close()
    return False, account


def server_connect():  # 登录或者注册,注册调用判断用户名是否可用
    try:
        print("---------------------------------------------------")
        str = input("如果您有账号，请选择功能１，如果没有账号请选择功能０:")
        print("---------------------------------------------------")
        if str == "0":
            try:
                judge = True
                while (judge):
                    judge, accout = judge_cust()
                print("------------")
                mima = input("请输入您的密码:")

                con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                              charset="utf8")
                cs = con.cursor()
                sql_insert_accout = """insert into customers values("%s","%s");""" % (accout, mima)
                cs.execute(sql_insert_accout)
                # cs.execute("select *from customers;")
                # st=cs.fetchall()
                con.commit()
                log_str = "普通用户"
                return log_str, accout
                # print(st)
                cs.close()
                con.close()
            except Exception as h:
                print("--------")
                print("输入不合法")

        if str == "1":
            try:
                print("----------")
                cust_name = input("请输入用户名:")
                con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                              charset="utf8")
                cs = con.cursor()
                cs.execute("select * from customers; ")
                FLAG = False
                stock_custName = cs.fetchall()
                for name_mima in stock_custName:
                    if name_mima[0] == cust_name:  # 判断用户是否存在
                        log = False
                        while log is False:
                            print("------------")
                            cust_mima = input("请输入密码:")
                            log, log_str, cust_name2 = judge_log(cust_name, cust_mima)
                            if log_str != "密码不正确":
                                return log_str, cust_name2
                        FLAG = True

                if FLAG is False:  # 用户不存在就直接去注册
                    judge = True
                    while (judge):
                        judge, accout = judge_cust()
                    print("-------------")
                    mima = input("请输入您的密码:")

                    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                                  charset="utf8")
                    cs = con.cursor()
                    sql_insert_accout = """insert into customers values("%s","%s");""" % (accout, mima)
                    cs.execute(sql_insert_accout)
                    # cs.execute("select *from customers;")
                    # st=cs.fetchall()
                    con.commit()
                    log_str = "普通用户"
                    return log_str, accout
                    # print(st)
                    cs.close()
                    con.close()

            except Exception as i:
                print("输入不合法")

    except Exception as j:
        print("输入不合法")


def judge_log(cust_name, cust_mima):
    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv", charset="utf8")
    cs = con.cursor()
    cs.execute("select * from customers; ")
    stock_custName = cs.fetchall()
    for name in stock_custName:
        if name[0] == cust_name and cust_name != "zhangyue" and name[1] == cust_mima:
            print("-------")
            print("登录成功")
            return True, "普通用户", cust_name
        elif cust_name == "zhangyue" and cust_mima == "123456":
            print("------------")
            print("管理员登录成功")
            return True, "管理员", cust_name
        elif name[0] == cust_name and name[1] != cust_mima:
            print("---------")
            print("密码不正确")
            return False, "密码不正确"
    cs.close()
    con.close()

    # con = connect(host="localhost", port=3306, user="root", password="123456", database="resv", charset="utf8")
    # cs = con.cursor()
    # cs.execute("select * from customers ")
    # stock_customers = cs.fetchall()
    #
    # input("")


def ordinary_cust(cust_name):
    # 普通用户
    while True:
        try:

            print("------------------------------------------------------------------------------------------")
            str_ordinary = input("输入１查看航班。输入２查看出租。输入３查看宾馆。输入４预定。输入５查看自己的预定，输入６退出登录")
            print("------------------------------------------------------------------------------------------")
            if str_ordinary == "1":  # 打印航班信息
                con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                              charset="utf8")
                cs = con.cursor()
                sql = "select * from flights;"
                cs.execute(sql)
                stock_fights = cs.fetchall()
                for stock in stock_fights:
                    str_fights = "航班编号：%s,航班价格：%d,航班座位：%d,航班可用座位：%d,始发地：%s,到达地：%s/n" % (
                        stock[0], stock[1], stock[2], stock[3], stock[4], stock[5])
                    print("--------------------------------------------------------------------------")
                    print(str_fights)
                cs.close()
                con.close()

            if str_ordinary == "2":  # 打印出租车信息
                con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                              charset="utf8")
                cs = con.cursor()
                sql = "select * from cars;"
                cs.execute(sql)
                stock_cars = cs.fetchall()
                for stock in stock_cars:
                    str_cars = "出租车车型:%s,出租车所在地:%s,价格:%d,总数:%d,可用出租车数量:%d\n" % (
                        stock[0], stock[1], stock[2], stock[3], stock[4])
                    print("--------------------------------------------------------------------------")
                    print(str_cars)
                cs.close()
                con.close()

            if str_ordinary == "3":  # 打印宾馆信息
                con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                              charset="utf8")
                cs = con.cursor()
                sql = "select * from hotels;"
                cs.execute(sql)
                stock_hotels = cs.fetchall()
                for stock in stock_hotels:
                    str_hotels = "宾馆名称:%s,宾馆所在地:%s,价格:%d,房间总数:%d,可用房间数量:%d/n" % (
                        stock[0], stock[1], stock[2], stock[3], stock[4])
                    print("--------------------------------------------------------------------------")
                    print(str_hotels)
                cs.close()
                con.close()

            if str_ordinary == "4":  # 预定
                # print(cust_name)
                while True:
                    print("-------------------------------------------------------------")
                    print("-------------------------------------------------------------")
                    a = input("输入１预定航班，输入２预定出租，输入３预定宾馆,输入４返回上层目录:")
                    i = 0
                    j = 0
                    if a == "1":
                        try:
                            str_xinxi = input("依次输入预定航班编号,预定座位数量,以逗号分割:")
                            fights_num = str_xinxi.split(",")[0]
                            set_num = int(str_xinxi.split(",")[1])
                            sql = """insert into reservataions values("%s",%d,"%s")""" % (
                                cust_name, set_num, fights_num)
                            con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi,
                                          database="resv",
                                          charset="utf8")
                            cs = con.cursor()
                            # 查是否存在航班
                            cs.execute("select flightNum from flights;")
                            stock_flightsNum = cs.fetchall()
                            for stock in stock_flightsNum:
                                j += 1
                                if stock[0] != fights_num:
                                    i = i + 1
                            if i == j:
                                print("有没你要预定的航班编号")
                            elif i < j:
                                # 判断座位是否足够
                                cs.execute("select flightNum,numAvail from flights;")
                                stock_flightNum_numAvail = cs.fetchall()
                                for stock in stock_flightNum_numAvail:
                                    if stock[0] == fights_num:
                                        if stock[1] >= set_num:
                                            print("预定成功")
                                            cs.execute("""update flights set numAvail=%d where flightNum="%s";""" % (
                                                stock[1] - set_num, fights_num))
                                            cs.execute(sql)
                                            con.commit()
                                            cs.close()
                                            con.close()
                                        else:
                                            print("座位不够，无法预订")
                                            con.commit()
                                            cs.close()
                                            con.close()

                        except Exception as b:
                            print("输入不合法")

                    if a == "2":
                        try:
                            print("---------------------------------------------------------")
                            str_xinxi = input("请依次输入您要预定的车型，地点，数量，以逗号分隔：/n")
                            print("---------------------------------------------------------")
                            car_type = str_xinxi.split(",")[0]
                            location = str_xinxi.split(",")[1]
                            car_need = int(str_xinxi.split(",")[2])
                            con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi,
                                          database="resv",
                                          charset="utf8")
                            cs = con.cursor()
                            # 查询是否存在地点
                            cs.execute("select location from cars;")
                            lo = cs.fetchall()
                            for l in lo:
                                j += 1
                                if l[0] != location:
                                    i += 1
                            if i == j:
                                print("----------------------------")
                                print("您要预定的地方没有预定出租车服务")
                            elif i < j:
                                i = 0
                                j = 0
                                cs.execute("select type from cars;")
                                ct = cs.fetchall()
                                for c in ct:
                                    j += 1
                                    if c[0] != car_type:
                                        i += 1
                                if i == j:
                                    print("------------------------------")
                                    print("您所预定的城市没有这种车型的出租车")
                                elif i < j:
                                    cs.execute("select type,location,numAvail from cars;")
                                    san = cs.fetchall()
                                    for stock in san:
                                        if stock[0] == car_type and stock[1] == location:
                                            if stock[2] > car_need:
                                                print("预定成功/n")
                                                cs.execute(
                                                    """update cars set numAvail=%d where type="%s" and location="%s";""" % (
                                                        stock[2] - car_need, car_type, location))
                                                sql = """insert into reservataions values("%s",%d,"%s")""" % (
                                                    cust_name, car_need, car_type)
                                                cs.execute(sql)
                                                con.commit()
                                                cs.close()
                                                con.close()
                                            else:
                                                print("-------------------------")
                                                print("剩余的出租车不够，预定失败/n")
                                                con.commit()
                                                cs.close()
                                                con.close()

                        except Exception as a:
                            print("输入不合法")

                    if a == "3":
                        try:

                            print("---------------------------------------------------------")
                            print("---------------------------------------------------------")
                            str_xinxi = input("请依次输入您要预定的宾馆名称，地点，数量，以逗号分隔：")
                            car_type = str_xinxi.split(",")[0]
                            location = str_xinxi.split(",")[1]
                            car_need = int(str_xinxi.split(",")[2])
                            con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi,
                                          database="resv",
                                          charset="utf8")
                            cs = con.cursor()
                            # 查询是否存在地点
                            cs.execute("select location from hotels;")
                            lo = cs.fetchall()
                            for l in lo:
                                j += 1
                                if l[0] != location:
                                    i += 1
                            if i == j:
                                print("---------------------------")
                                print("您要预定的地方没有预定出租车服务")
                            elif i < j:
                                i = 0
                                j = 0
                                cs.execute("select name from cars;")
                                ct = cs.fetchall()
                                for c in ct:
                                    j += 1
                                    if c[0] != car_type:
                                        i += 1
                                if i == j:
                                    print("-------------------------------")
                                    print("您所预定的城市没有这种车型的出租车")
                                elif i < j:
                                    cs.execute("select name,location,numAvail from hotels;")
                                    san = cs.fetchall()
                                    for stock in san:
                                        if stock[0] == car_type and stock[1] == location:
                                            if stock[2] > car_need:
                                                print("预定成功/n")
                                                cs.execute(
                                                    """update hotels set numAvail=%d where name="%s" and location="%s";""" % (
                                                        stock[2] - car_need, car_type, location))
                                                sql = """insert into reservataions values("%s",%d,"%s")""" % (
                                                    cust_name, car_need, car_type)
                                                cs.execute(sql)
                                                con.commit()
                                                cs.close()
                                                con.close()
                                            else:
                                                print("--------------------------")
                                                print("剩余的房间数量不够，预定失败/n")
                                                con.commit()
                                                cs.close()
                                                con.close()

                        except Exception as a:
                            print("输入不合法\n\n")

                    if a == "4":
                        break

            if str_ordinary == "5":
                # print(11)
                con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                              charset="utf8")
                cs = con.cursor()
                # print(22)
                cs.execute("""select *from reservataions where custName="%s";""" % cust_name)
                # print(33)
                cu = cs.fetchall()

                # print(44)
                for c in cu:
                    print("-----------------------")
                    print("您预定了%s,预定数量为%d" % (c[2], c[1]))

                cs.close()
                con.close()

            if str_ordinary == "6":
                exit(1)

        except Exception as k:
            print("输入不合法kk\n\n")
            exit(1)


def administrator():
    # 管理员
    # print("欢迎管理员登录")
    while True:
        try:

            print("---------------------------------------------------------------------------")
            str_admini = input("输入１修改用户账号信息，输入２修改航班信息，输入３修改宾馆信息，输入４修改出租车信息，输入5修改用户预定信息,输入６退出系统:")
            print("---------------------------------------------------------------------------")
            if str_admini == "1":  # 修改账号密码
                while True:
                    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                                  charset="utf8")
                    cs = con.cursor()
                    sql = "select * from customers;"
                    cs.execute(sql)
                    all_cust = cs.fetchall()
                    for a in all_cust:
                        print("用户名：%s,密码：%s" % (a[0], a[1]))
                    try:

                        print("-----------------------------------------------------------")
                        change = input("无权限删除用户，如果想修改用户密码，请输入１,返回上一层输入２")
                        print("-----------------------------------------------------------")
                        if change == "1":
                            try:

                                print("--------------------------------------------------------------")

                                str_name_mima = input("请依次输入您要修改的用户的用户名和密码，用逗号分隔:")
                                print("--------------------------------------------------------------")
                                cust_name = str_name_mima.split(",")[0]
                                cust_mima = str_name_mima.split(",")[1]
                                try:
                                    sql = """update customers set mima="%s" where custName="%s";""" % (
                                        cust_mima, cust_name)
                                    cs.execute(sql)
                                    con.commit()
                                except Exception as d:
                                    print("没有你要修改的用户")
                            except Exception as c:
                                print("输入不合法")
                        if change == "2":
                            break

                    except Exception as b:
                        print("请直接输入１")

                    cs.close()
                    con.close()

            if str_admini == "2":
                while True:
                    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                                  charset="utf8")
                    cs = con.cursor()
                    sql = "select *from flights;"
                    cs.execute(sql)
                    all_flights = cs.fetchall()
                    for a in all_flights:
                        print("航班编号：%s,价格：%d,座位总数:%d,座位剩余数量:%d,始发地：%s,到达地：%s" % (a[0], a[1], a[2], a[3], a[4], a[5]))
                        print("---------------------------------------------------------------------------------------")
                    print("---------------------------------------------------------------------------------------")
                    print("---------------------------------------------------------------------------------------")
                    str_hanban = input("如果想增加航班输入１，如果想修改航班输入２，如果想删除航班输入３,如果想返回上一层输入４")
                    if str_hanban == "1":
                        # pass
                        try:
                            print("------------------------------------------------------------------------------")
                            print("------------------------------------------------------------------------------")
                            add_flights = input("请依次按照航班编号，价格，座位总数，剩余座位数量，始发地，到达地输入，中间用逗号分隔")
                            f_flights = add_flights.split(",")[0]
                            f_price = add_flights.split(",")[1]
                            f_numSeats = add_flights.split(",")[2]
                            f_numAvail = add_flights.split(",")[3]
                            f_FromCity = add_flights.split(",")[4]
                            f_AricCity = add_flights.split(",")[5]
                            con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi,
                                          database="resv",
                                          charset="utf8")
                            cs = con.cursor()
                            sql = """insert into flights values("%s",%d,%d,%d,"%s","%s");""" % (
                                f_flights, int(f_price), int(f_numSeats), int(f_numAvail), f_FromCity, f_AricCity)
                            cs.execute(sql)
                            con.commit()
                            cs.close()
                            con.close()

                        except Exception as t:
                            print("输入不合法11")

                    if str_hanban == "2":
                        print("----------------------------")
                        print("----------------------------")
                        fn = input("请输入想要修改的航班编号：")
                        try:
                            cs.execute("""select *from flights where flightNum='%s';""" % fn)
                        except Exception as fn:
                            print("没有这个航班编号")
                            break
                        print("--------------------------------------------------------------------")
                        print("--------------------------------------------------------------------")
                        str_pnnfa = input("请依次输入价格，总座位数，剩余座位数，始发地，达到地,中间以逗号隔开")
                        # print("zhix")
                        try:
                            str_p = int(str_pnnfa.split(",")[0])
                            str_ns = int(str_pnnfa.split(",")[1])
                            str_na = int(str_pnnfa.split(",")[2])
                            str_f = str_pnnfa.split(",")[3]
                            str_a = str_pnnfa.split(",")[4]

                            sql = """update flights set price=%d,numSeats=%d,numAvail=%d,FromCity="%s",AricCity="%s" where flightNum="%s";""" % (
                                str_p, str_ns, str_na, str_f, str_a, fn)
                            cs.execute(sql)

                            con.commit()
                            cs.close()
                            con.close()

                        except Exception as str_a:
                            print("请按照正确的格式输入")

                    if str_hanban == "3":
                        print("---------------------")
                        print("---------------------")
                        hangban = input("请输入您要删除的航班编号")
                        try:
                            cs.execute("""select *from flights where flightNum='%s'""" % hangban)
                        except Exception as fn:
                            print("没有这个航班编号")
                            break
                        sql = """delete from flights where flightNum="%s";""" % hangban
                        cs.execute(sql)
                        con.commit()
                        cs.close()
                        con.close()

                    if str_hanban == "4":
                        break

            if str_admini == "3":
                while True:
                    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                                  charset="utf8")
                    cs = con.cursor()
                    sql = "select * from hotels;"
                    cs.execute(sql)
                    all_flights = cs.fetchall()
                    for a in all_flights:
                        print("-----------------------------------------------------------------")
                        print("宾馆名称：%s,所在地：%s,价格:%d,房间总数:%d,剩余房间数量:%d" % (a[0], a[1], a[2], a[3], a[4]))
                        print("-----------------------------------------------------------------")
                    str_hanban = input("如果想增加宾馆输入１，如果想修改宾馆输入２，如果想删除宾馆输入３,如果想返回上一层输入４")
                    if str_hanban == "1":
                        # pass
                        try:
                            add_flights = input("请依次按照宾馆名称，所在地，价格，房间总数，房间剩余数量输入，中间用逗号分隔")
                            f_flights = add_flights.split(",")[0]
                            f_price = add_flights.split(",")[1]
                            f_numSeats = add_flights.split(",")[2]
                            f_numAvail = add_flights.split(",")[3]
                            f_FromCity = add_flights.split(",")[4]
                            # f_AricCity = add_flights.split(",")[5]
                            con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi,
                                          database="resv",
                                          charset="utf8")
                            cs = con.cursor()
                            sql = """insert into hotels values("%s","%s",%d,%d,%d);""" % (
                                f_flights, f_price, int(f_numSeats), int(f_numAvail), int(f_FromCity))
                            cs.execute(sql)
                            con.commit()
                            cs.close()
                            con.close()

                        except Exception as t:
                            print("输入不合法11")

                    if str_hanban == "2":
                        print("--------------------------")
                        print("--------------------------")
                        fn = input("请输入想要修改的宾馆名称：")
                        try:
                            cs.execute("""select *from hotels where name='%s';""" % fn)
                        except Exception as fn:
                            print("没有这个宾馆")
                            break
                        print("-------------------------------------------------------------")
                        print("-------------------------------------------------------------")
                        str_pnnfa = input("请依次输入所在地，价格，房间总数，剩余房间数量,中间以逗号隔开")
                        # print("zhix")
                        try:
                            str_p = str_pnnfa.split(",")[0]
                            str_ns = int(str_pnnfa.split(",")[1])
                            str_na = int(str_pnnfa.split(",")[2])
                            str_f = int(str_pnnfa.split(",")[3])
                            # str_a = str_pnnfa.split(",")[4]

                            sql = """update hotels set location="%s",price=%d,numRooms=%d,numAvail=%d where name="%s";""" % (
                                str_p, str_ns, str_na, str_f, fn)
                            cs.execute(sql)

                            con.commit()
                            cs.close()
                            con.close()

                        except Exception as str_a:
                            print("请按照正确的格式输入")

                    if str_hanban == "3":
                        print("-----------------------")
                        print("-----------------------")
                        hangban = input("请输入您要删除的宾馆名称")
                        try:
                            cs.execute("""select *from hotels where name='%s'""" % hangban)
                        except Exception as fn:
                            print("没有这个宾馆")
                            break
                        sql = """delete from hotels where name="%s";""" % hangban
                        cs.execute(sql)
                        con.commit()
                        cs.close()
                        con.close()

                    if str_hanban == "4":
                        break

            if str_admini == "4":
                while True:
                    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                                  charset="utf8")
                    cs = con.cursor()
                    sql = "select * from cars;"
                    cs.execute(sql)
                    all_flights = cs.fetchall()
                    for a in all_flights:
                        print("-----------------------------------------------------------------")
                        print("出租车类型：%s,所在地：%s,价格:%d,出租车总数:%d,剩余出租车数量:%d" % (a[0], a[1], a[2], a[3], a[4]))
                        print("-----------------------------------------------------------------")
                    str_hanban = input("如果想增加出租车输入１，如果想修改出租车输入２，如果想删除出租车输入３,如果想返回上一层输入４")
                    if str_hanban == "1":
                        # pass
                        try:
                            add_flights = input("请依次按照出租车名称，所在地，价格，出租车总数，出租车剩余数量输入，中间用逗号分隔")
                            f_flights = add_flights.split(",")[0]
                            f_price = add_flights.split(",")[1]
                            f_numSeats = add_flights.split(",")[2]
                            f_numAvail = add_flights.split(",")[3]
                            f_FromCity = add_flights.split(",")[4]
                            # f_AricCity = add_flights.split(",")[5]
                            con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi,
                                          database="resv",
                                          charset="utf8")
                            cs = con.cursor()
                            sql = """insert into cars values("%s","%s",%d,%d,%d);""" % (
                                f_flights, f_price, int(f_numSeats), int(f_numAvail), int(f_FromCity))
                            cs.execute(sql)
                            con.commit()
                            cs.close()
                            con.close()
                        except Exception as t:
                            print("输入不合法11")

                    if str_hanban == "2":
                        fn = input("请输入想要修改的出租车名称：")
                        try:
                            cs.execute("""select *from cars where type='%s';""" % fn)
                        except Exception as fn:
                            print("没有这个出租车")
                            break
                        str_pnnfa = input("请依次输入出租车所在地，价格，出租车总数，剩余出租车数量,中间以逗号隔开")
                        # print("zhix")
                        try:
                            str_p = str_pnnfa.split(",")[0]
                            str_ns = int(str_pnnfa.split(",")[1])
                            str_na = int(str_pnnfa.split(",")[2])
                            str_f = int(str_pnnfa.split(",")[3])
                            # str_a = str_pnnfa.split(",")[4]

                            sql = """update cars set location="%s",price=%d,numCars=%d,numAvail=%d where type="%s";""" % (
                                str_p, str_ns, str_na, str_f, fn)
                            cs.execute(sql)

                            con.commit()
                            cs.close()
                            con.close()

                        except Exception as str_a:
                            print("请按照正确的格式输入")

                    if str_hanban == "3":
                        print("--------------------------")
                        print("--------------------------")
                        hangban = input("请输入您要删除的出租车名称")
                        try:
                            cs.execute("""select *from cars where type='%s';""" % hangban)
                        except Exception as fn:
                            print("没有这个宾馆")
                            break
                        sql = """delete from cars where type="%s";""" % hangban
                        cs.execute(sql)
                        con.commit()
                        cs.close()
                        con.close()

                    if str_hanban == "4":
                        break

            if str_admini == "5":
                while True:
                    con = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="resv",
                                  charset="utf8")
                    cs = con.cursor()
                    sql = "select * from reservataions;"
                    cs.execute(sql)
                    all_flights = cs.fetchall()
                    for a in all_flights:
                        print("-----------------------------------------------------------------")
                        print("用户名%s,预定类型%s,预定数量%d" % (a[0], a[2], a[1]))
                        print("-----------------------------------------------------------------")
                    print("后台只能删除用户预定，增加预定只能由用户操作")
                    print("------------------------")
                    print("------------------------")
                    uu = input("删除请输入１，退出输入０")
                    if uu == "1":
                        print("------------------------")
                        print("------------------------")
                        str_cust_key = input("请输入要删除的用户和预定类型")
                        str_cust = str_cust_key.split(",")[0]
                        str_key = str_cust_key.split(",")[1]
                        try:
                            cs.execute(
                                "select *from reservataions where custName='%s' and resvKey='%s'" % (str_cust, str_key))
                        except Exception as ns:
                            print("没有您要删除的预定")
                        sql = """delete from reservataions where custName="%s" and resvKey="%s";""" % (
                        str_cust, str_key)
                        cs.execute(sql)
                        con.commit()
                        cs.close()
                        con.close()
                    if uu == "0":
                        break

            if str_admini == "6":
                break


        except Exception as k:
            print("-----------------")
            print("-----------------")
            print("没有你要选择的功能")


def main():

    log_str, cust_name = server_connect()
    # print(log_str)
    if log_str == "普通用户":
        ordinary_cust(cust_name)
    elif log_str == "管理员":
        administrator()


if __name__ == '__main__':
    main()
