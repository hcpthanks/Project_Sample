
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

from personal.models import Employee

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/personal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/content/')
def text_content():
    return render_template('content.html')


@app.route('/ajax-basic/')
def ajax_basic():
    return render_template('ajax-basic.html')


@app.route('/employees/')
def employee_query():
    name = request.args.get('name', '')
    table_header = """
    <table border="1">
        <tr>
            <th>ID</th>  
            <th>姓名</th>  
            <th>地址</th>  
            <th>工资</th>  
        </tr>
    """
    employees = Employee.query.filter(Employee.name.contains(name)).all()
    rows = ""
    for emp in employees:
        rows += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            emp.id, emp.name, emp.address, emp.salary)
    table_footer = "</table>"

    return table_header + rows + table_footer


@app.route('/ajax-query/')
def ajax_query():
    return render_template('emp-query.html')


@app.route('/json/')
def json_demo():
    return render_template('json_demo.html')


#获取部门JSON数据
@app.route('/departments/')
def get_departments():
    depts = Department.query.all()
    return jsonify([d.to_json() for d in depts])


#员工查询服务端, 返回JSON
@app.route('/employees-json/')
def employee_query_json():
    departments = [{'id': 3, 'name': '财务部'}, {'id': 4, 'name': '技术部'}]
    return jsonify(departments)


@app.route('/emp-json/')
def emp_json():
    return render_template('emp-query-json.html')


@app.route('/reg/', methods=['POST', 'GET'])
def reg_user():
    if request.method == 'POST' and request.is_xhr:
        username = request.form.get('username', '')
        pwd = request.form.get('pwd', '')
        email = request.form.get('email', '')
        return jsonify(username)
    return render_template('reg-user.html')


@app.route('/checkuser/')
def check_user():
    name = request.args.get('username', '')
    names = ['tom', 'jerry', 'mike', 'peter']
    return jsonify(name.lower() not in names)

if __name__ == '__main__':
    app.run()
