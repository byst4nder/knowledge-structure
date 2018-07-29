# encoding=utf-8
import pymysql
# connection 用于数据库连接，获取数据库对象，cursor，数据库交互对象，exception数据库异常类。
'''
    https://blog.csdn.net/yjz_sdau/article/details/79211309
    
    流程：
    1、创建connection,创建数据库连接对象，
    2、然后调用cursor方法，返回cursor对象，对数据库进行操作，
    3、cursor调用方法，执行命令，获取数据处理出数据，
    4、然后关闭cursor，关闭connection（否则占用资源）,结束。
'''

# connection对象的方法：
#       cursor()：使用该链接并返回游标，
#       commit()：提交当前事务,
#       rollback()：回滚当前事务，
#       close()：关闭连接 。

'''
    游标对象：用于执行查询和获取结果。
    excute()：执行数据库查询和命令，将数据库语句送到数据库执行，数据库将对象返回客户端缓冲池。
    fetchone()：去的结果集的下一行；
    fetchmany(size)：获取结果集的下几行；
    fetchall()：获取结果集中的剩下所有行；
    rowcount()：最近一次execute返回数据的行数或者影响的行数。
    close()：关闭是游标对象。
    fetch*()方法：通过rownumber指针返回数据；
        比如开始时候，rownumber=0，调用fetchone，ruwnumber+1,返回第一条数据。
'''
try:
    # 建立数据库连接：
    conn = pymysql.connect(
        host='192.168.85.20',
        port=3306,
        db='follow',
        user='root',
        passwd='123456',
        charset='utf8'
        # 此处若是填写utf-8则报错：'NoneType'object has no attribute 'encoding'。
    )

    # 获取游标
    cursor = conn.cursor()
    # print(conn)
    # print(cursor)

    # 1、从数据库中查询
    # sql="INSERT INTO login(user_name,pass_word)"
    sql = "SELECT * FROM login"
    # cursor执行sql语句
    cursor.execute(sql)
    # 打印执行结果的条数
    print(cursor.rowcount)

    # 使用fetch方法进行遍历结果  总共有三条数据

    # rs=cursor.fetchone()#将第一条结果放入rs中
    # re=cursor.fetchmany(3)#将多个结果放入re中
    rr = cursor.fetchall()  # 将所有的结果放入rr中
    # 对结果进行处理
    for row in rr:
        print("ID是：%s, 姓名是：%s, 密码是：%s" % row)
    # print(re)#输出两条数据，因为fetch()方法是建立在上一次fetch()方法基础上的

    # 2数据库中插入数据
    sql_insert = "INSERT INTO login(user_name,pass_word) values('中兴','123')"
    # 执行语句
    cursor.execute(sql_insert)
    # 事务提交，否则数据库得不到更新
    conn.commit()
    print(cursor.rowcount)
    # 数据库插入多条数据

    # 修改数据库中的内容
    sql_update = "UPDATE login SET user_name='hhh' WHERE id=3"
    cursor.execute(sql_update)
    conn.commit()

    # 删除数据库中的内容，并利用try catch语句进行事务回滚
    try:
        sql_delete = "DELETE FROM login WHERE id=6"
        cursor.execute(sql_delete)
        conn.commit()
    except Exception as e:
        print(e)
        # 事务回滚，即出现错误后，不会继续执行，而是回到程序未执行的状态，原先执行的也不算了
        conn.rollback()

    # 数据库连接和游标的关闭
    conn.close()
    cursor.close()

except Exception as e:
    print(e)


