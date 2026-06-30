from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.task import Task
from models.audit import AuditLog
from models import db
from datetime import date

employee_portal = Blueprint(
    "employee_portal",
    __name__
)


# ==========================
# Employee Dashboard
# ==========================
@employee_portal.route("/employee-dashboard")
@login_required
def dashboard():

    employee_id = current_user.employee_id

    total = Task.query.filter_by(
        employee_id=employee_id
    ).count()

    completed = Task.query.filter_by(
        employee_id=employee_id,
        status="Completed"
    ).count()

    pending = Task.query.filter_by(
        employee_id=employee_id,
        status="Pending"
    ).count()

    overdue = Task.query.filter(
        Task.employee_id == employee_id,
        Task.status != "Completed",
        Task.due_date < date.today()
    ).count()

    tasks = Task.query.filter_by(
        employee_id=employee_id
    ).order_by(Task.task_id.desc()).limit(5).all()

    return render_template(
        "employee/dashboard.html",
        total=total,
        completed=completed,
        pending=pending,
        overdue=overdue,
        tasks=tasks
    )


# ==========================
# My Tasks
# ==========================
@employee_portal.route("/my-tasks")
@login_required
def my_tasks():

    tasks = Task.query.filter_by(
        employee_id=current_user.employee_id
    ).order_by(Task.task_id.desc()).all()

    return render_template(
        "employee/my_tasks.html",
        tasks=tasks
    )


# ==========================
# View Task Details
# ==========================
@employee_portal.route("/task/<int:id>")
@login_required
def view_task(id):

    task = Task.query.get_or_404(id)

    # Prevent users from viewing other employees' tasks
    if task.employee_id != current_user.employee_id:
        flash("Access Denied!", "danger")
        return redirect(url_for("employee_portal.dashboard"))

    return render_template(
        "employee/task_details.html",
        task=task
    )


# ==========================
# Employee Profile
# ==========================
@employee_portal.route("/profile")
@login_required
def profile():

    return render_template(
        "employee/profile.html"
    )
    
    # ==========================
# Update Task Status
# ==========================
@employee_portal.route("/update-task/<int:id>", methods=["GET", "POST"])
@login_required
def update_task(id):

    task = Task.query.get_or_404(id)

    # Employee can update only their own task
    if task.employee_id != current_user.employee_id:
        flash("Access Denied!", "danger")
        return redirect(url_for("employee_portal.dashboard"))

    if request.method == "POST":

        task.status = request.form["status"]
        task.remarks = request.form["remarks"]

        if task.status == "Completed":
            task.completed_date = date.today()

        db.session.commit()

        # Audit Log
        log = AuditLog(
            employee_id=current_user.employee_id,
            action="Task Updated",
            description=f"Updated task '{task.title}' to {task.status}"
        )

        db.session.add(log)
        db.session.commit()

        flash("Task updated successfully.", "success")

        return redirect(url_for("employee_portal.my_tasks"))

    return render_template(
        "employee/update_task.html",
        task=task
    )