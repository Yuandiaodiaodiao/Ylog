import tornado.ioloop
import tornado.web
import json
import pymysql
import time


class Mysqldb:
    def __init__(self, post):
        self.db = pymysql.connect(host='blog.yuandiaodiaodiao.cn',
                                  user='blog',
                                  password='Wangzixi1108',
                                  db='blog',
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
        self.post = post

    def __enter__(self):
        return self.db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.db.commit()
        else:
            self.db.rollback()
            self.post.write(json.dumps(
                {'code': 'db error', }
            ))
        self.db.close()


def change_str(strs):
    strs = strs.replace("\\", "\\\\")
    strs = strs.replace("'", "\\'")
    strs = strs.replace('"', '\\"')
    return strs


def rechange_str(strs):
    """
    转义字符处理
    :param strs:
    :return:
    """
    strs = strs.replace("\\\\", "\\")
    strs = strs.replace("\\''", "'")
    strs = strs.replace('\\"', '"')
    return strs

#登陆
class LoginHandler(tornado.web.RequestHandler):
    """
    登陆class
    """
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', f"{self.request.headers['Origin']}")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def get(self):
        username = self.get_cookie('username')
        password = self.get_cookie('password')

        print(f'username={username} password={password}')
        with Mysqldb(self) as cursor:
            sql = f"select * from 用户 where 昵称 = '{username}' and 密码 = '{password}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(f'login {result}')
            if result is not None:
                self.write(json.dumps(
                    {'code': 'success', 'uid': result['uid']}
                ))
            else:
                self.write(json.dumps(
                    {'code': 'error username'}
                ))

#注册
class RegisterHandler(LoginHandler):

    def get(self):
        self.set_default_headers()
        username = self.get_cookie('username')
        password = self.get_cookie('password')

        print(f'username={username} password={password}')
        with Mysqldb(self) as cursor:
            sql = f"select * from 用户 where 昵称 = '{username}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) == 1:
                self.write(json.dumps(
                    {'code': 'error exists'}
                ))
            else:
                sql = f"insert into 用户 select max(uid)+1 ,'{username}','{password}' from 用户"
                cursor.execute(sql)
                self.write(json.dumps(
                    {'code': 'success'}
                ))

#创建博客
class CreateHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', f"{self.request.headers['Origin']}")
        self.set_header("Access-Control-Allow-Headers", "content-type,")
        self.set_header('Access-Control-Allow-Methods', 'POST,OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def post(self):
        self.set_default_headers()
        js = json.loads(self.request.body)
        print(f'create {js}')
        title = change_str(js['title'])
        value = change_str(js['value'])
        uid = js['uid']
        if js['bid'] == -1:
            with Mysqldb(self) as cursor:
                sql = "select max(bid)+1 from 博客"
                cursor.execute(sql)
                res1 = cursor.fetchone()
                bid = res1["max(bid)+1"]
                if bid is None:
                    bid = 1
                sql = f"""insert into 博客 values ( {bid} ,
                 {uid} , '{title}' , '{value}' , 
                 {int(time.time())} ,{int(time.time())}, 0 ) """
                cursor.execute(sql)
                self.write(json.dumps({
                    'code': 'success',
                    'bid': bid
                }))
                return
        else:
            with Mysqldb(self) as cursor:
                bid = js['bid']
                sql = f"delete  from 博客 where bid = '{bid}' "
                cursor.execute(sql)
                sql = f"""insert into 博客 values ( {bid} ,
                            {uid} , '{title}' , '{value}' , 
                            {int(time.time())} ,{int(time.time())}, 0 ) """
                cursor.execute(sql)
                self.write(json.dumps({
                    'code': 'success',
                    'bid': bid
                }))
                return

#拉取文章内容
class ArticleHandler(CreateHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', f"{self.request.headers['Origin']}")
        self.set_header("Access-Control-Allow-Headers", "content-type,charset=utf-8")
        self.set_header('Access-Control-Allow-Methods', 'POST,OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def post(self):
        self.set_default_headers()
        js = json.loads(self.request.body)
        bid = js['bid']
        with Mysqldb(self) as cursor:
            sql = f"select * from 博客 where bid= '{bid}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result is not None:
                result['code'] = 'success'
                result['title'] = rechange_str(result['title'])
                result['value'] = rechange_str(result['value'])
                self.write(json.dumps(result))
            else:
                self.write(json.dumps({
                    'code': 'false'
                }))

#获取10个文章
class GetTenHandlder(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', f"{self.request.headers['Origin']}")
        self.set_header("Access-Control-Allow-Headers", "content-type,charset=utf-8")
        self.set_header('Access-Control-Allow-Methods', 'POST,OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def post(self):
        self.set_default_headers()
        js = json.loads(self.request.body)
        unix_time = js['time']
        bigger = js['cmp']
        desc = 'desc'
        if bigger == '>':
            desc = 'asc'
        with Mysqldb(self) as cursor:
            sql = f"select * from 博客 where 编辑时间 {bigger} '{unix_time}' order by 编辑时间 {desc}"
            cursor.execute(sql)
            result = cursor.fetchmany(10)
            if len(result) >= 1:
                for x in result:
                    uid = x['uid']
                    sql = f"select * from 用户 where uid = '{uid}'"
                    cursor.execute(sql)
                    res2 = cursor.fetchone()
                    x['username'] = res2['昵称']
                self.write(json.dumps({
                    'code': 'success',
                    'js': result
                }))
            else:
                self.write(json.dumps({
                    'code': 'failed'
                }))

#获取个人的所有文章
class GetMyHandlder(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', f"{self.request.headers['Origin']}")
        self.set_header("Access-Control-Allow-Headers", "content-type,charset=utf-8")
        self.set_header('Access-Control-Allow-Methods', 'POST,OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def post(self):
        self.set_default_headers()
        js = json.loads(self.request.body)
        unix_time = js['time']
        bigger = js['cmp']
        desc = 'desc'
        if bigger == '>':
            desc = 'asc'
        uid = js['uid']
        with Mysqldb(self) as cursor:
            sql = f"select * from 博客 where 编辑时间 {bigger} '{unix_time}' and uid = '{uid}' order by 编辑时间 {desc}"
            cursor.execute(sql)
            result = cursor.fetchmany(10)
            if len(result) >= 1:
                self.write(json.dumps({
                    'code': 'success',
                    'js': result
                }))
            else:
                self.write(json.dumps({
                    'code': 'failed'
                }))

#删除文章
class DelHandlder(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', f"{self.request.headers['Origin']}")
        self.set_header("Access-Control-Allow-Headers", "content-type,charset=utf-8")
        self.set_header('Access-Control-Allow-Methods', 'POST,OPTIONS')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def post(self):
        self.set_default_headers()
        js = json.loads(self.request.body)
        bid = js['bid']
        with Mysqldb(self) as cursor:
            sql = f"delete  from 博客 where bid = '{bid}' "
            cursor.execute(sql)


def make_app():
    return tornado.web.Application([
        (r"/api/login", LoginHandler),
        (r"/api/register", RegisterHandler),
        (r"/api/create", CreateHandler),
        (r"/api/article", ArticleHandler),
        (r"/api/getten", GetTenHandlder),
        (r"/api/getmy", GetMyHandlder),
        (r"/api/del", DelHandlder)

    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(1024)
    print('stard')
    tornado.ioloop.IOLoop.current().start()
