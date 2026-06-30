from models import db
from datetime import datetime


class Notification(db.Model):
    __tablename__ = "notification"

    notification_id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employee.employee_id"),
        nullable=False
    )

    title = db.Column(db.String(200), nullable=False)

    message = db.Column(db.String(500))

    is_read = db.Column(
        db.String(1),
        default="N"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    employee = db.relationship(
        "Employee",
        backref="notifications"
    )