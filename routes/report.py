from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import func, extract

from models import db
from models.employee import Employee
from models.task import Task

report = Blueprint("report", __name__)


@report.route("/reports")
@login_required
def reports():

    total_employees = Employee.query.count()

    total_tasks = Task.query.count()

    completed = Task.query.filter_by(status="Completed").count()

    pending = Task.query.filter_by(status="Pending").count()

    overdue = Task.query.filter_by(status="Overdue").count()

    # ---------------------------
    # Monthly Tasks
    # ---------------------------

    monthly_result = (
        db.session.query(
            extract("month", Task.assigned_date),
            func.count(Task.task_id)
        )
        .filter(Task.assigned_date != None)
        .group_by(extract("month", Task.assigned_date))
        .all()
    )

    monthly_data = [0] * 12

    for month, count in monthly_result:
        monthly_data[int(month) - 1] = count

    # ---------------------------
    # Platform Report
    # ---------------------------

    platform_result = (
        db.session.query(
            Task.platform,
            func.count(Task.task_id)
        )
        .group_by(Task.platform)
        .all()
    )

    platform_labels = [row[0] for row in platform_result]
    platform_data = [row[1] for row in platform_result]

    # ---------------------------
    # Complexity Report
    # ---------------------------

    complexity_result = (
        db.session.query(
            Task.complexity,
            func.count(Task.task_id)
        )
        .group_by(Task.complexity)
        .all()
    )

    complexity_labels = [row[0] for row in complexity_result]
    complexity_data = [row[1] for row in complexity_result]

    return render_template(
        "manager/reports.html",

        total_employees=total_employees,
        total_tasks=total_tasks,

        completed=completed,
        pending=pending,
        overdue=overdue,

        monthly_data=monthly_data,

        platform_labels=platform_labels,
        platform_data=platform_data,

        complexity_labels=complexity_labels,
        complexity_data=complexity_data
    )