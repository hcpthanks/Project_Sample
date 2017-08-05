from flask_wtf import Form
import wtforms


class EmployeeForm(Form):
    name = wtforms.StringField('姓名')
    gender = wtforms.RadioField('性别', choices=[('男', '男'), ('女', '女')])
    job = wtforms.StringField('职位')
    birthdate = wtforms.DateField('生日')
    idcard = wtforms.StringField('身份证')
    address = wtforms.StringField('地址')
    salary = wtforms.DecimalField('工资')
    department_id = wtforms.SelectField('部门')


