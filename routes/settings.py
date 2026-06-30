from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from models import db
from models import bcrypt

settings = Blueprint("settings", __name__)


@settings.route("/settings")
@login_required
def settings_page():

    return render_template("settings/settings.html")


@settings.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():

    if request.method == "POST":

        current_user.full_name = request.form["full_name"]
        current_user.email = request.form["email"]
        current_user.phone = request.form["phone"]

        db.session.commit()

        flash("Profile updated successfully.", "success")

        return redirect(url_for("settings.settings_page"))

    return render_template(
        "settings/edit_profile.html"
    )


@settings.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():

    if request.method == "POST":

        old_password = request.form["old_password"]
        new_password = request.form["new_password"]

        if not bcrypt.check_password_hash(
                current_user.password,
                old_password):

            flash("Old password is incorrect.", "danger")

            return redirect(
                url_for("settings.change_password")
            )

        current_user.password = bcrypt.generate_password_hash(
            new_password
        ).decode("utf-8")

        db.session.commit()

        flash("Password changed successfully.", "success")

        return redirect(
            url_for("settings.settings_page")
        )

    return render_template(
        "settings/change_password.html"
    )