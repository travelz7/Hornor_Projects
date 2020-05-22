import sys
sys.path.extend(['D:\\Python\\Projects\\zsyl_web\\venv\\Lib\\site-packages'])
import web


urls = (
    '/', 'calendar'
)


app = web.application(urls, globals())
# 模板
render = web.template.render('../templates/')


class calendar:
    def GET(self):
        return render.calendar


if __name__ == '__main__':
    app.run()


