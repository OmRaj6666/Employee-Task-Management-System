from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models.notification import Notification
from models import db

notification = Blueprint(
    "notification",
    __name__
)


@notification.route("/notifications")
@login_required
def notifications():

    notifications = Notification.query.filter_by(
        employee_id=current_user.employee_id
    ).order_by(
        Notification.notification_id.desc()
    ).all()

    return render_template(
        "notifications.html",
        notifications=notifications
    )


@notification.route("/notification/read/<int:id>")
@login_required
def mark_read(id):

    note = Notification.query.get_or_404(id)

    if note.employee_id != current_user.employee_id:
        return redirect(url_for("notification.notifications"))

    note.is_read = "Y"

    db.session.commit()

    return redirect(url_for("notification.notifications"))