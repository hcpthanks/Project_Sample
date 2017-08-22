from flask import Flask, request, make_response, render_template
from flask import Flask, redirect, url_for, abort
import json


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    #创建一个响应对象response
    resp = make_response()
    resp.response = render_template('index.html')      #响应内容
    resp.headers['Content-type'] = 'application/json'  #ContentType
    resp.status_code = 200
    return resp


@app.route('/user-info/')
def user_info():
    name = 'tom'
    return render_template('user-info.html', name=name)


@app.route('/help/')
def req_help():
    abort(404)


@app.route('/rq/')
def test_rq():
    data = {}
    data['ip'] = request.remote_addr
    data['full_path'] = request.full_path
    data['url'] = request.url
    data['is_xhr'] = request.is_xhr
    data['endpoint'] = request.endpoint
    return str(data)


if __name__ == '__main__':
    app.run()