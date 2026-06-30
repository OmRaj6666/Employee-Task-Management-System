from models import db


class Task(db.Model):
    __tablename__ = "task"

    task_id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employee.employee_id"),
        nullable=False
    )

    company_id = db.Column(db.Integer, nullable=False)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text)

    platform = db.Column(db.String(50), nullable=False)

    complexity = db.Column(db.String(20), nullable=False)

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    assigned_date = db.Column(db.Date)

    due_date = db.Column(db.Date)

    completed_date = db.Column(db.Date)

    remarks = db.Column(db.String(500))

    employee = db.relationship(
        "Employee",
        backref="tasks"
    )