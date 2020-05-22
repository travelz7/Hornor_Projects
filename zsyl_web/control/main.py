import sys
sys.path.extend(['D:\\Python\\Projects\\zsyl_web\\venv\\Lib\\site-packages'])
import web
import pymysql


urls = (
    '/', 'index',
    '/add', 'add'
)
# globals() 函数会以字典类型返回当前位置的全部全局变量
app = web.application(urls, globals())

# 模板
render = web.template.render('templates/')
# 数据库
db = web.database(dbn='mysql', user='root', pw='zs960114.', db='runoob')


class index:
    def GET(self):
        todos = db.select('todo')
        return render.hello(todos)


class add:
    def POST(self):
        i = web.input()
        db.insert('todo', title=i.title)
        raise web.seeother('/')


if __name__ == '__main__':
    app.run()
