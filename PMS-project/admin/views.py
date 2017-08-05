from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from personal.models import *
from personal.forms import EmployeeForm


# @admin.route('/emp/list/')
# @admin.route('emp/list/<int:page/'>
# def emp_list(page=1):
#     items = db.session.query(Employee).limit(10)
#     return render_template('admin/emp-list.html', items=items)

class EmployeeListView(MethodView):
    def get(self, page=1):
        items = Employee.query.paginate(page, per_page=18)
        return render_template('admin/emp-list.html', employees=items)


class EmployeeDelView(MethodView):
    def get(self, id=None):
        if id:
            emp = db.session.query(Employee).get(id)
            if emp:
                db.session.delete(emp)
                db.session.commit()
        return redirect(url_for('admin.emp_list'))


class EmployeeDelView(MethodView):
    def get(self, id=None):
        if id:
            emp = db.session.query(Employee).get(id)
            if emp:
                db.session.delete(emp)
                db.session.commit()

        return redirect(url_for('admin.emp_list'))


class EmployeeCreateView(MethodView):
    def get(self):
        departments = db.session.query(Department).all()
        return render_template('admin/emp-detail.html', departments=departments)

    def post(self):
        employee = Employee(
            request.form.get('name'),
            request.form.get('gender', '男'),
            request.form.get('job'),
            datetime.strptime(request.form.get('birthdate'), '%Y-%m-%d'),
            request.form.get('idcard'),
            request.form.get('address'),
            float(request.form.get('salary'))
        )
        employee.department_id = int(request.form.get('department_id'))

        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('.emp_list'))


class EmployeeCreateOrEdit(MethodView):
    def get(self, id=None):
        emp = Employee() if not id else db.session.query(Employee).get(id)

        form = EmployeeForm(request.form, obj=emp)
        form.department_id.choices = [(d.id, d.name) for d in Department.query.all()]
        return render_template('admin/emp-edit.html', form=form)

    def post(self, id=None):
        form = EmployeeForm(request.form)
        emp = Employee() if not id else db.session.query(Employee).get(id)
        form.populate_obj(emp)
        if not id:
            db.session.add(emp)
        db.session.commit()
        return redirect(url_for('.emp_list'))








