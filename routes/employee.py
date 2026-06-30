from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, bcrypt
from models.employee import Employee
from models.audit import AuditLog

employee = Blueprint("employee", __name__)


@employee.route("/employees")
@login_required
def employees():

    search = request.args.get("search")

    if search:

        employees = Employee.query.filter(
            (Employee.full_name.ilike(f"%{search}%")) |
            (Employee.email.ilike(f"%{search}%")) |
            (Employee.username.ilike(f"%{search}%"))
        ).order_by(Employee.employee_id).all()

    else:

        employees = Employee.query.order_by(Employee.employee_id).all()

    return render_template(
        "manager/employees.html",
        employees=employees
    )


@employee.route("/add-employee", methods=["GET", "POST"])
@login_required
def add_employee():

    if request.method == "POST":

        full_name = request.form["full_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        if Employee.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
            return redirect(url_for("employee.add_employee"))

        if Employee.query.filter_by(email=email).first():
            flash("Email already exists!", "danger")
            return redirect(url_for("employee.add_employee"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_employee = Employee(
            company_id=1,
            full_name=full_name,
            email=email,
            phone=phone,
            username=username,
            password=hashed_password,
            role=role
        )

        db.session.add(new_employee)
        db.session.commit()

        # Audit Log
        log = AuditLog(
            employee_id=current_user.employee_id,
            action="Add Employee",
            description=f"Added employee {full_name}"
        )

        db.session.add(log)
        db.session.commit()

        flash("Employee added successfully!", "success")

        return redirect(url_for("employee.employees"))

    return render_template("manager/add_employee.html")


@employee.route("/edit-employee/<int:id>", methods=["GET", "POST"])
@login_required
def edit_employee(id):

    emp = Employee.query.get_or_404(id)

    if request.method == "POST":

        full_name = request.form["full_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        username = request.form["username"]
        role = request.form["role"]

        existing_email = Employee.query.filter(
            Employee.email == email,
            Employee.employee_id != id
        ).first()

        if existing_email:

            flash("Email already exists!", "danger")

            return redirect(url_for("employee.edit_employee", id=id))

        existing_username = Employee.query.filter(
            Employee.username == username,
            Employee.employee_id != id
        ).first()

        if existing_username:

            flash("Username already exists!", "danger")

            return redirect(url_for("employee.edit_employee", id=id))

        emp.full_name = full_name
        emp.email = email
        emp.phone = phone
        emp.username = username
        emp.role = role

        db.session.commit()

        # Audit Log
        log = AuditLog(
            employee_id=current_user.employee_id,
            action="Edit Employee",
            description=f"Updated employee {full_name}"
        )

        db.session.add(log)
        db.session.commit()

        flash("Employee updated successfully!", "success")

        return redirect(url_for("employee.employees"))

    return render_template(
        "manager/edit_employee.html",
        employee=emp
    )


@employee.route("/delete-employee/<int:id>", methods=["POST"])
@login_required
def delete_employee(id):

    emp = Employee.query.get_or_404(id)

    name = emp.full_name

    db.session.delete(emp)
    db.session.commit()

    # Audit Log
    log = AuditLog(
        employee_id=current_user.employee_id,
        action="Delete Employee",
        description=f"Deleted employee {name}"
    )

    db.session.add(log)
    db.session.commit()

    flash("Employee deleted successfully!", "success")

    return redirect(url_for("employee.employees"))