#!/usr/bin/python3

import pymysql

def mysqlcon():

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "race_2018_f")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    gate_info_dic = {}
    # SQL 查询语句
    sql = "SELECT * FROM gates"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        i = 1
        for row in results:

            gate_info = []

            gate = row[0]
            hall = row[1]
            area = row[2]
            arr_type = row[3]
            dap_type = row[4]
            air_type = row[5]

            gate_info.append(gate)
            gate_info.append(hall)
            gate_info.append(area)
            gate_info.append(arr_type)
            gate_info.append(dap_type)
            gate_info.append(air_type)

            gate_info_dic[i] = gate_info

            i = i + 1

            # 打印结果
            print("\t%s\t%s\t%s\t%s\t%s\t%s" % \
                  (gate, hall, area, arr_type, dap_type, air_type))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return gate_info_dic

