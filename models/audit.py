from models import db
from datetime import datetime


class AuditLog(db.Model):

    __tablename__ = "audit_log"

    log_id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employee.employee_id"),
        nullable=False
    )

    action = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(500))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    employee = db.relationship(
        "Employee",
        backref="audit_logs"
    )