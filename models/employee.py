from flask_login import UserMixin
from models import db

class Employee(UserMixin, db.Model):
    __tablename__ = "employee"

    employee_id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(db.Integer)

    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))

    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(20))

    created_at = db.Column(db.DateTime)

    def get_id(self):
        return str(self.employee_id)