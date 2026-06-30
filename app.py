from flask import Flask
from config import Config

from models import db, bcrypt, login_manager
from models.employee import Employee

app = Flask(__name__)

app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


# ==========================
# Import Blueprints
# ==========================

from routes.auth import auth
from routes.employee import employee
from routes.employee_portal import employee_portal   # NEW
from routes.task import task
from routes.report import report
from routes.audit import audit
from routes.notification import notification   # NEW
from routes.settings import settings   # NEW


# ==========================
# Register Blueprints
# ==========================

app.register_blueprint(auth)
app.register_blueprint(employee)
app.register_blueprint(employee_portal)   # NEW
app.register_blueprint(task)
app.register_blueprint(report)
app.register_blueprint(audit)
app.register_blueprint(notification)   # NEW
app.register_blueprint(settings)   # NEW


if __name__ == "__main__":
    app.run(debug=True, port=5001)