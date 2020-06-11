import pymysql


# 打开数据库连接

db = pymysql.connect("192.168.57.114","mudou","123456","clustertest" )


# 使用cursor()方法获取操作游标

cursor = db.cursor()


#查询

sql = "select * from test_table"

try:
    cursor.execute(sql)

    result = cursor.fetchall()

    for row in result:
        name = row[0]
        value = row[1]
        #打印结果
        print('name = %s, value = %s' %(name,value))

except:
    print("Error: unable to fetch data")
db.close() 
