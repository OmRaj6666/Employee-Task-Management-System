from flask import Blueprint, render_template
from flask_login import login_required
from models.audit import AuditLog

audit = Blueprint("audit", __name__)


@audit.route("/audit-logs")
@login_required
def audit_logs():

    logs = AuditLog.query.order_by(
        AuditLog.created_at.desc()
    ).all()

    return render_template(
        "manager/audit_logs.html",
        logs=logs
    )