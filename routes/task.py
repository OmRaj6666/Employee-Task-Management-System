from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models.notification import Notification
from models import db
from models.employee import Employee
from models.task import Task
from models.audit import AuditLog  # Correct import

task = Blueprint("task", __name__)


@task.route("/tasks")
@login_required
def tasks():

    tasks = Task.query.order_by(Task.task_id.desc()).all()

    return render_template(
        "manager/tasks.html",
        tasks=tasks
    )


@task.route("/add-task", methods=["GET", "POST"])
@login_required
def add_task():

    employees = Employee.query.order_by(Employee.full_name).all()

    if request.method == "POST":

        employee_id = request.form["employee_id"]
        title = request.form["title"]
        description = request.form["description"]
        platform = request.form["platform"]
        complexity = request.form["complexity"]
        status = request.form["status"]
        due_date = request.form["due_date"]

        new_task = Task(
            employee_id=employee_id,
            company_id=1,
            title=title,
            description=description,
            platform=platform,
            complexity=complexity,
            status=status,
            due_date=due_date
        )

        db.session.add(new_task)
        
        # ============================================
        # CREATE NOTIFICATION FOR THE EMPLOYEE
        # ============================================
        notification = Notification(
            employee_id=employee_id,
            title="New Task Assigned",
            message=f"You have been assigned '{title}'."
        )
        db.session.add(notification)
        
        # Commit both task and notification together
        db.session.commit()
        
        # Get employee name for audit log
        employee = Employee.query.get(employee_id)
        employee_name = employee.full_name if employee else "Unknown"
        
        # Log add task action
        log = AuditLog(
            employee_id=current_user.employee_id,
            action="Assign Task",
            description=f"Assigned task '{title}' to {employee_name} (Platform: {platform}, Complexity: {complexity}, Status: {status})"
        )
        db.session.add(log)
        db.session.commit()

        flash("Task Assigned Successfully!", "success")

        return redirect(url_for("task.tasks"))

    return render_template(
        "manager/add_task.html",
        employees=employees
    )


@task.route("/edit-task/<int:id>", methods=["GET", "POST"])
@login_required
def edit_task(id):
    
    task_obj = Task.query.get_or_404(id)
    
    if request.method == "POST":
        
        # Store old values for audit log
        old_title = task_obj.title
        old_status = task_obj.status
        old_employee_id = task_obj.employee_id
        
        employee_id = request.form["employee_id"]
        title = request.form["title"]
        description = request.form["description"]
        platform = request.form["platform"]
        complexity = request.form["complexity"]
        status = request.form["status"]
        due_date = request.form["due_date"]
        
        task_obj.employee_id = employee_id
        task_obj.title = title
        task_obj.description = description
        task_obj.platform = platform
        task_obj.complexity = complexity
        task_obj.status = status
        task_obj.due_date = due_date
        
        db.session.commit()
        
        # Get employee names for audit log
        old_employee = Employee.query.get(old_employee_id)
        new_employee = Employee.query.get(employee_id)
        old_emp_name = old_employee.full_name if old_employee else "Unknown"
        new_emp_name = new_employee.full_name if new_employee else "Unknown"
        
        # Log edit task action
        log = AuditLog(
            employee_id=current_user.employee_id,
            action="Edit Task",
            description=f"Updated task '{old_title}' → '{title}' (Status: {old_status} → {status}, Employee: {old_emp_name} → {new_emp_name})"
        )
        db.session.add(log)
        db.session.commit()
        
        flash("Task updated successfully!", "success")
        return redirect(url_for("task.tasks"))
    
    employees = Employee.query.order_by(Employee.full_name).all()
    return render_template("manager/edit_task.html", task=task_obj, employees=employees)


@task.route("/delete-task/<int:id>", methods=["POST"])
@login_required
def delete_task(id):
    
    task_obj = Task.query.get_or_404(id)
    
    # Store task details for audit log
    task_title = task_obj.title
    employee_name = task_obj.employee.full_name if task_obj.employee else "Unknown"
    
    db.session.delete(task_obj)
    db.session.commit()
    
    # Log delete task action
    log = AuditLog(
        employee_id=current_user.employee_id,
        action="Delete Task",
        description=f"Deleted task '{task_title}' (Assigned to: {employee_name})"
    )
    db.session.add(log)
    db.session.commit()
    
    flash("Task deleted successfully!", "success")
    return redirect(url_for("task.tasks"))