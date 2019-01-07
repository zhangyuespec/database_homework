from pymysql import *

db_name = "resv"
str_mi = input("请输入数据库密码")


def cre_db():
    try:
        db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi,
                     charset="utf8")
        cursor = db.cursor()
        cursor.execute("show databases;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            tmp = "%2s" % row
            # print(tmp)
            if db_name == tmp:
                cursor.execute("drop database " + db_name + ";")
        print(22222)
        cursor.execute("create database " + db_name + ";")
        print(11111)
        db.commit()
    except Exception as f:
        print("发生错误")
    finally:
        cursor.close()
        db.close()


def cre_table():
    db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="%s" % db_name,
                 charset="utf8")
    cursor = db.cursor()
    sql_cars = "create table cars(type varchar(20),location varchar(255),price int(7),numCars int(4),numAvail int(4));"
    sql_customers = "create table customers(custName varchar(255),mima varchar(255));"
    sql_flights = "create table flights(flightNum varchar(255),price int(5),numSeats int(3),numAvail int(3),FromCity varchar(255),AricCity varchar(255));"
    sql_hotels = "create table hotels(name varchar(255),location varchar(255),price int(5),numRooms int(3),numAvail int(3));"
    sql_reservataions = "create table reservataions(custName varchar(20),resvType int(3),resvKey varchar(255));"
    cursor.execute("use %s" % db_name)
    cursor.execute(sql_cars)
    cursor.execute(sql_customers)
    cursor.execute(sql_flights)
    cursor.execute(sql_hotels)
    cursor.execute(sql_reservataions)

    db.commit()
    cursor.close()
    db.close()


def uf():
    sql1 = """alter table cars convert to charset utf8;"""
    sql2 = """alter table customers convert to charset utf8;"""
    sql3 = """alter table flights convert to charset utf8;"""
    sql4 = """alter table hotels convert to charset utf8;"""
    sql5 = """alter table reservataions convert to charset utf8;"""
    db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="%s" % db_name,
                 charset="utf8")
    cursor = db.cursor()
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    cursor.execute(sql5)
    cursor.close()
    db.close()


class Table_Cars():
    def cre(self, type, location, price, numCars, numA):
        db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="%s" % db_name,
                     charset="utf8")
        cursor = db.cursor()
        sql = """insert into cars values("%s","%s",%d,%d,%d)""" % (type, location, price, numCars, numA)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()


class Table_Customers():
    def cre(self, custName, mima):
        db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="%s" % db_name,
                     charset="utf8")
        cursor = db.cursor()
        sql = """insert into customers values("%s","%s")""" % (custName, mima)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()


class Table_Flights():
    def cre(self, glightNum, price, numSeats, numA, F, A):
        db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="%s" % db_name,
                     charset="utf8")
        cursor = db.cursor()
        sql = """insert into flights values("%s",%d,%d,%d,"%s","%s")""" % (glightNum, price, numSeats, numA, F, A)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()


class Table_Hotels():
    def cre(self, name, location, price, numR, numA):
        db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="%s" % db_name,
                     charset="utf8")
        cursor = db.cursor()
        sql = """insert into hotels values("%s","%s",%d,%d,%d)""" % (name, location, price, numR, numA)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()


class Table_Reservataions():
    def cre(self, custName, resvtype, rexvKey):
        db = connect(host="localhost", port=3306, user="root", password="%s" % str_mi, database="%s" % db_name,
                     charset="utf8")
        cursor = db.cursor()
        sql = """insert into reservataions values("%s",%d,"%s")""" % (custName, resvtype, rexvKey)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()


def table_Input():
    a = Table_Cars()
    a.cre("雪铁龙", "合肥", 50, 100, 20)
    a.cre("东风", "苏州", 40, 400, 50)
    a.cre("宝马", "上海", 100, 40, 5)
    a.cre("红旗", "滁州", 500, 1, 1)
    a.cre("奔驰", "北京", 100, 40, 1)

    b = Table_Customers()
    b.cre("zhangyue", "123456")

    c = Table_Flights()
    c.cre("东航255", 1000, 100, 50, "合肥", "厦门")
    c.cre("东航256", 1200, 100, 60, "南京", "合肥")
    c.cre("厦航265", 2300, 120, 20, "北京", "乌鲁木齐")
    c.cre("南航120", 2300, 120, 30, "苏州", "杭州")
    c.cre("北航220", 2300, 120, 90, "北京", "南京")
    c.cre("厦航120", 4500, 120, 56, "厦门", "苏州")

    d = Table_Hotels()
    d.cre("七天", "合肥", 120, 100, 20)
    d.cre("格林豪泰", "苏州", 123, 120, 20)
    d.cre("万达", "北京", 256, 120, 23)
    d.cre("靖江之星", "南京", 125, 300, 200)
    d.cre("香格里拉", "厦门", 450, 120, 56)


if __name__ == '__main__':
    cre_db()  # 建立数据库
    cre_table()  # 建立表
    uf()  # 解决中文插入问题
    table_Input()  # 初始化一些数据
