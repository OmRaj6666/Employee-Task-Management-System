from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import func
from datetime import datetime

from models import db, bcrypt
from models.employee import Employee
from models.task import Task
from models.audit import AuditLog

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        employee = Employee.query.filter_by(username=username).first()

        if employee and bcrypt.check_password_hash(employee.password, password):

            login_user(employee)

            # Audit Log
            log = AuditLog(
                employee_id=employee.employee_id,
                action="Login",
                description="User logged into the system"
            )

            db.session.add(log)
            db.session.commit()

            # Role Based Redirect
            if employee.role.lower() == "manager":
                return redirect(url_for("auth.dashboard"))
            else:
                return redirect(url_for("employee_portal.dashboard"))

        flash("Invalid Username or Password", "danger")

    return render_template("auth/login.html")


@auth.route("/dashboard")
@login_required
def dashboard():

    total_employees = Employee.query.count()

    completed = Task.query.filter_by(status="Completed").count()

    pending = Task.query.filter_by(status="Pending").count()

    today = datetime.now().date()

    overdue = Task.query.filter(
        Task.status != "Completed",
        Task.due_date < today
    ).count()

    recent_tasks = Task.query.order_by(
        Task.task_id.desc()
    ).limit(5).all()

    current_year = datetime.now().year

    monthly_data = []

    for month in range(1, 13):

        count = Task.query.filter(
            func.extract("month", Task.assigned_date) == month,
            func.extract("year", Task.assigned_date) == current_year
        ).count()

        monthly_data.append(count)

    return render_template(
        "manager/dashboard.html",
        total_employees=total_employees,
        completed=completed,
        pending=pending,
        overdue=overdue,
        recent_tasks=recent_tasks,
        monthly_data=monthly_data,
        current_user=current_user
    )


@auth.route("/logout")
@login_required
def logout():

    log = AuditLog(
        employee_id=current_user.employee_id,
        action="Logout",
        description="User logged out of the system"
    )

    db.session.add(log)
    db.session.commit()

    logout_user()

    flash("Logged out successfully.", "success")

    return redirect(url_for("auth.login"))