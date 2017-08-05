import os
import sqlite3
from datetime import datetime

from flask import Flask, request, render_template, url_for, redirect, g, flash
from flask import Flask, send_from_directory, session, make_response
from account.views import RegUser, UserLogin, MyRegUser
from article.views import article


app = Flask(__name__)
app.debug = True
app.secret_key = "sdsdf234353478077&&##%%$$"

database_url = r'.\db\feedback.db'
UPLOAD_FOLDER = r'.\uploads'
ALLOWED_EXTENSIONS = ['.jpg', '.png', '.gif']

app.register_blueprint(article)


# 呈现特定目录下的资源
@app.route('/profile/<filename>/')
def render_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# 检查文件是否允许上传
def allowed_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS


#把数据库元祖转化为字典表形式
def make_dicts(cursor, row):
    return dict((cursor.description[i][0], value) for i, value in enumerate(row))


# 获取(建立数据库连接)
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database_url)
        db.row_factory = make_dicts
    return db


# 执行sql语句不返回数据结果
def execute_sql(sql, prms=()):
    c = get_db().cursor()
    c.execute(sql, prms)
    c.connection.commit()


# 执行用于选择数据的SQL语句
def query_sql(sql, prms=(), one=False):
    c = get_db().cursor()
    result = c.execute(sql, prms).fetchall()
    c.close()
    return (result[0] if result else None) if one else result


# 关闭连接
@app.teardown_appcontext
def close_connection(exeption):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sql = "select count(*) as [count] from userinfo WHERE username=? and password = ?"
        result = query_sql(sql, (username, password), one=True)
        if int(result.get('count')) > 0:
            session['admin'] = username
            return redirect(url_for('feedback_list'))
        flash('用户或密码错误')
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('admin')
    return redirect(url_for('feedback_list'))


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/feedback/')
def feedback():
    conn = sqlite3.connect(database_url)
    c = conn.cursor()
    sql = "select rowid,categoryname from category"
    categories = c.execute(sql).fetchall()

    c.close()
    conn.close()
    return render_template('post.html', categories=categories)


@app.route('/post_feedback/', methods=['POST'])
def post_feedback():
    if request.method == 'POST':
        subject = request.form['subject']
        categoryid = request.form.get('category', 1)
        username = request.form.get('username')
        email = request.form.get('email')
        body = request.form.get('body')
        is_processed = 0
        release_time = datetime.now()
        img_path = None

        if request.files.get('screenshot', None):
            img = request.files['screenshot']
            if allowed_file(img.filename):
                img_path = datetime.now().strftime('%Y%m%d%H%M%f') + os.path.splitext(img.filename)[1]
                img.save(os.path.join(UPLOAD_FOLDER, img_path))

        conn = sqlite3.connect(database_url)
        c = conn.cursor()
        sql = "insert into feedback (Subject, CatogoryID, UserName, Email, Body, Isprocessed, Releasetime,Image) VALUES (?,?,?,?,?,?,?,?)"
        c.execute(sql, (subject, categoryid, username, email, body, is_processed, release_time, img_path))
        conn.commit()
        conn.close()

        return redirect(url_for('feedback'))


@app.route('/admin/list/')
def feedback_list():
    if session.get('admin', None) is None:
        return redirect(url_for('login'))
    else:
        key = request.args.get('key', '')
        sql = "select f.ROWID,f.*,c.categoryname from feedback f INNER JOIN category c on c.ROWID = f.CatogoryID WHERE f.Subject LIKE ?ORDER by f.ROWID DESC "
        feedbacks = query_sql(sql, ('%{}%'.format(key),))
        return render_template('feedback-list.html', items=feedbacks)


@app.route('/admin/edit/<id>/')
def edit_feedback(id=None):
    if session.get('admin', None) is None:
        return redirect(url_for('login'))
    else:
        sql = "select rowid,categoryname from category"
        categories = query_sql(sql)

        sql = "select rowid,* from feedback WHERE rowid = ?"
        current_feedback = query_sql(sql, (id,), one=True)
        return render_template('edit.html', categories=categories, item=current_feedback)


@app.route('/admin/save_edit/', methods=['POST'])
def save_feedback():
    if request.method == 'POST':
        rowid = request.form.get('rowid', None)
        reply = request.form.get('reply')
        is_processed = 1 if request.form.get('isprocessed', 0) == 'on' else 0
        sql = 'update feedback set reply=?, isprocessed=? where rowid = ?'
        conn = sqlite3.connect(database)
        c = conn.cursor()
        c.execute(sql, (reply, is_processed, rowid))
        conn.commit()
        conn.close()

        return redirect(url_for('feedback_list'))


@app.route('/admin/feedback/del/<id>/')
def delete_feedback(id=0):
    sql = "delete from feedback WHERE rowid = ?"
    execute_sql(sql, (id,))
    return redirect(url_for('feedback_list'))


#设置cookie
@app.route('/setck/')
def set_mycookie():
    resp = make_response('ok')
    resp.set_cookie('username', 'hcpthanks', path= '/', expires=datetime.now() + timedelta(days=7))
    return resp


@app.route('/getck/')
def get_mycookie():
    ck = request.cookies.get('username', None)
    if ck:
        return ck
    return '未找到'


@app.route('/rmck/')
def remove_cookie():
    resp = make_response('删除cookie')
    resp.set_cookie('username', '', expires=0)
    return resp


#为导入基于类的视图添加分配URL规则
# app.add_url_rule('/reg/', view_func=RegUser.as_view('reg_user'))
app.add_url_rule('/reg/', view_func=MyRegUser.as_view('reg_user'))


if __name__ == '__main__':
    app.run()
