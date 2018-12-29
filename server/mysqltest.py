import pymysql


class Mysqldb:
    def __init__(self):
        self.db = pymysql.connect(host='blog.yuandiaodiaodiao.cn',
                                  user='blog',
                                  password='Wangzixi1108',
                                  db='blog',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor
                                  )

    def __enter__(self):
        return self.db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        if exc_type is not None:
            self.db.commit()
        else:
            self.db.rollback()
        self.db.close()


with Mysqldb() as cursor:
    sql = "select * from 用户 where 昵称 = 'abc'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
