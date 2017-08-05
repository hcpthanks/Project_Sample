from flask import render_template
from flask.views import View, MethodView


#基于类的视图

class RegUser(View):
    def dispatch_request(self):
        return render_template('reg.html')


class UserLogin(View):
    def dispatch_request(self):
        pass


#基于方法的视图
class MyRegUser(MethodView):
    def get(self):
        return render_template('reg.html')

    def post(self):
        # if request.method == 'POST':
        # pass
        return None